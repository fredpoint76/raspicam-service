#!/usr/bin/env python3
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
import sys
import os
import io
import signal


def signal_handler(sig, frame):
    print('Received CTRL+C, exiting...')
    picam2.stop_encoder()
    picam2.stop()
    sys.exit(0)

picam2=Picamera2()
config = picam2.create_video_configuration(main={'size': (640, 480), 'format':'XBGR8888'}, raw={'size': (1640,1232)
}, buffer_count=4)
picam2.configure(config)

#FIXME: bitrate shall be configurable
encoder = H264Encoder(bitrate=2000000, repeat=True, iperiod=7, framerate=30)
output = FileOutput('/dev/stdout')
picam2.start_recording(encoder, output)

print('starting stream')
picam2.start()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
signal.pause()

