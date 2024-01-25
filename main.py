from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline





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