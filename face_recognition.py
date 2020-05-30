import face_recognition
import os
import cv2

# directory setup, opencv border settings
ROOT_DIR = os.getcwd()
KNOWN_FACES_DIR = (f"{ROOT_DIR}/static/images/known")
UNKNOWN_FACES_DIR = (f"{ROOT_DIR}/static/images/unknown")
MATCHES_DIR = (f"{ROOT_DIR}/static/images/matches")
UPLOADED_IMAGES_DIR = (f"{ROOT_DIR}/static/images/uploaded")

# face_recognition settings
TOLERANCE = 0.45
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
OFFSET = 15
COLOR = [0, 255, 0]
MODEL = "cnn"

# delete files in matches folder
if len(os.listdir(MATCHES_DIR)) > 0:
    for image in os.listdir(MATCHES_DIR):
      if image.endswith('.png'):
        os.unlink(f"{MATCHES_DIR}/{image}")

# delete files in matches folder
if len(os.listdir(UNKNOWN_FACES_DIR)) > 0:
    for image in os.listdir(UNKNOWN_FACES_DIR):
      os.unlink(f"{UNKNOWN_FACES_DIR}/{image}")


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
      path = MATCHES_DIR
      cv2.imwrite(f'{UNKNOWN_FACES_DIR}/{filename}', resized)
    else:
      cv2.imwrite(f'{UNKNOWN_FACES_DIR}/{filename}', image)




known_faces = []
known_names = []

print('Loading Known Person')
# iterate through known faces directory to save known face encodings into an array
for name in os.listdir(KNOWN_FACES_DIR):
  if name.endswith(".DS_Store"):
      continue
  else:
      for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
          image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
          encoding = face_recognition.face_encodings(image)[0]
          known_faces.append(encoding)
          known_names.append(name)

print("Processing Unknown Faces")
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
            player = [{'first':'last'}]
            cv2.imwrite(f"{MATCHES_DIR}/{filename}", image)


