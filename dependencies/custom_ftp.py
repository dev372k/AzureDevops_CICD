import ftplib
import os


# Replace these with your details
server_address = "72.52.175.14"
username = "inshal-dev"
password = "Noman!@123"
local_dir = "release"  # Replace with the source directory
remote_dir = "/"  # Replace with the target directory on the server


def deploy(confirm=True):
    """
    Deploys the entire local folder structure to the FTP server,
    recursively copying files and directories.

    Args:
        confirm (bool, optional): Prompt for confirmation before uploading
            (defaults to True).
    """

    try:
        ftp = ftplib.FTP(server_address)
        ftp.login(username, password)
        ftp.set_pasv(True)  # Use passive mode for firewalled environments (optional)

        if confirm:
            answer = input(f"This will copy all files and directories from '{local_dir}' to '{remote_dir}' on the server. Are you sure? (y/N): ")
            if answer.lower() not in ("y", "yes"):
                print("Upload canceled.")
                return

        for root, dirs, files in os.walk(local_dir):
            remote_sub_dir = os.path.relpath(root, local_dir)  # Relative path for subdirectories
            try:
                ftp.mkd(os.path.join(remote_dir, remote_sub_dir))  # Create directories on the server
                print(f"Created directory: {os.path.join(remote_dir, remote_sub_dir)}")
            except ftplib.all_errors as e:
                # Handle potential directory creation errors (e.g., already exists)
                print(f"Directory creation error: {e}")
                continue  # Skip to the next iteration

            for filename in files:
                local_filepath = os.path.join(root, filename)
                with open(local_filepath, "rb") as file:
                    try:
                        ftp.storbinary(f"STOR {os.path.join(remote_sub_dir, filename)}", file)
                        print(f"Uploaded: {os.path.join(remote_sub_dir, filename)}")
                    except ftplib.all_errors as e:
                        print(f"Error uploading file: {e}")

        print("Folder deployment successful!")
    except Exception as e:  # Catch any other unexpected errors
        print(f"Unexpected error: {e}")
    finally:
        ftp.quit()



