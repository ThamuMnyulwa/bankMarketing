import pandas as pd
import numpy as np
import requests
import io
from loguru import logger
from bankpackage import utils, validation


def import_from_url_no_credentials_necessary(link):
    """
    Import data from url endpoint without credentials necessary
    """
    try:
        response = requests.get(link)
        if response.status_code == 200:
            return pd.read_csv(io.StringIO(response.content.decode("utf-8")), sep=";")
        else:
            logger.error(f"Error: {response.status_code}")
    except Exception as e:
        logger.error(f"Error: {e}")


def run():
    """
    Run the script
    """
    logger.info("Start featurestore.py")

    # import and validate data from url endpoint
    link = "https://raw.githubusercontent.com/ThamuMnyulwa/bankMarketing/main/data/bank-additional-full.csv"
    df = import_from_url_no_credentials_necessary(link).pipe(validation.ingress_schema)

    logger.info("End featurestore.py")
