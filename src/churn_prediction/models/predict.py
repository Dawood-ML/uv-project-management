"""
Prediction utilities with input validation.

WHAT: Safe prediction with NaN handling
WHY: Prevent NaN predictions in production
WHEN: Inference time
WHEN NOT: N/A
ALTERNATIVE: Allow NaNs (causes production failures)
"""

import numpy as np
import pandas as pd
from typing import Any


def predict_safe(model: Any, X: pd.DataFrame) -> np.ndarray:
    """
    Make predictions with input validation.
    
    WHAT: Validate inputs before prediction
    WHY: Catch NaNs before they cause issues
    WHEN: Production inference
    WHEN NOT: Training (NaNs handled in preprocessing)
    ALTERNATIVE: model.predict() directly (risky)
    
    Args:
        model: Trained model
        X: Input features
        
    Returns:
        Predictions
        
    Raises:
        ValueError: If input contains NaN or Inf
    """
    # WHAT: Check for NaN values
    # WHY: NaN → NaN predictions
    # WHEN: Before every prediction
    # WHEN NOT: Never skip validation
    # ALTERNATIVE: Fill NaN (changes data unexpectedly)
    
    if X.isnull().any().any():
        raise ValueError(
            f"Input contains NaN values in columns: "
            f"{X.columns[X.isnull().any()].tolist()}"
        )
    
    # WHAT: Check for Inf values
    # WHY: Inf → unstable predictions
    # WHEN: Before every prediction
    # WHEN NOT: Never skip validation
    # ALTERNATIVE: Clip Inf (silent data modification)
    
    if np.isinf(X.select_dtypes(include=[np.number])).any().any():
        raise ValueError("Input contains Inf values")
    
    # WHAT: Make prediction
    # WHY: Inputs validated, safe to predict
    # WHEN: After validation passes
    # WHEN NOT: If validation fails
    # ALTERNATIVE: None
    
    predictions = model.predict(X)
    
    return predictions
