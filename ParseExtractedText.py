import re
from firebase import firebase

firebase = firebase.FirebaseApplication('https://formal-era-303305-default-rtdb.firebaseio.com/', None)

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
        openSpot = re.sub(r'\d+', '', str(openSpot))
        if openSpot in str(lotData[next(iter(lotData))].keys()):
            spotFilled[openSpot] += 1
    spotFilled['Total'] = sum(spotFilled.values())

    for spotType in densityData.keys():
        densityData[spotType] = spotFilled[spotType]/spotFreq[spotType]

    post_density_data(densityData)


# Sends a POST request to the Firebase Realtime DB.
def post_density_data(densityData):
    result = firebase.post('/DensityData/Lot6A/', densityData)


calculate_density('Lot6A')