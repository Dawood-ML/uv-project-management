# Customer Churn Prediction

**Production-grade ML pipeline with modern dependency management using UV.**

## 📋 Project Overview

Predicts customer churn using machine learning with a focus on:
- ✅ Reproducible environments (pyproject.toml + uv.lock)
- ✅ Modular code structure
- ✅ Comprehensive testing
- ✅ Production-ready patterns

## 🏗️ Project Structure
```
customer-churn-prediction/
├── pyproject.toml          # Project metadata & dependencies
├── uv.lock                 # Locked dependency versions
├── src/
│   └── churn_prediction/
│       ├── data/           # Data loading & validation
│       ├── features/       # Feature engineering
│       ├── models/         # Model training & inference
│       └── evaluation/     # Metrics & evaluation
├── scripts/
│   └── train.py           # Training pipeline
├── tests/
│   ├── unit/              # Unit tests
│   └── integration/       # Integration tests
├── data/
│   ├── raw/               # Original data
│   └── processed/         # Transformed data
└── notebooks/             # Exploratory analysis
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- UV package manager ([install instructions](https://github.com/astral-sh/uv))

### Setup Environment
```bash
# Clone repository
git clone <your-repo-url>
cd customer-churn-prediction

# Install production dependencies only
uv sync --no-dev

# OR install with development tools
uv sync --group dev --group test

# OR install everything (including notebooks)
uv sync --all-groups
```

### Train Model
```bash
# Run training pipeline
uv run python scripts/train.py

# Expected output:
# - Synthetic data created
# - Model trained
# - Evaluation metrics printed
# - Model saved to models/random_forest_model.joblib
```

### Run Tests
```bash
# Install test dependencies
uv sync --group test

# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ --cov=src/churn_prediction --cov-report=term-missing
```

## 📦 Dependency Management

### Production Dependencies
```bash
# Install production packages only (deployment)
uv sync --no-dev
```

Includes: numpy, pandas, scikit-learn, joblib

### Development Dependencies
```bash
# Install dev tools (linting, formatting)
uv sync --group dev
```

Includes: black, flake8, mypy, ipython

### Testing Dependencies
```bash
# Install test tools
uv sync --group test
```

Includes: pytest, pytest-cov, pytest-mock

### Notebooks Dependencies
```bash
# Install Jupyter and visualization
uv sync --group notebooks
```

Includes: jupyter, matplotlib, seaborn, plotly

### Adding New Dependencies
```bash
# Add production dependency
uv add <package-name>

# Add dev dependency
uv add --group dev <package-name>

# Lock dependencies
uv lock

# Commit both files
git add pyproject.toml uv.lock
git commit -m "Add <package-name>"
```

## 🧪 Testing
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/unit/test_data_loader.py

# Run with coverage
uv run pytest --cov=src/churn_prediction

# Run with verbose output
uv run pytest -v
```

## 🔍 Code Quality
```bash
# Format code with black
uv run black src/ tests/

# Lint with flake8
uv run flake8 src/ tests/

# Type check with mypy
uv run mypy src/
```

## 📊 Model Performance

Current model (Random Forest):
- Accuracy: ~0.85
- Precision: ~0.82
- Recall: ~0.78
- F1 Score: ~0.80
- ROC AUC: ~0.88

## 🔄 Reproducibility

This project ensures bit-for-bit reproducibility:

1. **Exact Python version**: Specified in `.python-version`
2. **Locked dependencies**: All versions in `uv.lock` with SHA256 hashes
3. **Deterministic training**: Fixed random seeds
4. **Version control**: Git tracks code, DVC tracks data (future)

### Reproduce Environment
```bash
# On any machine:
git clone <repo>
cd customer-churn-prediction
uv sync  # Installs EXACT versions from uv.lock

# Verify
uv run python scripts/train.py
# Should produce identical results
```

## 📝 Development Workflow
```bash
# 1. Create feature branch
git checkout -b feature-name

# 2. Make changes, add dependencies if needed
uv add new-package

# 3. Run tests
uv run pytest

# 4. Format and lint
uv run black src/ tests/
uv run flake8 src/ tests/

# 5. Commit (both pyproject.toml and uv.lock)
git add pyproject.toml uv.lock src/ tests/
git commit -m "Descriptive message"

# 6. Push
git push origin feature-name
```

## 🎯 Future Enhancements

- [ ] Data version control (DVC)
- [ ] Model registry (MLflow)
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Containerization (Docker)
- [ ] API serving (FastAPI)
- [ ] Monitoring (Prometheus + Grafana)

## 📄 License

MIT

## 👤 Author

Muhammad Dawood Khan - [dawood.ml@outlook.com](mailto:dawood.ml@outlook.com)

---

**Note**: This project demonstrates MLOps best practices for environment management and reproducibility. It's designed as a portfolio piece and learning resource.
