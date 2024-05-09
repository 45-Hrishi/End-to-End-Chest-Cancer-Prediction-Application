from dataclasses import dataclass
from pathlib import Path

# dataclass is used to stored data and frozen is used when the data is not going to change.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 
    
