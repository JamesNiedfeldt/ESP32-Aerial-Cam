# ESP32 Aerial Camera
This is a modified version of jameszah's [ESP32-CAM-Video-Recorder](https://github.com/jameszah/ESP32-CAM-Video-Recorder). I am still working on getting everything working properly with Git and Arduino IDE and will update this readme as I organize code and figure things out.
***
Currently libraries and packages are not included in any form. By loading the contents of `arduino/` into Arduino Portable's `portable/` folder, necessary libraries should be found and installed by Arduino IDE.
***
The file `arduino/sketchbook/TimelapseAvi94x/private_settings.h` is ignored but is necessary for the program to connect to the internet. It should contain personal settings related to WiFi as outlined in `private_settings.h.sample`. Copy and paste that file (but do *not* delete), and rename the newly made file `private_settings.h` to change your settings there.
