import os
import shutil

# https://www.geeksforgeeks.org/delete-a-directory-or-file-using-python/

def delete_folders(folder):
  FOLDER_DIR = (f"/Users/bryanevangelista/Documents/projects/flask-site/static/images/{folder}")

  for file in os.listdir(FOLDER_DIR):
    print(file)
    shutil.rmtree(f"{FOLDER_DIR}/{file}/")



def delete_contents(folder):
  FOLDER_DIR = (f"/Users/bryanevangelista/Documents/projects/flask-site/static/images/{folder}")

  for file in os.listdir(FOLDER_DIR):
    os.remove(f"{FOLDER_DIR}/{file}")


def reset_all():
  delete_folders("known")
  delete_contents("unknown")

# delete_contents("unknown")
# delete_contents("unknown")
# reset_all()