from collections import namedtuple

#DEFINING THE INPUTS OF THE DIFFERENT COMPONENTS


DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","raw_data_dir","ingested_train_dir","ingested_test_dir"])
"""Brings data into system"""


DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])
"""Schema Validation means checking file name,no: of columns the file has and the structure of data
Null Check,duplicate values, imbalance datasets, data drift(statistics of the datasets), domain value
check i.e. possible values for a column or data range"""


DataTransformationConfig = namedtuple("DataTransformationConfig", ["is_fraud",
                                                                   "transformed_train_dir",
                                                                   "transformed_test_dir",
                                                                   "preprocessed_object_file_path"])
"""EDA and feature engineering"""


ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path","base_accuracy"])
"""model selection,hyper-parameter tuning"""


ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])
"""compare performance of the pre-existing model and test model with the testing dataset"""


ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])