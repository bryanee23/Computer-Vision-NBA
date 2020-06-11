import os
import shutil
from reload_server import reload_server

ROOT_DIR = os.getcwd()

def delete_folder(folder):
  FOLDER_DIR = (f"{ROOT_DIR}/static/images/{folder}")
  for file in os.listdir(FOLDER_DIR):
    shutil.rmtree(f"{FOLDER_DIR}/{file}/")


def delete_folder_contents(folder):
  FOLDER_DIR = (f"{ROOT_DIR}/static/images/{folder}")
  for file in os.listdir(FOLDER_DIR):
    os.remove(f"{FOLDER_DIR}/{file}")

def delete_cache():
  FOLDER_DIR = (f"{ROOT_DIR}/__pycache__")
  for file in os.listdir(FOLDER_DIR):
    os.remove(f"{FOLDER_DIR}/{file}")

def reset_all():
  delete_folder("known")
  delete_folder_contents("unknown")
  delete_folder_contents("uploads")
  delete_folder_contents("matches")
  reload_server()
  print('Reset Complete')

