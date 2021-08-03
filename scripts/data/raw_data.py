'''
Module for loading data from source. If run as 
script (__main__) will re-download and save 
data to raw data folder. 

Has functions to grab data and save to our 
raw data folder.

Has an (hidden) implicit pandas dependency in the scikit-learn (sklearn)
funcitno call load_iris() because of the as_frame = True. 
'''
import pandas as pd 
import sklearn
import sklearn.datasets
import time 
import random 

dataFolder = "/home/jovyan/data/"
rawFolder = dataFolder + "raw/"
rawDataFile = rawFolder + 'iris_data.csv'

def importData() -> pd.DataFrame:
    ''' Grab data from "remote" source. Returns a pandas DataFrame.'''
    ##simulate some wait time for grabbing the api data or database call
    time.sleep(random.randrange(10,60))
    
    data = sklearn.datasets.load_iris(as_frame=True)
    df = data['frame']
    df['target_names'] = df['target'].apply(lambda i:data['target_names'][i])
    return df

def _dumpData(df):
    ''' Save raw data to raw data folder. '''
    df.to_csv(rawDataFile, index=False)

def saveData():
    ''' Parse/grab data from data source and save to disk in raw data folder. '''
    df = importData()
    _dumpData(df)

def getRaw() -> pd.DataFrame:
    ''' Load data from stored raw folder. Returns a pandas DataFrame.'''
    return pd.read_csv(rawDataFile)

if __name__ == "__main__":
    print("Loading data from data source...")
    saveData()
    print(f"Data saved to {rawFolder}")
    df_check = getRaw()
    print("Sample head of data:")
    print()
    print(df_check.head())
