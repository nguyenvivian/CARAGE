import ExtractText
import ParseExtractedText
import PopulateParkingLocations

PopulateParkingLocations.post_lot()
ExtractText.detect_text('test-5.jpg')
ParseExtractedText.calculate_density('Lot6A')