import os
import git # type: ignore

def clone(remote_repo_url, branch_name, local_repo_path) -> bool:
    if os.path.exists(local_repo_path):
        try:
            repo = git.Repo(local_repo_path)
            repo.git.checkout(branch_name)
            origin = repo.remotes.origin
            origin.pull()
            
            print('Pull successful.')
            
            return True
        except git.GitCommandError as e:
            print(f"Error: {e}")

            return False
    else:
        try:
            repo = git.Repo.clone_from(remote_repo_url, local_repo_path)
            repo.git.checkout(branch_name)
            print('Cloned successful.')

            return True
        except git.GitCommandError as e:
            print(f"Error: {e}")
            
            return False
