import io
import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'carage-service-account-token-f525563457d6.json'


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

    return extractedPhrases

# detect_text('test-4.jpg')
