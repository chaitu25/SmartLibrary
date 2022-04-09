import wifi
import rfid
import mqtt
import time
import machine
import led_controller as ledc
import oled

MQTT_TOPIC = "smart-library/book/sub"
LED_SUBSCRIPTION_MQTT_TOPIC = "smart-library/user/proximity"

def _print(*args):
    print('\n[MAIN]', end=" ")
    msg = ""
    for y in args:
        print(y, end=" ")
        msg += y + " "
    print()        
    oled._print("[MAIN]", msg)
    
def subscribe(led):
    _print("Scan User Id Card ... ")
    first = rfid.scan()
    _print("SCANNED User:", first)
    led.on()
    _print("Scan Book ... ")
    second = rfid.scan(first)
    while(second == first):
        second = rfid.scan(first)
    _print("SCANNED Book:", second)
    led.off()
    #return {book: str(first), 1: str(second)}
    return '{ "bookId": "' + str(second) + '", "userId": "' + str(1) + '", "action": "subscribe" }'

def connect():
    if wifi.status():
        return
    #wifi.connect("VM3827353", "Ywxneps3cxza")
    wifi.connect("iPhone", "12345678")
    #wifi.connect("CiaraHotspot", "0b3b53def233")
    
def main():
    _print("INIT ... 2")
    led = ledc.setup(16)
    led.on()
    
    _print("Checking internet connection ...")
    connect()
    
    _print("Connecting with MQTT broker ...")
    mqtt.connect()
    led.off()
    
    while True:
        try:
            led.off()
            mqtt.publish(MQTT_TOPIC, str(subscribe(led)))
        except KeyboardInterrupt:
            mqtt.disconnect()
            led.off()
            return
        else:
            _print("PAUSE")
            ledc.blink_times(led, 5, 50)
            _print("RESUME")

main()