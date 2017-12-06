import io
import time
import picamera
from PIL import Image

def outputs(x):
    stream = io.BytesIO()
    for i in range(x):
        # This returns the stream for the camera to capture to
        yield stream
        # Once the capture is complete, the loop continues here
        # (read up on generator functions in Python to understand
        # the yield statement). Here you could do some processing
        # on the image...
        stream.seek(0)
        img = Image.open(stream)
        # img.save(str(i) + '.jpeg')
        # Finally, reset the stream for the next capture
        stream.seek(0)
        stream.truncate()

with picamera.PiCamera() as camera:
    camera.resolution = (480, 360)
    camera.framerate = 60
    camera.start_preview()
    time.sleep(2)
    start = time.time()
    take_num_pics=1000
    camera.capture_sequence(outputs(take_num_pics), 'jpeg', use_video_port=True)
    finish = time.time()
    print('Captured %d images at %.2ffps' % (take_num_pics, take_num_pics / (finish - start)))
