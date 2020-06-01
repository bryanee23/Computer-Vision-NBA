import os
from directory import *

match_list = os.listdir(MATCHES_DIR)

index = 0
def image_slider(n):
  global index
  len_list = len(match_list)-1

  if index == len_list and n == 1:
    index = 0
  elif index >= 0 and n == 1:
    index += n

  if index <= 0 and n == -1:
    index = len_list
  elif index == len_list and n == -1:
    index += n
  elif index > 0 and n == -1:
    index += n

  print(index)
  return index