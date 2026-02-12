"""
Model training pipeline.

WHAT: Train ML models for churn prediction
WHY: Centralized training logic
WHEN: Developing and deploying models
WHEN NOT: Inference only
ALTERNATIVE: Notebook training (not reproducible)
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import joblib
from pathlib import Path
from typing import Any, Dict


def train_model(
    X_train,
    y_train,
    model_type: str = "random_forest",
    **model_params
) -> Any:
    """
    Train classification model.
    
    WHAT: Fit scikit-learn model on training data
    WHY: Encapsulate training logic
    WHEN: Model development, retraining
    WHEN NOT: Inference only
    ALTERNATIVE: Manual model.fit() (less reusable)
    
    Args:
        X_train: Training features
        y_train: Training labels
        model_type: Type of model to train
        **model_params: Model hyperparameters
        
    Returns:
        Trained model
    """
    if model_type == "random_forest":
        # WHAT: Random Forest classifier
        # WHY: Good baseline, handles non-linear patterns
        # WHEN: First model to try
        # WHEN NOT: Need probabilistic predictions (use LogisticRegression)
        # ALTERNATIVE: XGBoost, LightGBM (better but more complex)
        model = RandomForestClassifier(
            n_estimators=model_params.get("n_estimators", 100),
            max_depth=model_params.get("max_depth", 10),
            random_state=model_params.get("random_state", 42),
            n_jobs=-1  # Use all CPU cores
        )
    elif model_type == "logistic_regression":
        # WHAT: Logistic Regression
        # WHY: Interpretable, fast, good for linear patterns
        # WHEN: Need interpretability
        # WHEN NOT: Complex non-linear patterns
        # ALTERNATIVE: Random Forest (less interpretable)
        model = LogisticRegression(
            random_state=model_params.get("random_state", 42),
            max_iter=1000
        )
    else:
        raise ValueError(f"Unknown model type: {model_type}")
    
    print(f"Training {model_type}...")
    model.fit(X_train, y_train)
    print("Training complete!")
    
    return model


def save_model(model: Any, model_path: str) -> None:
    """
    Save trained model to disk.
    
    WHAT: Serialize model with joblib
    WHY: Persist model for later use
    WHEN: After training
    WHEN NOT: Throwaway experiments
    ALTERNATIVE: pickle (joblib better for numpy arrays)
    
    Args:
        model: Trained scikit-learn model
        model_path: Path to save model
    """
    path = Path(model_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    joblib.dump(model, path)
    print(f"Model saved to {path}")


def load_model(model_path: str) -> Any:
    """
    Load trained model from disk.
    
    WHAT: Deserialize model with joblib
    WHY: Use previously trained model
    WHEN: Inference, evaluation
    WHEN NOT: Training from scratch
    ALTERNATIVE: Retrain every time (wasteful)
    
    Args:
        model_path: Path to saved model
        
    Returns:
        Loaded model
    """
    path = Path(model_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Model not found: {model_path}")
    
    model = joblib.load(path)
    print(f"Model loaded from {path}")
    
    return model