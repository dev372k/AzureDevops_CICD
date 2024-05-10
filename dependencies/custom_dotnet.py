import subprocess
import os
import shutil

def release(project_directory, proj_file, release_path) -> bool:
    command = f"dotnet build -c release {proj_file}"
    try:
        subprocess.run(command, shell=True, check=True, cwd=project_directory)
        print("Build successful.")

        source_directory = os.path.join(project_directory, "bin", release_path)
        
        destination_directory = "release"
        
        if os.path.exists(destination_directory):
            if os.path.isdir(destination_directory):
                shutil.rmtree(destination_directory)
                print(f"Deleted existing '{destination_directory}' directory.")

        shutil.copytree(source_directory, destination_directory)
        print("Files copied successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


