from ChickenDiseaseClassification import logger
import os
from ChickenDiseaseClassification.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from ChickenDiseaseClassification.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from ChickenDiseaseClassification.pipeline.stage03_base_model import PrepareBaseModelTrainingPipeline
from ChickenDiseaseClassification.pipeline.stage04_callback import CallbackPipeline




# ------------------------------------------ Data_Ingestion ------------------------------------ 


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




# ------------------------------------------ Data_Validation ------------------------------------ 

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


# ------------------------------------------ Base_Model ------------------------------------ 


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




# ------------------------------------------ Callbacks----------------------------------------


STAGE_NAME = "Callbacks"
try: 
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = CallbackPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e