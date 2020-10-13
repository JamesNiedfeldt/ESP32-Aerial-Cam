# ESP32 Aerial Camera
This is a modified version of jameszah's [ESP32-CAM-Video-Recorder-junior](https://github.com/jameszah/ESP32-CAM-Video-Recorder-junior). It includes added HTTP methods for changing settings and recording remotely.
***
### WiFiManager
This project uses a 3rd party library named [WiFiManager](https://github.com/tzapu/WiFiManager/tree/development) that must be installed directly from GitHub. To do so, from the `arduino/sketchbook/libraries` directory, run the following Git command: `git clone -b development https://github.com/tzapu/WiFiManager.git`. 
***
### Connecting the camera to wifi
When the camera first boots up, it will try to connect to the previously saved wifi network. If this fails (either because it has no credentials already saved or the network is unavailable) it will create its own access point that hosts a configuration portal. 
* Connect to the newly created access point (named after the device's `devname`) and in a browser navigate to `192.168.4.1`.
* Enter the desired SSID and password, then save. The camera will then automatically try to connect to the supplied network.

If you want to use the same device to both configure the wifi and act as a mobile hotspot, first connect to the camera's AP to configure wifi, then turn on the hotspot and restart the camera. At that point it should connect automatically.
***
Included in this repository is a crude Python command line tool for testing the camera remotely. When the camera and server are running, run the Python script, enter your IP address supplied by the camera, then edit settings and record remotely as you see fit. This tool is meant as a proof of concept for further development of remote controlling the camera.
