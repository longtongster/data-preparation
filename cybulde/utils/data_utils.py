import subprocess
from shutil import rmtree

def run_shell_command(cmd: str) -> str:
    return subprocess.run(cmd, text=True, shell=True, check=True, capture_output=True).stdout


def get_cmd_to_get_raw_data(
        version: str ="a",
        data_local_save_dir: str ="./data/",
        dvc_remote_repo: str ="a",
        dvc_data_folder: str ="./data/raw/",
        github_user_name: str="a",
        github_access_token: str="a",
) -> str:
    """Get some data stuff""" 

    dvc_remote_repo = "git@github.com:longtongster/project_template_ml.git"
    # we might need to make this
    # dvc_remote_repo = "<usern>:<acc_tok>@git@github.com:longtongster/project_template_ml.git"
    command =  f"dvc list {dvc_remote_repo} {dvc_data_folder}"
    #command =  f"dvc get {dvc_remote_repo} {dvc_data_folder} --rev {version} -o {data_local_save_dir}"
    print(command)
    return command

def run_command():
    rmtree("./data/", ignore_errors=True)
    
    command = get_cmd_to_get_raw_data()
    value = run_shell_command(command)
    print(value)

run_command()