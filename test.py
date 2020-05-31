import os
from directory import *

match_list = os.listdir(MATCHES_DIR)




index = 0
def img_slider(n):
  global index
  len_list = len(match_list)-1

  # index += n
  if index == len_list:
    index = 0
  else:
    index += n

  return index



def start():
  print(match_list)
  print(match_list[0])

# mimics a next press
# def img_slider(1):
#   return img_slider(1)


def postive_edge():
  current_img = match_list[img_slider(1)]
  return current_img

def negative_edge():
  start()
  print(next_img())
  print(next_img())
  print(next_img())
  print(prev())

start()
print(postive_edge())
print(postive_edge())
print(postive_edge())
print(postive_edge())
# negative_edge()
# print(next_img())
# print(next_img())
# print(next_img())



#on start
# MATCHES_DIR[0]

# edge cases:
# at the end

#at the beggining:
  # negative

# brute force = restrict code on html
  # if at the end of array, reset back to beginning
  # can't press neg