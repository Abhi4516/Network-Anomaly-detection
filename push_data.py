import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging

class NetworkDataExtract():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_convertor(self, file_paths):
        try:
            all_records = []
            for file_path in file_paths:
              data=pd.read_csv(file_path)
              data.reset_index(drop=True, inplace=True)
              records = list(json.loads(data.T.to_json()).values())
              all_records.extend(records)
            return all_records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
   


    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL) 
            self.database=self.mongo_client[self.collection]

            self.collection=self.database[self.collection]  
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)    
        
if __name__ == '__main__':
    FILE_PATH = [os.path.join("Network_Data", f"file{i}.csv") for i in range(0,1)]
    DATABASE = 'ABHI'
    Collection = "Network_Data"
    
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_convertor(file_paths=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records=records, database=DATABASE, collection=Collection)
    
    print(no_of_records)
