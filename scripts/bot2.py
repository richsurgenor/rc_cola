import requests
import time
import keyboard
import datetime

PATH = 'http://172.22.129.15:5000/aicar/'
r = requests.get(PATH  + 'connect')


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
    if keyboard.is_pressed('h'):
        action = PATH + '06-29-24'
    if keyboard.is_pressed('g'):
        action = PATH + '06-8-24'
    if keyboard.is_pressed('f'):
        action = PATH + '06-16-24'
    
    if action:
        r = requests.get(action)
        
    time.sleep(.01)
