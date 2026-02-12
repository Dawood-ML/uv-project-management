import pandas as pd
from pathlib import Path
from typing import Tuple


def load_data(data_path: str) -> pd.DataFrame:
    """
    Loads customer data from csv
    """

    path = Path(data_path)

    if not path.exists():
        raise FileNotFoundError(f"Data not found in {path}")
    
    df = pd.read_csv(path)
    print(f"Loaded ( {len(df)} ) records from Path : {data_path}")

    return df

def split_data(df:pd.DataFrame, 
               target_col:str = 'Churn', 
               test_size:float = 0.2, 
               ranom_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    X, y = df.drop(columns=[target_col], axis=1), df[target_col]
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=test_size, random_state=ranom_state,
                                                         stratify = y)
    
    print(f"Train: {len(X_train)} | Test: {len(X_test)}")
    print(f"Train churn rate: {y_train.mean():.2%}")
    print(f"Test churn rate: {y_test.mean():.2%}")
    
    return X_train, X_test, y_train, y_test



