# Intentionally messy file to test pre-commit hooks

import os
import sys
import pandas as pd
from sklearn.metrics import accuracy_score

def bad_function(x,y,z):
    print("This is a debug print statement")  # Hook should flag this
    result=x+y+z  # No spaces around =
    return result


def another_function(  ):   # Extra spaces
    x=1+2+3+4+5  # No spaces
    return x   


# Trailing whitespace on next line:    
