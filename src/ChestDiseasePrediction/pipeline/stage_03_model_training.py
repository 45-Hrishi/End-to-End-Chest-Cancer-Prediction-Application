from ChestDiseasePrediction.config.configuration import ConfigurationManager
from ChestDiseasePrediction.components.model_training import ModelTraining
from ChestDiseasePrediction import logger

STAGE_NAME = "Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        configmanager = ConfigurationManager()
        model_training_config = configmanager.get_training_model_config()
        model_training = ModelTraining(model_training_config)
        model_training.get_base_model()
        model_training.train_valid_generator()
        model_training.train()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e