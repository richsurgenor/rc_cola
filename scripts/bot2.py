import requests
import time
import keyboard
import datetime
from picamera import PiCamera

PATH = 'http://localhost:5000/aicar/'
r = requests.get(PATH  + 'connect')

camera = PiCamera(resolution="160x120")
camera.rotation = 180

def capture(direction):
    name = direction
    cur_time = datetime.datetime.now().strftime("%I:%M:%S %M-%d")
    name += "-" + cur_time
    camera.capture("/home/pi/rc_cola/data/" + name + ".jpg", use_video_port=True)
    


while True:
    direction = None
    action = None
    if keyboard.is_pressed('up') :
        action = PATH + 'forward/0/10'
        direction = 'up'
    if keyboard.is_pressed('left'): 
        action = PATH + 'turn-left/8/1'
        direction = 'left'
    if keyboard.is_pressed('right'):
        action = PATH + 'turn-right/8/1'
        direction = 'right'
    if keyboard.is_pressed('down'):
        action = PATH + 'turnyboi'
        direction = 'down'
    
    if direction:
        capture(direction)
    if action:
        r = requests.get(action)
        
    time.sleep(.01)
