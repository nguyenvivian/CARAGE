import ExtractText
import ParseExtractedText
import PopulateParkingLocations

FIREBASE_URL = 'https://formal-era-303305-default-rtdb.firebaseio.com/'

PopulateParkingLocations.post_lot()
ExtractText.detect_text('test-5.jpg')
ParseExtractedText.calculate_density('Lot6A')