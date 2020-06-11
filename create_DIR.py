import os
from directory import IMAGES_DIR
from flask import Flask

folders = ['known', 'unknown', 'matches', 'uploads']

def create_IMAGES_DIR():
  if (f"{IMAGES_DIR}/{folders[0]}") == True:
    pass
  else:
    for folder_Name in folders:
      path = (f"{IMAGES_DIR}/{folder_Name}")
      try:
        os.mkdir(path)
      except OSError:
          print ("Creation of the directory %s failed" % path)
      else:
          print ("Successfully created the directory %s" % path)

    return path


