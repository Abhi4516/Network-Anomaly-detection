from Networksecurity.components.data_ingestion import DataIngestion
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.logging.logger import logging
from Networksecurity.entity.config_entity import DataIngestionConfig
from Networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataengestionconfg=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataengestionconfg)
        logging.info("intitate the data ingestiob")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
           raise NetworkSecurityException(e,sys)
    