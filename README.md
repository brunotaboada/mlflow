# MLflow + promptings for vibe coding software development process.

The idea of this template is to help those interested to understand and implement the vibe coding software development process in their team. This comes with a open source AI-powered agent named kilo and some pre-defined agents, rules and md templates. It also comes with the mlflow prompt manager to help you manage and optimize your prompts and md templates.

## 📋 Overview

This project provides a robust framework for:
- Registering markdown-based prompts with MLflow
- Optimizing prompts using MLflow's GenAI capabilities
- Tracking prompt performance and evolution
- Managing instruction templates and technical specifications

## 🚀 Features

### Core Functionality
- **Prompt Registration**: Automatically register markdown files as MLflow prompts
- **Prompt Optimization**: Use MLflow's GenAI optimizer to improve prompt quality
- **Performance Tracking**: Track prompt performance metrics over time
- **Template Management**: Organize instruction templates and technical specifications

### Key Components
- **register_mds.py**: Main script for registering markdown prompts
- **optimize_mlflow.py**: Advanced prompt optimization with enhanced feedback
- **Instruction Templates**: Pre-defined templates for various use cases
- **SQLite Database**: Local MLflow tracking database

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- MLflow
- SQLite

### Setup
```bash
# Clone the repository
git clone https://github.com/your-repo/mlflow-prompt-manager.git
cd mlflow-prompt-manager

# Install dependencies
pip install -r requirements.txt

# Set up virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

## 📁 Project Structure

```
mlflow/
├── .gitignore                # Git ignore rules
├── .kilocode/                # Configuration and rules
├── .kilocodemodes            # Mode configurations
├── .venv/                    # Python virtual environment
├── .vscode/                  # VSCode configuration
├── instructions/             # Instruction templates
│   ├── arquitect.md          # Architecture instructions
│   ├── create_tasks.md       # Task creation instructions
│   └── tech_spec.md          # Technical specification template
├── templates/                # Document templates
│   ├── plan-template.md      # Project planning template
│   ├── task-template.md      # Task management template
│   ├── tasks-template.md     # Task management template
│   └── techspec-template.md  # Technical specification template
├── optimize_mlflow.py        # Prompt optimization script
├── register_mds.py           # Main prompt registration script
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🎯 Usage

### Registering Prompts

```bash
# Register all markdown files as MLflow prompts
python register_mds.py
```

This will:
1. Connect to the local MLflow SQLite database
2. Scan the `instructions/`, `.kilocode/rules/`, and `templates/` directories
3. Register each markdown file as an MLflow prompt
4. Log the registration process

### Optimizing Prompts

```bash
# Run prompt optimization
python optimize_mlflow.py
```

This will:
1. Initialize the enhanced GEPA optimizer
2. Register instruction prompts
3. Run optimization with detailed feedback
4. Log optimization results to MLflow

## 🔧 Configuration

### MLflow Tracking
The system uses SQLite for local tracking:
```python
mlflow.set_tracking_uri("sqlite:///mlflow.db")
```

### Customization
- **Prompt Templates**: Modify files in `instructions/` and `templates/`
- **Optimization Parameters**: Adjust in `optimize_mlflow.py`
- **Database Location**: Change the SQLite path as needed

## 📊 Example Workflow

1. **Create Instruction Templates**: Add new `.md` files to the `instructions/` directory
2. **Register Prompts**: Run `register_mds.py` to register them with MLflow
3. **Optimize Prompts**: Run `optimize_mlflow.py` to improve prompt quality
4. **Track Performance**: Monitor results in the MLflow UI

## 🔍 Technical Details

### Enhanced GEPA Optimizer
The `EnhancedGepaPromptOptimizer` provides:
- Detailed initialization feedback
- Progress tracking
- Performance metrics
- Optimization insights

### Error Handling
- Comprehensive error handling for file operations
- Graceful handling of missing directories
- Detailed error messages for debugging

## 📈 Performance Metrics

The system tracks:
- Initial vs. final evaluation scores
- Optimization improvement percentages
- Prompt versioning and evolution
- Execution time and resource usage

## 🎓 Learning Resources

### MLflow Documentation
- [MLflow Official Docs](https://mlflow.org/docs/latest/index.html)
- [MLflow GenAI Guide](https://mlflow.org/docs/latest/genai/index.html)

### Prompt Engineering
- [Prompt Engineering Guide](https://learnprompting.org/)
- [MLflow Prompt Optimization](https://mlflow.org/docs/3.2.0/genai/prompt-registry/optimize-prompts/)

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:
1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add appropriate tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 📧 Contact

For questions or support, please contact:
- Project Maintainer: [Bruno Taboada]
- Email: [bruno.taboada@gmail.com]

---

© 2025 MLflow Prompt Management System. All rights reserved.