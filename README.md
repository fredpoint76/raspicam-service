# raspicam-service

## PROJECT
Set of tools and systemd service to stream a local camera to a server in RSTP.

## INSTALL
Deploy init script in systemd appropriate directory and the python script in /usr/bin.

Create user streamcam and add it to the video group:
```
sudo useradd streamcam
sudo usermod streamcam -G video
```

Then finish the install in systemd for rpicam-vid camera setup (legacy pi camera):
```
sudo systemctl daemon-reload
sudo systemctl start streamcam-rpicam-vid
```

Or for camera supported by Pycamera2 project (https://github.com/raspberrypi/picamera2)
```
sudo systemctl daemon-reload
sudo systemctl start streamcam-pycamera2
```

## USAGE
The RSTP port is for now set on 8554. The port is set in the "streamcam-cvlc.service" file.

## CONFIGURATION
N/A
