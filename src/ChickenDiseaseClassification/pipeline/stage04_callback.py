from ChickenDiseaseClassification.config.configuration import ConfigurationManager
import os
from ChickenDiseaseClassification.components.callback import PrepareCallback
from ChickenDiseaseClassification import logger




STAGE_NAME = "Callbacks"

class CallbackPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = CallbackPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e