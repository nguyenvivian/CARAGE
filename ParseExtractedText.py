import re
import string

from firebase import firebase

from EnvironmentConstants import FIREBASE_URL

firebase = firebase.FirebaseApplication(FIREBASE_URL, None)

def calculate_density(parkingLot):
    lotData = firebase.get('/ParkingLocationCount/'+parkingLot+'/', '')
    extractedText = firebase.get('/ExtractedText/'+parkingLot+'/', '')

    densityData = {}
    spotFilled = {}

    for spotType in lotData[next(iter(lotData))].keys():
        spotFilled[spotType] = 0
        densityData[spotType] = 0
    spotFreq = dict(lotData[next(iter(lotData))].items())

    for openSpot in extractedText[next(reversed(extractedText))]['ExtractedPhrasesRaw'][1:]:
        #Post-noise Processing
        openSpot = re.sub(r'\d+', '', str(openSpot))

        if openSpot in str(lotData[next(iter(lotData))].keys()) and openSpot in spotFilled and openSpot:
            spotFilled[openSpot] += 1
    spotFilled['Total'] = sum(spotFilled.values())
    spotFilled['TimeTaken'] = extractedText[next(reversed(extractedText))]['TimeTaken']

    post_raw_freq_data(spotFilled)

    for spotType in densityData.keys():
        densityData[spotType] = spotFilled[spotType]/spotFreq[spotType]

    densityData['TimeTaken'] = extractedText[next(reversed(extractedText))]['TimeTaken']
    post_density_data(densityData)

    print(spotFilled)


# Sends a POST request to the Firebase Realtime DB.
def post_raw_freq_data(spotFilled):
    result = firebase.post('/Frequency/Lot6A/', spotFilled)


# Sends a POST request to the Firebase Realtime DB.
def post_density_data(densityData):
    result = firebase.post('/DensityData/Lot6A/', densityData)

