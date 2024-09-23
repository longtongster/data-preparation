from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING
from cybulde.utils.aws_secret import get_secret 


@dataclass
class DataProcessingConfig:
    version: str = "1" #MISSING
    data_local_save_dir = "./data/raw"
    dvc_remote_repo = "git@github.com:longtongster/project_template.git"
    dvc_data_folder = "./data/raw"
    github_user_name = "longtongster"
    github_access_token = "no_way"



def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="data_processing_config_schema", node=DataProcessingConfig)
