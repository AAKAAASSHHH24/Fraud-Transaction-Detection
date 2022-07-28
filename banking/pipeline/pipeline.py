from banking.config.configuration import Configuartion
from banking.logger import logging
from banking.exception import BankingException

from banking.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact,DataTransformationArtifact
from banking.entity.config_entity import DataIngestionConfig
from banking.components.data_ingestion import DataIngestion
from banking.components.data_validation import DataValidation
from banking.components.data_transformation import DataTransformation
import os,sys

class Pipeline:

    def __init__(self,config: Configuartion = Configuartion()) -> None:
        try:
            self.config=config


        except Exception as e:
            raise BankingException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise BankingException(e,sys) from e    


    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact) \
        -> DataValidationArtifact :
        try:
            data_validation =  DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                              data_ingestion_artifact=data_ingestion_artifact
            )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise BankingException(e,sys) from e

    def start_data_transformation(self,
                                data_ingestion_artifact:DataIngestionArtifact,
                                data_validation_artifact: DataValidationArtifact
                                )->DataTransformationArtifact:
        try:
            data_transformation = DataTransformation(
                data_transformation_config=self.config.get_data_transformation_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
            )
            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise BankingException(e,sys)

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass

    def run_pipeline(self):
        try:
            #running pipeline
            
            
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion_artifact = self.start_data_ingestion()
            
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact,)
            
            data_transformation_artifact = self.start_data_transformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact
                
            )


        except Exception as e:
            raise BankingException(e,sys) from e