# SmartLibrary
Firmware code for IoT based Smart Library System.

### Hardware Used
ESP32


## Getting Started with ESP32
### Firmware for ESP32
Download the most recent MicroPython firmware .bin file to load onto the ESP32 device. It can be downloaded from the [MicroPython downloads page](https://micropython.org/download/#esp32).


### Firmware Install
Esptool will be used to copy the firmware
```
pip install esptool
```
Using esptool.py, erase the flash
```
esptool.py --port /dev/ttyUSB0 erase_flash
```
Deploy new firmware
```
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
```
## Source Code
Use integrated development environments like Thonny for development. Thonny also makes file operations easy.

Rename the `main-###.py` files to `main.py` to achieve the respective control flow.
| MAIN File Name | Flow Control |
| --- | --- |
| `main-led.py` | LED |
| `main-rfid.py` | RFID |

### Description about all files
| File | Description |
| - | - |
| `boot.py` | file named `boot.py` is run automatically by ESP32 on start or reset |
| `ibeacon.py` | iBeacon functionality |
| `led_controller.py` | LED light control |
| `mqtt.py` | MQTT Comms. publish and subscribe functionality |
| `oled.py` | OLED screen printing and refresh functionality |
| `rfid.py` | RFID Scanning control |
| `wifi.py` | Connecting to WiFi (SSID and Password to be set in `main.py`) |
