from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.stop_preview()

# This is a change to test .gitignore
# Test Push
# testing test branch
# showing testing output in testing branch