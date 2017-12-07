import requests
import time
import keyboard
import datetime
from picamera import PiCamera

PATH = 'http://localhost:5000/aicar/'
r = requests.get(PATH  + 'connect')

camera = PiCamera(resolution="160x120")
camera.rotation = 180

direction = None

while True:
    direction = None
    if keyboard.is_pressed('up') :
        r = requests.get(PATH + 'forward/0/10')
        direction = 'up'
    if keyboard.is_pressed('left'): 
        r = requests.get(PATH + 'turn-left/8/1')
        direction = 'left'
    if keyboard.is_pressed('right'):
        r = requests.get(PATH + 'turn-right/8/1')
        direction = 'right'
    if keyboard.is_pressed('down'):
        r = requests.get(PATH + '180')
        direction = 'down'

    
    if direction:
        name = direction
        cur_time = datetime.datetime.now().strftime("%I:%M:%S %M-%d")
        name += "-" + cur_time
        camera.capture("/home/pi/rc_cola/data/" + name + ".jpg", use_video_port=True)
    

    time.sleep(.01)
