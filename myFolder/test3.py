import cv2
from djitellopy import Tello
import time

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
time.sleep(3)

cv2.imwrite("picture.png", frame_read.frame)

tello.land()