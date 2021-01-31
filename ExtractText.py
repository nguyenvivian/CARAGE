import io
import os
import string
from google.cloud import vision
from firebase import firebase
from datetime import datetime
from EnvironmentConstants import FIREBASE_URL, GOOGLE_APPLICATION_CREDENTIALS
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS
firebase = firebase.FirebaseApplication(FIREBASE_URL, None)


# Takes the path to an image and sends a request to the Vision API.
# Image is then parsed for text and returned via a JSON response.
def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    extractedPhrases = []

    for text in texts:
        #Image Noise Processing
        extractedPhrases.append(text.description.translate(str.maketrans('', '', string.punctuation))
)
    if response.error.message:
        raise Exception('{}\n'.format(response.error.message))

    post_text(extractedPhrases)


# Sends a POST request to the Firebase Realtime DB.
def post_text(extractedPhrases):
    data = {'ParkingLot': 'Lot 6A',
            'TimeTaken': datetime.now(),
            'ExtractedPhrasesRaw': extractedPhrases
            }
    result = firebase.post('/ExtractedText/Lot6A/', data)

# detect_text('test-6-emptylot.jpg')
