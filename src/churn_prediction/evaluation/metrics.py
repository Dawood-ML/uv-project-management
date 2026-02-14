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

def calculate_business_metrics(y_true, y_pred, y_pred_proba):
    """
    Calculate business-focused metrics for churn prediction.
    
    WHAT: Metrics that translate to business value
    WHY: Accuracy alone doesn't show ROI
    WHEN: Presenting to stakeholders
    WHEN NOT: Technical evaluation (use evaluate_model)
    ALTERNATIVE: Just show accuracy (stakeholders don't care)
    
    Args:
        y_true: Actual churn labels
        y_pred: Predicted churn labels
        y_pred_proba: Predicted churn probabilities
        
    Returns:
        Dictionary with business metrics
    """
    from sklearn.metrics import confusion_matrix
    import numpy as np
    
    # Confusion matrix
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    
    # Business metrics (example values)
    revenue_per_customer = 1000  # $1000 average annual revenue
    retention_cost = 100  # $100 cost to retain customer
    
    # True Positives: Correctly identified churners we can save
    saved_customers = tp
    saved_revenue = saved_customers * (revenue_per_customer - retention_cost)
    
    # False Positives: Wasted retention efforts
    wasted_retention = fp * retention_cost
    
    # False Negatives: Lost customers we didn't identify
    lost_revenue = fn * revenue_per_customer
    
    # ROI calculation
    total_cost = (tp + fp) * retention_cost
    total_benefit = saved_revenue
    roi = (total_benefit - total_cost) / total_cost if total_cost > 0 else 0
    
    return {
        'saved_customers': int(saved_customers),
        'saved_revenue': float(saved_revenue),
        'wasted_retention': float(wasted_retention),
        'lost_revenue': float(lost_revenue),
        'roi': float(roi),
        'net_benefit': float(saved_revenue - wasted_retention - lost_revenue)
    }
