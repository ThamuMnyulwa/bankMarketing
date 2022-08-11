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

def ingress_schema(df: pd.DataFrame = None) -> pd.DataFrame:
  """
  To validate aganist a schema and return dataframe with only the rows that meet the schema requirements.
  Args:
    df (pd.DataFrame): pd.DataFrame = None
  Returns:
    A dataframe with the same columns as the original dataframe, but with the rows that do not meet the schema requirements removed.
  """
  # Create an ingress schema for the initial dataframe
  prepared_schema = pa.DataFrameSchema(
                      columns={
                          'age': pa.Column(int,coerce=True,nullable=True,checks=pa.Check(lambda s: s >= 0, element_wise=False)),
                          'job': pa.Column(object, coerce=True, nullable=False),
                          'marital': pa.Column(object, coerce=True, nullable=False),
                          'education': pa.Column(object, coerce=True, nullable=False),
                          'default': pa.Column(object, coerce=True, nullable=False),
                          'housing': pa.Column(object, coerce=True, nullable=False),
                          'loan': pa.Column(object, coerce=True, nullable=False),
                          'contact': pa.Column(object, coerce=True, nullable=False),
                          'month': pa.Column(object, coerce=True, nullable=False),
                          'day_of_week': pa.Column(object, coerce=True, nullable=False),
                          'duration': pa.Column(int,coerce=True,nullable=True,checks=pa.Check(lambda s: s >= 0, element_wise=False)),
                          'campaign': pa.Column(int,coerce=True,nullable=True,checks=pa.Check(lambda s: s >= 0, element_wise=False)),
                          'pdays': pa.Column(int,coerce=True,nullable=True),
                          'previous': pa.Column(int,coerce=True,nullable=True),
                          'poutcome':  pa.Column(object, coerce=True, nullable=False),
                          'emp.var.rate': pa.Column(float,coerce=True,nullable=True),
                          'cons.price.idx': pa.Column(float,coerce=True,nullable=True),
                          'cons.conf.idx': pa.Column(float,coerce=True,nullable=True),
                          'euribor3m': pa.Column(float,coerce=True,nullable=True),
                          'nr.employed': pa.Column(float,coerce=True,nullable=True),
                          'y':  pa.Column(object, coerce=True, nullable=False),
                      },
                      checks=[],
                      name=None,
                      ordered=False,
                      unique_column_names=False
                  )
  # catch errors and return all data where conditions are met
  fail_index = []
  try:
      prepared_schema.validate(df, lazy=True)
  except pa.errors.SchemaErrors as ex:
      fail_index = ex.failure_cases["index"]
  clean_df = df[~df.index.isin(fail_index)]
  logger.success("Done: Validated ingress schema for in_sample data (target present).")
  return clean_df