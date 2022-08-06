
import numpy as np
import pandas as pd

from loguru import logger


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


# standard in python

if __name__ == "__main__":
    logger.info("This is a module")
    