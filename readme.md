# ESP32 Aerial Camera
This is a modified version of jameszah's [ESP32-CAM-Video-Recorder-junior](https://github.com/jameszah/ESP32-CAM-Video-Recorder-junior). It includes added HTTP methods for changing settings and recording remotely.
***
### WiFiManager
This project uses a 3rd party library named [WiFiManager](https://github.com/tzapu/WiFiManager/tree/development) that must be installed directly from GitHub. To do so, from the `arduino/sketchbook/libraries` directory, run the following Git command: `git clone -b development https://github.com/tzapu/WiFiManager.git`. 
***
### Connecting the camera to wifi
When the camera first boots up, it will try to connect to the previously saved wifi network. If this fails (either because it has no credentials already saved or the network is unavailable) it will create its own access point that hosts a configuration portal. 
* Connect to the newly created access point (named "{devname} Setup") and in a browser navigate to `192.168.4.1`.
* Enter the desired SSID and password, then save. The camera will then automatically try to connect to the supplied network.

If you want to use the same device to both configure the wifi and act as a mobile hotspot, do the following steps in order:
1. Connect device to "{devname} Setup" network
1. Navigate to `192.168.4.1` in browser
1. Set SSID and password to those that will be found on the hotspot network and save
1. Turn on mobile hotspot with supplied SSID and password
1. Reset camera; camera will automatically connect to hotspot

**!!!** - *Currently there is no way to set/clear the wifi credentials if the camera is already successfully connected to a network. This may be a problem if there is no way to move the camera out of range of the network or to turn off the network long enough to reconfigure the credentials. For now the wifi settings must be cleared programatically and the code recompiled.*
***
### HTTP PUT requests
The following HTTP PUT requests used to configure video settings and record videos. 

**Record**
* Will set the camera to record until the set time has elapsed. Will fail if the camera is already recording.
* URL: `/record`
* No parameters
* Example: `curl -i -X PUT "http://{IP}/record"`

**Configure settings**
* Will change at least one of avi_length, framesize, and quality settings. Will fail if there are no parameters or if the camera is already recording. If any individual parameter is invalid this will be stated in the response but the request will not fail.
* URL: `\config`
* Query parameters:
    * `avilength` - desired video duration in seconds, between 1 and 300 inclusive
    * `framesize` - desired framesize, must be 5, 6, 7, 9, or 10
    * `compression` - desired image compression ('quality' variable in code), between 11 and 63 inclusive
* Example: `curl -i -X PUT "http://{IP}/config?avilength=15&compression=20"`
***
**!!!** - *The Python testing tool currently does not function.*
Included in this repository is a crude Python command line tool for testing the camera remotely. When the camera and server are running, run the Python script, enter your IP address supplied by the camera, then edit settings and record remotely as you see fit. This tool is meant as a proof of concept for further development of remote controlling the camera.
