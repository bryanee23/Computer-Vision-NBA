import os


MATCHES_DIR = (f"/Users/bryanevangelista/Documents/projects/flask-site/static/images/matches")
matched_imgs = os.listdir(MATCHES_DIR)



index = -1
def increase_index():
    global index
    index += 1

def decrease_index():
    global index
    index -= 1

def reset():
    global index
    index = -1


def img_slider(direction):
  if index >= len(matched_imgs)-1:
    reset()

  if direction == 'next':
    increase_index()

  if direction == 'prev' and index <= -1:
    reset()
    increase_index()

  elif direction == 'prev' and index == 0:
    pass

  elif direction == 'prev':
    decrease_index()

  return matched_imgs[index]