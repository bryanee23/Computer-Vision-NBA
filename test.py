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

  return index



def start():
  print(match_list)
  print(match_list[0])

# mimics a next press
# def image_slider(1):
#   return image_slider(1)


def postive_edge():
  current_image = match_list[image_slider(1)]
  return current_image

def negative_edge():
  current_image = match_list[image_slider(-1)]
  return current_image

# start() # --0 start
# print(postive_edge()) # --1
# print(postive_edge()) # --2
# print(postive_edge()) # --0 output is 1
# print(postive_edge())

start() # --0 start
print(negative_edge()) # --0
print(negative_edge()) # --0
