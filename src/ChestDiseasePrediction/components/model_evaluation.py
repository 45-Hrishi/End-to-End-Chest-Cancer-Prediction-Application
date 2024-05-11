from pathlib import Path
from ChestDiseasePrediction.entity.config_entity import ModelEvaluationConfig
from ChestDiseasePrediction.utils.common import *
import tensorflow as tf
import mlflow
from urllib.parse import urlparse
import mlflow.keras

class ModelEvaluation:
    def __init__(self,config=ModelEvaluationConfig):
        self.config = config
    
    @staticmethod
    def load_model(path:Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def save_score(self):
        scores = {"loss":self.score[0],"accuracy":self.score[1]}
        save_json(path=Path("scores.json"),data=scores)
        
    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )
        
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        
    def model_evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def log_into_mlflow(self):
            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            with mlflow.start_run():
                mlflow.log_params(self.config.all_params)
                mlflow.log_metrics({"loss":self.score[0],"accuracy":self.score[1]})

                if tracking_url_type_store != "file":
                    mlflow.keras.log_model(self.model,"model",registered_model_name="VGG16Model")
                else:
                    mlflow.keras.log_model(self.model,"model")