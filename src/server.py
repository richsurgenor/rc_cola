#!flask/bin/python
from flask import Flask
from bluepy import btle
import binascii

app = Flask(__name__)

global driveConfig

@app.route('/aicar/connect/', methods=['GET'])
def connect():
    dev=btle.Peripheral("1c:0f:ea:24:f1:4e")
    driveCmd=btle.UUID("0000ffe5-0000-1000-8000-00805f9b34fb")
    driveService=dev.getServiceByUUID(driveCmd)

    driveUuidConfig=btle.UUID("0000ffe9-0000-1000-8000-00805f9b34fb")
    global driveConfig
    driveConfig=driveService.getCharacteristics(driveUuidConfig)[0]
    return "ok"

@app.route('/aicar/forward/<int:speed>/<int:time>', methods=['GET'])
def forward(speed, time):
    driveConfig.write(bytes(b"\x71" + bytes([speed]) + bytes([time])))
    return "ok" 

@app.route('/aicar/turn-left/<int:angle>/<int:time>', methods=['GET'])
def turn_left(angle, time):
    driveConfig.write(bytes(b"\x73" +bytes([angle]) +bytes([time])))
    return "ok"

@app.route('/aicar/turn-right/<int:angle>/<int:time>', methods=['GET'])
def turn_right(angle, time):
    driveConfig.write(bytes(b"\x74" +bytes([angle]) + bytes([time])))
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
