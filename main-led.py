import wifi
import mqtt
import time
import machine

MQTT_TOPIC = "sdk/test/Python"
LED_SUBSCRIPTION_MQTT_TOPIC = "smart-library/user/proximity"

def _print(*args):
    print('\n[MAIN]', end=" ")
    msg = ""
    for y in args:
        print(y, end=" ")
        msg += y + " "
    print()        
    #oled._print("[MAIN]", msg)

def connect():
    if wifi.status():
        return
    #wifi.connect("VM3827353", "Ywxneps3cxza")
    wifi.connect("iPhone", "12345678")
    #wifi.connect("CiaraHotspot", "0b3b53def233")
    
def mqtt_callback(topic, msg):
    decoder = "utf8"
    led = machine.Pin(14, machine.Pin.OUT)
    i = 0
    while(i < 15):
        led.on()
        time.sleep(1)
        led.off()
        i += 1
    _print("Received: \n\tTopic: " + topic.decode(decoder) + "\n\tMessage: " + msg.decode(decoder))
    
def main():
    led = machine.Pin(14, machine.Pin.OUT)
    led.on()
    _print("INIT ... ")
    
    _print("Checking internet connection ...")
    connect()
    
    _print("Connecting with MQTT broker ...")
    mqtt.connect()
    
    mqtt.set_callback(mqtt_callback)
    mqtt.subscribe(LED_SUBSCRIPTION_MQTT_TOPIC)
    led.off()

    while True:
        mqtt.subscribe_checkUpdates()
        
main()