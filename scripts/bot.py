import requests
import time
import keyboard

while True:
    if keyboard.is_pressed('up') :
        r = requests.get('http://localhost:5000/aicar/forward/0/10')
    if keyboard.is_pressed('left'): 
        r = requests.get('http://localhost:5000/aicar/turn-left/2/1')
    if keyboard.is_pressed('right'):
        r = requests.get('http://localhost:5000/aicar/turn-right/2/1')
    if keyboard.is_pressed('down'):
        r = requests.get('http://localhost:5000/aicar/backward/1/10')

    time.sleep(.01)
