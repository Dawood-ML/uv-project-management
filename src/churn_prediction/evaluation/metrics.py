"""
Model evaluation metrics.

WHAT: Calculate performance metrics
WHY: Assess model quality
WHEN: After training, before deployment
WHEN NOT: Never skip evaluation
ALTERNATIVE: Ad-hoc evaluation (inconsistent)
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)
from typing import Dict, Any
import numpy as np


def evaluate_model(model: Any, X_test, y_test) -> Dict[str, float]:
    """
    Calculate classification metrics.
    
    WHAT: Comprehensive model evaluation
    WHY: Multiple metrics capture different aspects
    WHEN: After training, on test set
    WHEN NOT: On training set (overfitting check separate)
    ALTERNATIVE: Single metric (incomplete picture)
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels
        
    Returns:
        Dictionary of metrics
    """
    # WHAT: Generate predictions
    # WHY: Compare against ground truth
    # WHEN: Evaluation
    # WHEN NOT: Training
    # ALTERNATIVE: None
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # WHAT: Calculate metrics
    # WHY: Different metrics for different business needs
    # WHEN: Always calculate multiple metrics
    # WHEN NOT: Never rely on single metric
    # ALTERNATIVE: Custom business metrics
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_pred_proba),
    }
    
    # WHAT: Confusion matrix
    # WHY: See actual vs predicted breakdown
    # WHEN: Understanding model errors
    # WHEN NOT: Quick checks (too detailed)
    # ALTERNATIVE: Classification report
    cm = confusion_matrix(y_test, y_pred)
    metrics["confusion_matrix"] = cm.tolist()
    
    return metrics


def print_metrics(metrics: Dict[str, float]) -> None:
    """
    Print metrics in readable format.
    
    WHAT: Display evaluation results
    WHY: Human-readable output
    WHEN: After evaluation
    WHEN NOT: Automated pipelines (log instead)
    ALTERNATIVE: Structured logging
    """
    print("\n" + "="*50)
    print("MODEL EVALUATION RESULTS")
    print("="*50)
    
    for metric, value in metrics.items():
        if metric == "confusion_matrix":
            print(f"\n{metric}:")
            print(np.array(value))
        else:
            print(f"{metric:>15s}: {value:.4f}")
    
    print("="*50 + "\n")