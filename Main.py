import ExtractText
import ParseExtractedText

import PopulateParkingLocations

# PopulateParkingLocations.post_lot()
# ExtractText.detect_text('/Users/viviannguyen/PycharmProjects/CARAGE/assets/stream-test/30-01-2021_16.01.21.jpg')
# ExtractText.detect_text('/Users/viviannguyen/PycharmProjects/CARAGE/assets/stream-test/30-01-2021_16.01.32.jpg')
# ExtractText.detect_text('/Users/viviannguyen/PycharmProjects/CARAGE/assets/stream-test/30-01-2021_16.01.42.jpg')
# ParseExtractedText.calculate_density('Lot6A')
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "/Users/viviannguyen/PycharmProjects/CARAGE/assets/stream-test/"

    def __init__(self):
        self.observer = Observer()
        self.event_handler = PatternMatchingEventHandler(patterns=["*.jpg", "*.jpeg", "*.png", "*.bmp", "*.pdf"],
                                                         ignore_patterns=[".*"],
                                                         ignore_directories=True)
        self.event_handler.on_created = self.on_created
        self.observer.schedule(self.event_handler, self.DIRECTORY_TO_WATCH, recursive=True)

    @staticmethod
    def on_created(event):
        print("Received created event - %s." % event.src_path)
        ExtractText.detect_text(event.src_path)
        print("Calculated Spots Filled")
        ParseExtractedText.calculate_density('Lot6A')
        print("Calculated Lot Density")

    def run(self):
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error Observing")

        self.observer.join()


if __name__ == '__main__':
    PopulateParkingLocations.post_lot()
    ob = Watcher()
    ob.run()
