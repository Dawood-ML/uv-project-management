import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from churn_prediction.models.predict import predict_safe
from sklearn.ensemble import RandomForestClassifier

def test_predict_safe_raises_on_nan():
    """Test that predict_safe raises error on NaN input."""
    # Create dummy model
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    X_train = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    y_train = [0, 1, 0]
    model.fit(X_train, y_train)
    
    # Create input with NaN
    X_test = pd.DataFrame({'a': [1, np.nan], 'b': [4, 5]})
    
    # Should raise ValueError
    with pytest.raises(ValueError, match="NaN values"):
        predict_safe(model, X_test)


def test_predict_safe_raises_on_inf():
    """Test that predict_safe raises error on Inf input."""
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    X_train = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    y_train = [0, 1, 0]
    model.fit(X_train, y_train)
    
    # Create input with Inf
    X_test = pd.DataFrame({'a': [1, np.inf], 'b': [4, 5]})
    
    # Should raise ValueError
    with pytest.raises(ValueError, match="Inf values"):
        predict_safe(model, X_test)


def test_predict_safe_works_on_valid_input():
    """Test that predict_safe works with valid input."""
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    X_train = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    y_train = [0, 1, 0]
    model.fit(X_train, y_train)
    
    # Valid input
    X_test = pd.DataFrame({'a': [1, 2], 'b': [4, 5]})
    
    # Should work without error
    predictions = predict_safe(model, X_test)
    
    assert len(predictions) == 2
    assert predictions.dtype in [np.int64, np.int32]