#!/usr/bin/env python3

import mlflow
from mlflow.genai.optimize import GepaPromptOptimizer
from mlflow.genai.scorers import Correctness
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import requests

class EnhancedGepaPromptOptimizer(GepaPromptOptimizer):
    """
    Enhanced GEPA optimizer with better feedback about the optimization process.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("🤖 Enhanced GEPA Optimizer initialized")
        print("   - Reflection model:", self.reflection_model)
        print("   - Max metric calls:", self.max_metric_calls)
        print("   - Progress bar:", "enabled" if self.display_progress_bar else "disabled")
        print("💡 Tip: 'All subsample scores perfect' means your prompt is already optimal!")
        print("💡 Tip: 'Reflective mutation did not propose' means no improvement was found (this is good!)")


def main():
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("my-genai-experiment")

    prompt = mlflow.genai.load_prompt("tasks-template")

    result = mlflow.genai.optimize_prompts(
        predict_fn=predict_fn,
        train_data=prepare_training_data(),
        prompt_uris=[prompt.uri],
        optimizer=EnhancedGepaPromptOptimizer(
            reflection_model="ollama:/qwen3-coder:480b-cloud",
            max_metric_calls=10,
            display_progress_bar=True  # Enable progress bar for better visibility
        ),
        scorers=[Correctness(model="ollama:/qwen3-coder:480b-cloud")],
    )

    print("✅ Optimization completed!")

    # The optimized prompt is automatically registered as a new version
    optimized_prompt = result.optimized_prompts[0]
    print(f"🎯 Optimized prompt registered as version {optimized_prompt.version}")
    print(f"📝 Template: {optimized_prompt.template}")

    if result.initial_eval_score is not None and result.final_eval_score is not None:
        if result.final_eval_score >= result.initial_eval_score:
            improvement = result.final_eval_score - result.initial_eval_score
            if improvement > 0:
                print(f"📈 Score improved by {improvement:.2f} (from {result.initial_eval_score:.2f} to {result.final_eval_score:.2f})")
            else:
                print(f"✅ Already optimal! Score: {result.final_eval_score:.2f} (no improvement needed)")
        else:
            print(f"⚠️  Score: {result.final_eval_score:.2f} (initial: {result.initial_eval_score:.2f})")
    else:
        print(f"🎯 Final score: {result.final_eval_score}")

    _log_test_run()

def predict_fn(question: str) -> str:
        prompt = mlflow.genai.load_prompt("prompts:/tasks-template@latest")
        # Use Ollama instead of OpenAI
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen3-coder:480b-cloud",
                "prompt": prompt.format(question=question),
                "stream": False
            }
        )
        return response.json()["response"]

def _log_test_run():
    """Log a test run to MLflow for connectivity verification."""
    with mlflow.start_run():
        mlflow.log_param("test_param", "test_value")
        print("✓ Successfully connected to MLflow!")

def prepare_training_data():
        """Prepare training data with inputs and expectations."""
        return [
            {
                "inputs": {
                    "question": "1. Do the work. 2. Do something else."
                },
                "expectations": {
                    "expected_response": "[1] 1.0 Do the work. [2] 1.0 Do something else."
                }
            },
            {
                "inputs": {
                    "question": "3. Do the work. 4. Do something else."
                },
                "expectations": {
                    "expected_response": "[3] 3.0 Do the work. [4] 4.0 Do something else."
                }
            }
        ]

if __name__ == "__main__":
    main()
    