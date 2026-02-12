"""
Feature engineering for churn prediction.

WHAT: Transform raw data into ML-ready features
WHY: Better features = better models
WHEN: After data loading, before training
WHEN NOT: Never skip feature engineering
ALTERNATIVE: Use raw data (suboptimal performance)
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Tuple


class FeatureEngineer:
    """
    Feature engineering pipeline.
    
    WHAT: Reusable feature transformation pipeline
    WHY: Same transformations for train/test/inference
    WHEN: Training and inference
    WHEN NOT: Never transform features inconsistently
    ALTERNATIVE: Ad-hoc transformations (causes train/test skew)
    """
    
    def __init__(self):
        """
        Initialize feature engineer.
        
        WHAT: Setup internal state
        WHY: Store fitted transformers for inference
        WHEN: Creating new pipeline
        WHEN NOT: N/A
        ALTERNATIVE: Stateless functions (can't remember training stats)
        """
        self.scaler = StandardScaler()
        self.fitted = False
    
    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fit transformers on training data and transform.
        
        WHAT: Learn statistics from data, then transform
        WHY: Prevent data leakage (don't use test stats)
        WHEN: Training data only
        WHEN NOT: Test/inference data (use transform() instead)
        ALTERNATIVE: Transform without fitting (uses wrong statistics)
        
        Args:
            df: Training DataFrame
            
        Returns:
            Transformed DataFrame
        """
        df_transformed = df.copy()
        
        # WHAT: Select numeric columns for scaling
        # WHY: Standardization helps gradient-based models
        # WHEN: Features on different scales
        # WHEN NOT: Tree-based models (scale-invariant)
        # ALTERNATIVE: MinMaxScaler, RobustScaler
        numeric_cols = df_transformed.select_dtypes(include=[np.number]).columns.tolist()
        
        # Fit and transform
        df_transformed[numeric_cols] = self.scaler.fit_transform(df_transformed[numeric_cols])
        
        self.fitted = True
        print(f"Fitted on {len(numeric_cols)} numeric features")
        
        return df_transformed
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform using fitted parameters.
        
        WHAT: Apply learned transformations
        WHY: Consistent preprocessing for inference
        WHEN: Test data, inference
        WHEN NOT: Training data (use fit_transform)
        ALTERNATIVE: Refit on test data (data leakage!)
        
        Args:
            df: DataFrame to transform
            
        Returns:
            Transformed DataFrame
        """
        if not self.fitted:
            raise ValueError("Must call fit_transform() before transform()")
        
        df_transformed = df.copy()
        numeric_cols = df_transformed.select_dtypes(include=[np.number]).columns.tolist()
        
        df_transformed[numeric_cols] = self.scaler.transform(df_transformed[numeric_cols])
        
        return df_transformed