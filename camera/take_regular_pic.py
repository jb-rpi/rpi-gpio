import time
from picamera2 import Picamera2, Preview
from datetime import datetime
import os

def capture_image(picamera2, directory="/home/pi/Projects/rpi-gpio/camera/captured-images/"):
    """Capture une image et la sauvegarde dans le répertoire spécifié avec un horodatage."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{directory}image_{timestamp}.jpg"
    picamera2.capture_file(filename)
    #print(f"Photo prise et sauvegardée sous {filename}")

def main():
    # Initialisation de la caméra
    picamera2 = Picamera2()
    picamera2.configure(picamera2.create_still_configuration())

    # Créez le répertoire si nécessaire
    directory = "/home/pi/Projects/rpi-gpio/camera/captured_images/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    picamera2.start()
    try:
        while True:
            capture_image(picamera2, directory)
            # Attendre 5 minutes
            time.sleep(300)  # 300 secondes = 5 minutes
    except KeyboardInterrupt:
        print("Arrêt du script.")
    finally:
        picamera2.stop()

if __name__ == "__main__":
    main()
