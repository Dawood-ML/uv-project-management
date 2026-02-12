#!/usr/bin/env python3
"""
Training script for churn prediction model.

WHAT: End-to-end training pipeline
WHY: Reproducible model training
WHEN: Developing new models, retraining
WHEN NOT: Inference only
ALTERNATIVE: Jupyter notebook (not production-ready)

Usage:
    python scripts/train.py
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from churn_prediction.data.loader import load_data, split_data
from churn_prediction.features.engineering import FeatureEngineer
from churn_prediction.models.train import train_model, save_model
from churn_prediction.evaluation.metrics import evaluate_model, print_metrics


def main():
    """
    Main training pipeline.
    
    WHAT: Orchestrate data loading → feature engineering → training → evaluation
    WHY: Single entry point for training
    WHEN: Model development, retraining
    WHEN NOT: N/A
    ALTERNATIVE: Scattered scripts (hard to maintain)
    """
    print("\n" + "="*60)
    print("CUSTOMER CHURN PREDICTION - TRAINING PIPELINE")
    print("="*60 + "\n")
    
    # Configuration
    # WHAT: Hardcoded config for simplicity
    # WHY: Works for small projects
    # WHEN: Prototyping
    # WHEN NOT: Production (use config files - Chunk later)
    # ALTERNATIVE: YAML config, command-line args
    DATA_PATH = "data/raw/customers.csv"
    MODEL_PATH = "models/random_forest_model.joblib"
    MODEL_TYPE = "random_forest"
    
    # For this demo, we'll create synthetic data
    # In real project, data would be in data/raw/
    print("Step 1: Creating synthetic data for demo...")
    create_synthetic_data(DATA_PATH)
    
    # Load data
    print("\nStep 2: Loading data...")
    df = load_data(DATA_PATH)
    
    # Split data
    print("\nStep 3: Splitting data...")
    X_train, X_test, y_train, y_test = split_data(df)
    
    # Feature engineering
    print("\nStep 4: Engineering features...")
    engineer = FeatureEngineer()
    X_train_transformed = engineer.fit_transform(X_train)
    X_test_transformed = engineer.transform(X_test)
    
    # Train model
    print("\nStep 5: Training model...")
    model = train_model(
        X_train_transformed,
        y_train,
        model_type=MODEL_TYPE,
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    
    # Evaluate model
    print("\nStep 6: Evaluating model...")
    metrics = evaluate_model(model, X_test_transformed, y_test)
    print_metrics(metrics)
    
    # Save model
    print("\nStep 7: Saving model...")
    save_model(model, MODEL_PATH)
    
    print("\n" + "="*60)
    print("TRAINING COMPLETE!")
    print("="*60 + "\n")


def create_synthetic_data(output_path: str) -> None:
    """
    Create synthetic customer data for demo.
    
    WHAT: Generate fake customer data
    WHY: Demo without real data
    WHEN: Testing, demos
    WHEN NOT: Production (use real data)
    ALTERNATIVE: Use public datasets
    """
    import pandas as pd
    import numpy as np
    
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        "CustomerID": range(1, n_samples + 1),
        "Age": np.random.randint(18, 70, n_samples),
        "Tenure": np.random.randint(0, 120, n_samples),
        "MonthlyCharges": np.random.uniform(20, 120, n_samples),
        "TotalCharges": np.random.uniform(100, 8000, n_samples),
        "NumProducts": np.random.randint(1, 5, n_samples),
        "Churn": np.random.binomial(1, 0.3, n_samples),  # 30% churn rate
    }
    
    df = pd.DataFrame(data)
    
    # Create directory if needed
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"Created synthetic data: {output_path}")


if __name__ == "__main__":
   main()