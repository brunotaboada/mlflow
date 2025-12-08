#!/usr/bin/env python3

import mlflow
from mlflow.genai.optimize import GepaPromptOptimizer
from mlflow.genai.scorers import Correctness
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

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

def read_all_instruction_md_files(path: str):
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
    from pathlib import Path

    dir = Path(path)
    if not dir.exists():
        raise FileNotFoundError(f"Instructions directory not found: {dir}")

    md_files = list(dir.glob("*.md"))
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
    _log_test_run()

def _log_test_run():
    """Log a test run to MLflow for connectivity verification."""
    with mlflow.start_run():
        mlflow.log_param("test_param", "test_value")
        print("✓ Successfully connected to MLflow!")
        
if __name__ == "__main__":
    main()
    read_all_instruction_md_files('instructions')
    read_all_instruction_md_files('.kilocode/rules')
    read_all_instruction_md_files('templates')
    print("✅ Registrations completed!")
    