# ESP32 Aerial Camera
This is a modified version of jameszah's [ESP32-CAM-Video-Recorder-junior](https://github.com/jameszah/ESP32-CAM-Video-Recorder-junior). It includes added HTTP methods for changing settings and recording remotely.
***
The file `arduino/sketchbook/ESP32-CAM-Video-Recorder-junior-04a/private_settings.h` is ignored but is necessary for the program to connect to the internet. It should contain personal settings related to WiFi and default picture quality settings as outlined in `settings.h.sample`. Copy and paste that file (but do *not* delete), and rename the newly made file `settings.h` to change your settings there.
***
Included in this repository is a crude Python command line tool for testing the camera remotely. When the camera and server are running, run the Python script, enter your IP address supplied by the camera, then edit settings and record remotely as you see fit. This tool is meant as a proof of concept for further development of remote controlling the camera.
