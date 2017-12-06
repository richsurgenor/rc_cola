from picamera import PiCamera
import requests
import datetime


class CarTraining(object):
    
    def request_input(self):  
        endpoint = input('Enter an API path\n')
        r = requests.get('http://localhost:5000/aicar/' + endpoint) 
        return endpoint



camera = PiCamera()
while True:
    trainer = CarTraining()
    endpoint = trainer.request_input()
    path = endpoint.split('/')
    keep = input('good?')
    if keep == 'y':
        name = "-".join(path)
        time = datetime.datetime.now().strftime("%I:%M:%S %M-%d")
        name += "-" + time
        camera.capture("/home/pi/rc_cola/data/" + name + ".jpg")

