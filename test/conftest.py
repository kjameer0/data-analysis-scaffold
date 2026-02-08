import pytest
import pandas as pd

# Remove 
@pytest.fixture(scope="session")
def trees_df():
    """
    Load the trees dataset once per test session.
    """
    df = pd.read_csv("data-files/trees.csv", nrows=1000)
    return df
