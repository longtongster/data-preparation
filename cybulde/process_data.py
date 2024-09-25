from cybulde.config_schemas.data_processing_config_schema import DataProcessingConfig
from cybulde.utils.config_utils import get_config
from utils.data_utils import run_command
from utils.aws_secret import get_secret


@get_config(config_path="../configs", config_name="data_processing_config")
def process_data(config: DataProcessingConfig) -> None:
    print(config)
    config.version = "v6"
    # data_local_save_dir = config.data_local_save_dir
    # dvc_remote_repo = config.dvc_remote_repo
    # dvc_data_folder = config.dvc_data_folder
    # github_user_name = config.github_user_name
    # github_access_token = config.github_access_token

    #print(config.version, data_local_save_dir, dvc_remote_repo, dvc_data_folder, github_user_name, github_access_token, github_access_token)

    # run_command(config.version, 
    #             data_local_save_dir = config.data_local_save_dir, 
    #             dvc_remote_repo = config.dvc_remote_repo, 
    #             dvc_data_folder = config.dvc_data_folder, 
    #             github_user_name = config.github_user_name, 
    #             github_access_token = config.github_access_token)


if __name__ == "__main__":
    process_data()  # type: ignore
