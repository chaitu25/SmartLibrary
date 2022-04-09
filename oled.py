from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# -----------------
#  PIN CONNECTIONS
# -----------------
# | ESP32 | OLED  |
# -----------------
# | 19    | SDA   | 
# | 18    | SCL   |
# | GND   | GND   |
# | 3.3V  | VCC   |
# ----------------- 

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(18), sda=Pin(19))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def _print(msg):
    i, j, x, y = 0, 0, 0, -10
    oled.fill(0)
    while (j < len(msg)):
        i = j
        j += 16
        y += 10
        oled.text(msg[i:j], x, y)
        
def _print(title, msg):
    i, j, x, y = 0, 0, 0, 0
    oled.fill(0)
    oled.text(title, 0, 0)
    while (j < len(msg)):
        i = j
        j += 16
        y += 10
        oled.text(msg[i:j], x, y)
          
          
          
          
          
          
          
          
          
          
          
          
        
