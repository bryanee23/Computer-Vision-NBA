import os


def delete_contents(folder):
  FOLDER_DIR = (f"/Users/bryanevangelista/Documents/projects/flask-site/static/images/{folder}")
  for file in os.listdir(FOLDER_DIR):
    print(file)
    os.remove(f"{FOLDER_DIR}/{file}/")

delete_contents("known")