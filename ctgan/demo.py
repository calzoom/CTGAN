import pandas as pd

DEMO_URL = 'http://ctgan-data.s3.amazonaws.com/census.csv.gz'


def load_demo():
    return pd.read_csv('../elec_cleaned.csv')
