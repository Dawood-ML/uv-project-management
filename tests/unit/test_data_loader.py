"""
Unit tests for data loading module.

WHAT: Test data loading functions
WHY: Ensure data pipeline works correctly
WHEN: CI/CD, before commits
WHEN NOT: Never skip tests
ALTERNATIVE: Manual testing (not scalable)
"""

import pytest
import pandas as pd
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from churn_prediction.data.loader import split_data


def test_split_data():
    """
    Test train/test split functionality.
    
    WHAT: Verify split produces correct sizes
    WHY: Catch bugs in splitting logic
    WHEN: Every test run
    WHEN NOT: N/A
    ALTERNATIVE: None - testing is mandatory
    """
    # Create sample data
    df = pd.DataFrame({
        "feature1": range(100),
        "feature2": range(100, 200),
        "Churn": [0, 1] * 50
    })
    
    # Split data
    X_train, X_test, y_train, y_test = split_data(df, test_size=0.2)
    
    # Assertions
    assert len(X_train) == 80
    assert len(X_test) == 20
    assert len(y_train) == 80
    assert len(y_test) == 20
    
    # Check stratification
    train_churn_rate = y_train.mean()
    test_churn_rate = y_test.mean()
    assert abs(train_churn_rate - 0.5) < 0.1
    assert abs(test_churn_rate - 0.5) < 0.1


def test_split_data_reproducibility():
    """
    Test that split is reproducible with same random_state.
    
    WHAT: Verify deterministic splitting
    WHY: Reproducibility is critical for ML
    WHEN: Every test run
    WHEN NOT: N/A
    ALTERNATIVE: None
    """
    df = pd.DataFrame({
        "feature1": range(100),
        "Churn": [0, 1] * 50
    })
    
    # Split twice with same seed
    X_train1, _, _, _ = split_data(df, random_state=42)
    X_train2, _, _, _ = split_data(df, random_state=42)
    
    # Should be identical
    pd.testing.assert_frame_equal(X_train1, X_train2)