from ChestDiseasePrediction import logger
from ChestDiseasePrediction.config.configuration import ConfigurationManager
from ChestDiseasePrediction.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        configmanager = ConfigurationManager()
        prepare_base_model_config = configmanager.get_prepare_base_model_config()
        base_model = PrepareBaseModel(prepare_base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e