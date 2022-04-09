from time import sleep_ms
from machine import Pin, SPI
from mfrc522 import MFRC522

# -----------------
#  PIN CONNECTIONS
# -----------------
# | ESP32 | RC522 |
# -----------------
# | 12    | SDA   | 
# | 14    | SCK   |
# | 27    | MOSI  |
# | 26    | MISO  |
# | -     | IRQ   |
# | GND   | GND   |
# | 25    | RST   |
# | 3.3V  | 3.3V  |
# -----------------            

sck = Pin(14, Pin.OUT)
mosi = Pin(27, Pin.OUT)
miso = Pin(26, Pin.OUT)
spi = SPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

sda = Pin(12, Pin.OUT)

def scanOnce():
    rdr = MFRC522(spi, sda)
    uid = ""
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            if uid == previouslyScannedUID:
                return uid
            print_scan_results(uid, raw_uid, tag_type)
            return uid
    return None

def scan(previouslyScannedUID = None):
    try:
        while True:
            rdr = MFRC522(spi, sda)
            uid = ""
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK:
                    uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    if uid == previouslyScannedUID:
                        return uid
                    print_scan_results(uid, raw_uid, tag_type)
                    return uid                    
        return uid                
    except KeyboardInterrupt:
        _print("Keyboard Interrupt. Ending.")
        raise KeyboardInterrupt
        return
    except Exception as e:
        _print("ERROR: " + str(e))

def print_scan_results(uid, raw_uid, tag_type):
    _print("INPUT")
    _print("Tag_type: " + str(tag_type))
    _print("Raw_uid: " + str(raw_uid))
    _print("UID: " + uid)

def _print(msg):
    print('[RFID]', msg)