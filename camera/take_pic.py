from picamera2 import Picamera2, Preview
from time import sleep

picam0 = Picamera2(0)

picam0.start_preview(Preview.QTGL)

picam0.start()

sleep(10)

picam0.capture_file("cam0.jpg")

picam0.stop()

picam0.stop_preview()


