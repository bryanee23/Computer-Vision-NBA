import face_recognition
import os
import cv2
from directory import *

# face_recognition settings
TOLERANCE = 0.45
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
OFFSET = 15
COLOR = [0, 255, 0]
MODEL = "cnn"


# resize images to fit within grid
def resize_images():

  if len(os.listdir(f"{UPLOADED_IMAGES_DIR}")) != len(os.listdir(f"{UNKNOWN_FACES_DIR}")):
    print('Resizing Images')
    for filename in os.listdir(f"{UPLOADED_IMAGES_DIR}"):
      image = cv2.imread(f"{UPLOADED_IMAGES_DIR}/{filename}")

      if image.shape[1] > 650 and image.shape[0] > 650:
        scale_percent = 70
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dsize = (width, height)
        resized = cv2.resize(image, dsize)
        cv2.imwrite(f'{UNKNOWN_FACES_DIR}/{filename}', resized)
      else:
        cv2.imwrite(f'{UNKNOWN_FACES_DIR}/{filename}', image)


known_faces = []
known_names = []


def initate_recognition():

  print('Loading Known Person')

  for name in os.listdir(KNOWN_FACES_DIR):
    if name.endswith(".DS_Store"):
        continue

    else:

        for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
          image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
          encoding = face_recognition.face_encodings(image)[0]
          known_faces.append(encoding)
          known_names.append(name)

################################################
#### technically two functions
#### initiate and loading knowns
#### loading knowns was not working correctly
################################################

  print("Processing Unknown Faces")
  counter = 0
  for filename in os.listdir(f"{UNKNOWN_FACES_DIR}"):

      image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
      face_locations = face_recognition.face_locations(image, model=MODEL)
      encodings = face_recognition.face_encodings(image, face_locations) #takes current image and finds all faces
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

      for face_encoding, face_location in zip(encodings, face_locations):

          results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
          match = None

          if True in results:

              match = known_names[results.index(True)]
              top_left = (face_location[3], face_location[0] - OFFSET)
              bottom_right = (face_location[1] + OFFSET, face_location[2] + OFFSET)
              cv2.rectangle(image, top_left, bottom_right, COLOR, FRAME_THICKNESS)

              cv2.putText(
                image,
                match,
                (face_location[3] - 10 , face_location[2] + 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                COLOR,
                FONT_THICKNESS
              )

              print(f"Match Found: {match}")

              cv2.imwrite(f"{MATCHES_DIR}/{match}-{counter}.png", image)
              counter += 1

# clear list contents
  while len(known_faces) > 0:
    known_faces.pop()
  while len(known_names) > 0:
    known_names.pop()

  print('Face Recognintion Complete')


def run_face_recognition_script():
  resize_images()
  initate_recognition()