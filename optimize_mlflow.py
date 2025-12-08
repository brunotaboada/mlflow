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

def _read_md_content(file_path: str) -> str:
    """
    Read markdown content from a file and return it as a string.

    Args:
        file_path: Path to the markdown file

    Returns:
        The content of the markdown file as a string

    Raises:
        FileNotFoundError: If the file doesn't exist
        IOError: If there's an error reading the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Markdown file not found: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading markdown file: {e}")

def read_all_instruction_md_files():
    """
    Read all markdown files under the /instructions directory and register them as MLflow prompts.

    Args:
        None

    Returns:
        None

    Raises:
        FileNotFoundError: If the instructions directory doesn't exist
        IOError: If there's an error reading any of the files
    """
    import os
    from pathlib import Path

    instructions_dir = Path("instructions")
    if not instructions_dir.exists():
        raise FileNotFoundError(f"Instructions directory not found: {instructions_dir}")

    md_files = list(instructions_dir.glob("*.md"))
    if not md_files:
        return

    for md_file in md_files:
        try:
            content = _read_md_content(str(md_file))
            # Extract prompt name from filename (remove .md extension)
            prompt_name = md_file.stem
            # Register the prompt with MLflow
            mlflow.genai.register_prompt(
                name=prompt_name,
                template=content
            )
            print(f"📝 Registered prompt '{prompt_name}' from {md_file}")
        except Exception as e:
            raise IOError(f"Error reading file {md_file}: {e}")

def main():
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    # mlflow.set_experiment("my-genai-experiment")

    # prompt = mlflow.genai.register_prompt(
    #     name="math_tutor",
    #     template="Answer this math question: {{question}}. Provide a clear explanation.",
    # )

    # result = mlflow.genai.optimize_prompts(
    #     predict_fn=predict_fn,
    #     train_data=prepare_training_data(),
    #     prompt_uris=[prompt.uri],
    #     optimizer=EnhancedGepaPromptOptimizer(
    #         reflection_model="ollama:/qwen3-coder:480b-cloud",
    #         max_metric_calls=2,
    #         display_progress_bar=True  # Enable progress bar for better visibility
    #     ),
    #     scorers=[Correctness(model="ollama:/qwen3-coder:480b-cloud")],
    # )

    print("✅ Optimization completed!")

    # The optimized prompt is automatically registered as a new version
    # optimized_prompt = result.optimized_prompts[0]
    # print(f"🎯 Optimized prompt registered as version {optimized_prompt.version}")
    # print(f"📝 Template: {optimized_prompt.template}")

    # if result.initial_eval_score is not None and result.final_eval_score is not None:
    #     if result.final_eval_score >= result.initial_eval_score:
    #         improvement = result.final_eval_score - result.initial_eval_score
    #         if improvement > 0:
    #             print(f"📈 Score improved by {improvement:.2f} (from {result.initial_eval_score:.2f} to {result.final_eval_score:.2f})")
    #         else:
    #             print(f"✅ Already optimal! Score: {result.final_eval_score:.2f} (no improvement needed)")
    #     else:
    #         print(f"⚠️  Score: {result.final_eval_score:.2f} (initial: {result.initial_eval_score:.2f})")
    # else:
    #     print(f"🎯 Final score: {result.final_eval_score}")

    _log_test_run()

def predict_fn(question: str) -> str:
        prompt = mlflow.genai.load_prompt("prompts:/math_tutor@latest")
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
                    "question": "What is 15 + 27?"
                },
                "expectations": {
                    "expected_response": "42"
                }
            },
            {
                "inputs": {
                    "question": "Calculate 8 × 9"
                },
                "expectations": {
                    "expected_response": "72"
                }
            },
            {
                "inputs": {
                    "question": "What is 100 - 37?"
                },
                "expectations": {
                    "expected_response": "63"
                }
            }
        ]

if __name__ == "__main__":
    main()
    read_all_instruction_md_files()
    