from machine import Timer
from machine import Pin, Timer, SoftI2C
from time import sleep_ms
import ubluetooth
from esp32 import raw_temperature
import struct

class Beacon:
    UUID = 'e5447d13-bdf7-4a42-aee3-0c8a51192f52'
    MANUFACTURER_ID = const(0x004C)
    DEVICE_TYPE = const(0x02)
    DATA_LENGTH = const(0x15)
    BR_EDR_NOT_SUPPORTED = const(0x04)
    FLAG_BROADCAST = const(0x01)
    MANUFACTURER_DATA = const(0xFF)

    def __init__(self,name,major,minor,tx_power):
        self.name = name
        self.ble = ubluetooth.BLE()
        self.ble.active(False)
        self.ble.active(True)
        print('BLE Activated')
        self.uuid = bytearray((
                        0xa4, 0x95, 0xbb, 0x10, 0xc5, 0xb1, 0x4b, 0x44, 
                        0xb5, 0x12, 0x13, 0x70, 0xf0, 0x2d, 0x74, 0xde
                    ))
        self.major = major
        self.minor = minor
        self.tx_power = 0xFF + 1 + tx_power
        self.payload = self.createPayload()
    
    def createPayload(self):
        payload = bytearray()
                #Set advertising flag
        value    = struct.pack('B', BR_EDR_NOT_SUPPORTED)
        payload += struct.pack('BB', len(value) + 1, FLAG_BROADCAST) + value

        # Set advertising data
        value    = struct.pack('<H2B', MANUFACTURER_ID, DEVICE_TYPE, DATA_LENGTH) 
        value   += self.uuid
        #value += bytes(self.name,'UTF-8')
        value   += struct.pack(">2HB", self.major, self.minor, self.tx_power)
        payload += struct.pack('BB', len(value) + 1, MANUFACTURER_DATA) + value
        return payload
    
    def advertise(self,interval=100000):
        print('Advertising data',str(self.payload))
        self.ble.gap_advertise(None)
        self.ble.gap_advertise(interval_us = interval, adv_data=self.payload, connectable=False)
    
def startBeacon():
    beacon = Beacon('Beacon 1',100,1001,-50)
    beacon.advertise()

if __name__ == '__main__':
    startBeacon()
    while(True):
        pass