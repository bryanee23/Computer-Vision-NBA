import os
import shutil

# https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

ROOT_DIR = os.getcwd()

def delete_folder(folder):
  FOLDER_DIR = (f"{ROOT_DIR}/static/images/{folder}")
  for file in os.listdir(FOLDER_DIR):
    print(file, 'folder deleted')
    shutil.rmtree(f"{FOLDER_DIR}/{file}/")


def delete_folder_contents(folder):
  FOLDER_DIR = (f"{ROOT_DIR}/static/images/{folder}")
  for file in os.listdir(FOLDER_DIR):
    os.remove(f"{FOLDER_DIR}/{file}")


def reset_all():
  delete_folder("known")
  delete_folder_contents("unknown")
  delete_folder_contents("matches")
  delete_folder_contents("uploads")
