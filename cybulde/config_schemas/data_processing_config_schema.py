from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING

#from cybulde.utils.aws_secret import get_secret 
from cybulde.config_schemas.data_processing import dataset_readers_schema

@dataclass
class DataProcessingConfig:
    version: str = MISSING
    data_local_save_dir: str = "./data/raw"
    dvc_remote_repo: str = "https://github.com/longtongster/project_template.git"
    dvc_data_folder: str = "./data/raw"
    github_user_name: str = "longtongster"
    # github_access_token = get_secret()
    github_access_token = "test-secret"

    dataset_reader_manager: dataset_readers_schema.DatasetReaderManagerConfig = MISSING


def setup_config() -> None:
    dataset_readers_schema.setup_config()
    cs = ConfigStore.instance()
    cs.store(name="data_processing_config_schema", node=DataProcessingConfig)
    