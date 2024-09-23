from cybulde.config_schemas.data_processing_config_schema import DataProcessingConfig
from cybulde.utils.config_utils import get_config
from utils.data_utils import run_command
from utils.aws_secret import get_secret


@get_config(config_path="../configs", config_name="config")
def process_data(config: DataProcessingConfig) -> None:
    print(config)
    version = "v3"
    data_local_save_dir = "./data/raw"
    dvc_remote_repo = "git@github.com:longtongster/project_template.git"
    dvc_data_folder = "./data/raw"
    github_user_name = "longtongster"
    github_access_token = get_secret()
    print(github_access_token)

    #run_command(version, data_local_save_dir, dvc_remote_repo, dvc_data_folder, github_user_name, github_access_token)


if __name__ == "__main__":
    process_data()  # type: ignore
