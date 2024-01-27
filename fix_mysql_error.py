import os
import shutil

def rename_folder(old_path, new_path):
    try:
        if os.path.exists(old_path):
            shutil.move(old_path, new_path)
            print(f"Folder '{old_path}' successfully renamed to '{new_path}'.")
        else:
            print(f"Error: The folder '{old_path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

def create_folder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' successfully created.")
        else:
            print(f"Error: The folder '{folder_path}' already exists.")
    except Exception as e:
        print(f"Error: {e}")

def copy_files(src_folder, dest_folder):
    try:
        if os.path.exists(src_folder):
            for item in os.listdir(src_folder):
                source_item = os.path.join(src_folder, item)
                destination_item = os.path.join(dest_folder, item)
                if os.path.isdir(source_item):
                    shutil.copytree(source_item, destination_item)
                else:
                    shutil.copy2(source_item, destination_item)
            print(f"Contents of '{src_folder}' successfully copied to '{dest_folder}'.")
        else:
            print(f"Error: The source folder '{src_folder}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

def copy_database_folders(old_folder, new_folder, exclude_folders):
    try:
        if os.path.exists(old_folder):
            for item in os.listdir(old_folder):
                source_item = os.path.join(old_folder, item)
                destination_item = os.path.join(new_folder, item)
                if os.path.isdir(source_item) and item not in exclude_folders:
                    shutil.copytree(source_item, destination_item)
            print(f"Database folders from '{old_folder}' successfully copied to '{new_folder}'.")
        else:
            print(f"Error: The source folder '{old_folder}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

def copy_ibdata_file(old_file, new_folder):
    try:
        if os.path.exists(old_file):
            new_file = os.path.join(new_folder, os.path.basename(old_file))
            shutil.copy2(old_file, new_file)
            print(f"ibdata1 file successfully copied to '{new_folder}'.")
        else:
            print(f"Error: The source file '{old_file}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

def remove_folder(folder_path):
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' successfully removed.")
        else:
            print(f"Error: The folder '{folder_path}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Specify the old and new paths
    original_folder_path = r'C:\xampp\mysql\data'
    new_folder_path = r'C:\xampp\mysql\data_old'
    new_subfolder_path = r'C:\xampp\mysql\data'
    backup_folder_path = r'C:\xampp\mysql\backup'
    ibdata_file_path = r'C:\xampp\mysql\data_old\ibdata1'

    # Call the function to rename the folder
    rename_folder(original_folder_path, new_folder_path)

    # Call the function to create a new folder
    create_folder(new_subfolder_path)

    # Call the function to copy files and folders from the backup path to the new path
    copy_files(backup_folder_path, new_subfolder_path)

    # Specify the paths for copying database folders
    old_database_folder = r'C:\xampp\mysql\data_old'
    new_database_folder = r'C:\xampp\mysql\data'
    
    # Specify folders to exclude from copying
    exclude_folders = ['mysql', 'performance_schema', 'phpmyadmin', 'test']

    # Call the function to copy database folders
    copy_database_folders(old_database_folder, new_database_folder, exclude_folders)

     # Call the function to copy ibdata1 file
    copy_ibdata_file(ibdata_file_path, new_subfolder_path)

    # Call the function to remove the old folder
    remove_folder(old_database_folder)

if __name__ == "__main__":
    main()
