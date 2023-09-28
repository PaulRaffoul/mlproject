import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass #decorator that creates init functions to classes
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts','train.csv') #path to store training data
    test_data_path : str=os.path.join('artifacts','test.csv') #path to store test data
    raw_data_path : str=os.path.join('artifacts','data.csv') #path to store raw data
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #get the paths 

    def initiate_data_ingestion(self):
        logging.info('enter the data ingestion method or component')
        try:
            df=pd.read_csv('data\StudentsPerformance.csv') #read data
            logging.info('Read the dataset as dataframe')

            #create the train data folder
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) #saving raw data to path

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )


        except Exception as e:
            raise CustomException(e,sys)

if __name__=='__main__':
    
    obj=DataIngestion()
    obj.initiate_data_ingestion()





