# NeoPixel App
Python server &amp; web color picker for controlling NeoPixel light strip.

## About the project
This project started as a strip of 3x [Adafruit NeoPixel RGB Strips](https://www.amazon.com/Adafruit-NeoPixel-Digital-RGB-Strip/dp/B00XQN3AF0/ref=sr_1_8?keywords=neopixel&qid=1647930039&sr=8-8)
soldered into a Raspberry Pi Zero W and mounted to my desk. 

AdaFruit provides a nice Python library for controlling the strips and after fiddling around writing some scripts
to change color, I decided I'd like a simple web dashboard with a color picker to easily set the strip colors.

### Usage
*(optional)* Configure the port in `server.py`

`sudo python3 /path/to/server.py`

**Note: you must run server with `sudo` as it is required by the Adafruit library!**

Visit `<ip.of.raspberry.pi>:3001`

*(optional)* Create `systemd` service to run server as daemon
```[Unit]
Description=Python server for NeoPixel lights
After=network-online.target

[Service]
Type=simple
Restart=always
# note: configure path to server
ExecStart=/usr/bin/python3 /home/pi/neopixel-app/server.py

[Install]
WantedBy=multi-user.target
```




![color picker](https://user-images.githubusercontent.com/14096584/159421904-a9145640-96ff-4026-8342-33dff1e27005.PNG)
