import io
import os
import json
from google.cloud import vision
from firebase import firebase
from datetime import datetime

from Main import FIREBASE_URL

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'carage-service-account-token-f525563457d6.json'
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

    print('Text:')
    for text in texts:
        print('\n"{}"'.format(text.description))
        extractedPhrases.append(text.description)

    print(extractedPhrases)

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

# detect_text('test-5.jpg')
