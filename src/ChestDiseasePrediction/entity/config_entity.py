from dataclasses import dataclass
from pathlib import Path

# dataclass is used to stored data and frozen is used when the data is not going to change.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 
    
@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path :Path
    params_image_size : list
    params_learning_rate : float
    params_include_top: bool
    params_weights: str
    params_classes: int
    
@dataclass(frozen=True)
class TrainingConfig:
    root_dir:Path
    trained_model_path:Path
    updated_base_model_path:Path
    training_data:Path
    params_epochs:int
    params_batch_size:int
    params_is_augmented:bool
    params_image_size:list 
    

@dataclass(frozen=True)
class ModelEvaluationConfig:
    path_of_model:Path
    training_data:Path
    all_params:dict
    mlflow_uri:str
    params_image_size:list
    params_batch_size:int