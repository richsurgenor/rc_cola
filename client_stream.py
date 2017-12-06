import io
import socket
import struct
import time
import picamera

client_socket = socket.socket()
client_socket.connect(('0.0.0.0', 8160))

connection = client_socket.makefile('wb')
try:
	with picamera.PiCamera() as camera:
		camera.resolution = (640, 480)
		camera.start_preview()
		# let cam warm up(or not)
		time.sleep(2)

		start = time.time()
		stream = io.BytesIO()
		for foo in camera.capture_continuous(stream, 'jpeg'):
			connection.write(struct.pack('<L', stream.tell()))
			connection.flush()
			# Send image data
			stream.seek(0)
			connection.write(stream.read())

			# Reset stream for next capture
			stream.seek(0)
			stream.truncate()

		connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()
