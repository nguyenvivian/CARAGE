from firebase import firebase

firebase = firebase.FirebaseApplication('https://formal-era-303305-default-rtdb.firebaseio.com/', None)

# Sends a POST request to the Firebase Realtime DB. Currently filled with arbitrary numbers for test purposes.
# Eventually these numbers will be managed by an enterprise application and populated with every lot on campus.
def post_lot():
    data = {'HANDICAP': 3,
            'GENERAL': 6,
            'RESERVED': 2,
            'PREFERRED': 2,
            'EXECUTIVE': 1,
            'Total': 14
            }
    result = firebase.post('/ParkingLocationCount/Lot6A/', data)

