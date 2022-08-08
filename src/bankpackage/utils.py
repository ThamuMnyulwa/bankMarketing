
import numpy as np
import pandas as pd

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
    """cre
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


# standard in python


if __name__ == "__main__":
    logger.info("This is a module")
