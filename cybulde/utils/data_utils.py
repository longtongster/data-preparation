def get_cmd_to_get_raw_data(
        version: str,
        data_local_save_dir: str,
        dvc_remote_repo_name: str,
        dvc_data_folder: str,
        github_user_name: str,
        github_access_token: str,
) -> str:
    """Get some data stuff""" 

    command =  f"dvc get {dvc_remote_repo} {dvc_raw_data}"
    print("piemel")

get_cmd_to_get_raw_data()