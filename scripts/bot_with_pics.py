import requests
import time
import keyboard
from picamera import PiCamera

PATH = 'http://localhost:5000/aicar/'
r = requests.get(PATH  + 'connect')

camera = PiCamera(resolution="160x120")

direction = None

while True:
    if keyboard.is_pressed('up') :
        r = requests.get(PATH + 'forward/0/10')
        direction = 'up'
    if keyboard.is_pressed('left'): 
        r = requests.get(PATH + 'turn-left/2/1')
        direction = 'left'
    if keyboard.is_pressed('right'):
        r = requests.get(PATH + 'turn-right/2/1')
        direction = 'right'
    ##if keyboard.is_pressed('down'):
    ##    r = requests.get('http://localhost:5000/aicar/backward/1/10')
    ##    direction = 'down'

    name = direction
    time = datetime.datetime.now().strftime("%I:%M:%S %M-%d")
    name += "-" + time
    camera.capture("/home/pi/rc_cola/data/" + name + ".jpg")

    camera.capture(
    time.sleep(.01)
