import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from churn_prediction.features.engineering import FeatureEngineer


def test_feature_engineer_fit_transform():
    """Test feature engineering fit_transform."""
    df = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [10, 20, 30, 40, 50],
    })
    
    engineer = FeatureEngineer()
    df_transformed = engineer.fit_transform(df)
    
    # Check scaling (mean ~ 0, std ~ 1)
    assert abs(df_transformed["feature1"].mean()) < 0.01
    assert abs(df_transformed["feature1"].std() - 1.0) < 0.01


def test_feature_engineer_must_fit_before_transform():
    """Test that transform() fails if not fitted."""
    df = pd.DataFrame({"feature1": [1, 2, 3]})
    
    engineer = FeatureEngineer()
    
    with pytest.raises(ValueError, match="Must call fit_transform"):
        engineer.transform(df)