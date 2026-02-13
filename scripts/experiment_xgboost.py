#!/usr/bin/env python3
"""
XGBoost experiment for churn prediction.

WHAT: Compare XGBoost vs Random Forest
WHY: Potentially better performance
WHEN: Model development phase
WHEN NOT: Production deployment (needs validation)
ALTERNATIVE: Stick with Random Forest (less risk)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import xgboost as xgb
from churn_prediction.data.loader import load_data, split_data
from churn_prediction.features.engineering import FeatureEngineer
from churn_prediction.evaluation.metrics import evaluate_model, print_metrics


def main():
    """Run XGBoost experiment."""
    print("\n" + "="*60)
    print("EXPERIMENT: XGBoost vs Random Forest")
    print("="*60 + "\n")
    
    # Load data
    DATA_PATH = "data/raw/customers.csv"
    df = load_data(DATA_PATH)
    
    # Split and engineer features
    X_train, X_test, y_train, y_test = split_data(df)
    engineer = FeatureEngineer()
    X_train_transformed = engineer.fit_transform(X_train)
    X_test_transformed = engineer.transform(X_test)
    
    # Train XGBoost
    print("Training XGBoost...")
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        random_state=42
    )
    model.fit(X_train_transformed, y_train)
    
    # Evaluate
    metrics = evaluate_model(model, X_test_transformed, y_test)
    print_metrics(metrics)
    
    # DECISION CRITERIA:
    # If ROC AUC > 0.90 → Merge to main
    # If ROC AUC 0.88-0.90 → Consider merging
    # If ROC AUC < 0.88 → Discard experiment
    
    roc_auc = metrics['roc_auc']
    print(f"\nDecision: ROC AUC = {roc_auc:.4f}")
    
    if roc_auc > 0.90:
        print("✅ MERGE TO MAIN - Significant improvement")
    elif roc_auc > 0.88:
        print("⚠️  REVIEW - Marginal improvement, needs discussion")
    else:
        print("❌ DISCARD - No improvement over baseline")


if __name__ == "__main__":
    main()
