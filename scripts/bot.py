import requests
import time
import keyboard

while True:
    if keyboard.is_pressed('up') or keyboard.is_pressed('down') or keyboard.is_pressed('left') or keyboard.is_pressed('right'):
        r = requests.get('http://172.22.134.6:5000/aicar/forward/0/10')
        time.sleep(.01)

