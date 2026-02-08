from main import count_boroughs
import pandas as pd

def test_count_boroughs(trees_df):
  assert count_boroughs(trees_df) == 5
