
import numpy as np
import pandas as pd
import dateparser as date_parser
from loguru import logger
from pandas.errors import ParserError
from collections import Counter
from datetime import datetime
from loguru import logger

# python src/bankpackage/utils.py to test the function

# load dataset from github url
def load_dataset(url:str=None)->pd.DataFrame:
    """
    Load dataset from github url endpoint
    Args:
      (str) url: the url endpoint to the dataset
    Returns:
      (dataframe) data: A pandas dataframe
    """
    with open(url) as f: # use with to import the data 
        data = pd.read_csv(f)
    return data

def df_maker(df:pd.DataFrame=None):
    """
    It takes a pandas dataframe and prints out a dictionary of the dataframe's columns and values
    
    Args:
      df (pd.DataFrame): The dataframe you want to convert to a dictionary
    """
    d = df.to_dict()
    print('{')
    cnt = 0
    for i in d:
        if cnt != len(d):
            print(f"'{i}'" ,":", list(d[i].values()),',')
        if cnt == len(d)-1:
            print(f"'{i}'" ,":", list(d[i].values()))
        cnt += 1
    print('}')

def parse_date(date_or_string):
    """
    If the input is a date, return it; if it's a string, try to parse it as a date
    Args:
      date_or_string: The date to parse.
    Returns:
      (datetime.datetime) A date object
    """
    if isinstance(date_or_string, pd.Timestamp):
        return date_or_string.to_pydatetime().date()
    if isinstance(date_or_string, datetime):
        return date_or_string.date()
    if isinstance(date_or_string, date):
        return date_or_string
    try:
        return datetime.strptime(date_or_string, "%b-%y").date()
    except ValueError:
        pass
    try:
        return datetime.strptime(date_or_string, "_%b-%y").date()
    except ValueError:
        return date_parser.parse(date_or_string).date()
    
def date_columns_identifier(df):
    """Automatically detect each dataframe column which can be seen as a datetime just 
    when it is successfully parsed by df_utils.parse_date().
    Args:
        (dataframe) df: 
    Returns:
        (list) columns_date: list of datetime columns
        (list) columns_date_as_datetime: list of date columns as datetime
        (list) columns_not_date: list of not datetime columns
    """
    columns_date,columns_date_as_datetime, columns_not_date = [], [], [] # container for columns
    for c in df.columns: #don't convert non datetime column names
        try: 
            columns_date_as_datetime.append(parse_date(c)) # keep both original form and datetime
            columns_date.append(c)
        except (ParserError,ValueError,TypeError): #Can't convert some
            columns_not_date.append(c)
    return columns_date,columns_date_as_datetime, columns_not_date

# standard in python


if __name__ == "__main__":
    logger.info("This is a module")
