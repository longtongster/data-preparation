import subprocess
from shutil import rmtree

def run_shell_command(cmd: str) -> str:
    return subprocess.run(cmd, text=True, shell=True, check=True, capture_output=True).stdout


def get_cmd_to_get_raw_data(
    version: str,
    data_local_save_dir: str,
    dvc_remote_repo: str,
    dvc_data_folder: str,
    github_user_name: str,
    github_access_token: str,
) -> str:
    """Get shell command to download the raw data from dvc store

    Parameters
    ----------
    version: str
        data version
    data_local_save_dir: str
        where to save the downloaded data locally
    dvc_remote_repo: str
        dvc repository that holds information about the data
    dvc_data_folder: str
        localtion where the remote data is stored
    github_user_name: str
        github user name
    github_access_token: str
        github access token

    Returns
    -------
    str
        shell command to download the raw data from dvc store
    """
    without_https = dvc_remote_repo.replace("https://", "")
    dvc_remote_repo = f"https://{github_user_name}:{github_access_token}@{without_https}"
    command = f"dvc get {dvc_remote_repo} {dvc_data_folder} --rev {version} -o {data_local_save_dir}"
    return command

# def get_cmd_to_get_raw_data(
#         version: str,
#         data_local_save_dir: str,
#         dvc_remote_repo: str,
#         dvc_data_folder: str,
#         github_user_name: str,
#         github_access_token: str) -> str:
#     """Get some data stuff""" 

#     #dvc_remote_repo = "git@github.com:longtongster/project_template_ml.git"
#     # we might need to make this
#     # dvc_remote_repo = "<usern>:<acc_tok>@git@github.com:longtongster/project_template_ml.git"
#     # command =  f"dvc list {dvc_remote_repo} {dvc_data_folder}"
#     command =  f"dvc get {dvc_remote_repo} {dvc_data_folder} --rev {version} -o {data_local_save_dir}"
#     print(command)
#     return command

def run_command(        
        version: str,
        data_local_save_dir: str,
        dvc_remote_repo: str,
        dvc_data_folder: str,
        github_user_name: str,
        github_access_token: str):
    
    rmtree("./data/", ignore_errors=True)
    
    command = get_cmd_to_get_raw_data(version, data_local_save_dir, dvc_remote_repo, dvc_data_folder, github_user_name, github_access_token)
    value = run_shell_command(command)
    print(value)