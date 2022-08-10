import pandas as pd
import numpy as np
import pandera as pd

def validate_df(df:pd.DataFrame=None, schema:pd.Schema=None)->pd.DataFrame:
    """
    Validate a pandas dataframe against a pandas schema
    Args:
      df (pd.DataFrame): The dataframe you want to validate.
      schema (pd.Schema): The schema you want to validate against.
    Returns:
      (pd.DataFrame) A validated dataframe.
    """
    return df.validate(schema)