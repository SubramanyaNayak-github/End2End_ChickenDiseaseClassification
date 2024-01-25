from dataclasses import dataclass
from pathlib import Path



# ------------------------------------------ Data_Ingestion ------------------------------------ 


@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir:Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path


# ------------------------------------------ Data_Validation ------------------------------------ 



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list



# ------------------------------------------ Base_Model ------------------------------------ 



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int