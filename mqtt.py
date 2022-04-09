from umqtt.robust import MQTTClient
import oled
import machine
import time

CERT_FILE = "cert"
KEY_FILE = "key"
MQTT_CLIENT_ID = ""
MQTT_HOST = "a387fta6uxrpux-ats.iot.us-east-2.amazonaws.com"

MQTT_PORT = 8883

#MQTT_TOPIC = "sdk/test/Python"
#MQTT_TOPIC = "smart-library/book/sub"

mqtt_client = None

def subscription_callback(topic, msg):
    decoder = "utf8"
    led = machine.Pin(27, machine.Pin.OUT)
    i = 0
    while(i < 15):
        led.on()
        time.sleep(1)
        led.off()
        i += 1
    _print("Received: \n\tTopic: " + topic.decode(decoder) + "\n\tMessage: " + msg.decode(decoder))

def publish(topic, msg):
    global mqtt_client
    try:
        _print("Publishing - Topic: " + topic + ", Message: " + msg)
        mqtt_client.publish(topic, msg)
        _print("Published")
    except Exception as e:
        disconnect()
        _print("ERROR Publishing: " + str(e))
        raise
        

def connect():
    global mqtt_client
    try:
        _print("\tREADING Key ... ")
        with open(KEY_FILE, "r") as f: 
            key = f.read()
        _print("\t\tGOT Key")
        
        _print("\tREADING Cert ... ")
        with open(CERT_FILE, "r") as f: 
            cert = f.read()
        _print("\t\tGOT Cert")

        _print("CONNECTING ...")
        mqtt_client = MQTTClient(
            client_id = MQTT_CLIENT_ID,
            server = MQTT_HOST,
            port = MQTT_PORT,
            keepalive = 5000,
            ssl = True,
            ssl_params={
                "cert": cert,
                "key": key,
                "server_side": False
            }
        )
        #mqtt_client.set_callback(subscription_callback)
        mqtt_client.connect()
        _print('CONNECTED')
    except Exception as e:
        _print('ERROR MQTT Connection: ' + str(e))
        raise
    
def set_callback(callback):
    global mqtt_client
    mqtt_client.set_callback(callback)

def disconnect():
    global mqtt_client
    try:
        mqtt_client.disconnect()
        _print("MQTT CLIENT DISCONNECTED")
    except Exception as e:
        _print('ERROR MQTT Disconnection: ' + str(e))
        raise


def subscribe(topic):
    global mqtt_client
    try:
        mqtt_client.subscribe(topic)
        _print("MQTT Subscribed to " + topic)
#         while True:
#             if True:
#                 mqtt_client.wait_msg()
#             else:
#                 mqtt_client.check_msg()
#                 time.sleep(1)
#         disconnect()
    except Exception as e:
        disconnect()
        _print('ERROR MQTT Disconnection: ' + str(e))
        raise
    
def subscribe_checkUpdates():
    global mqtt_client
    try:
#        mqtt_client.subscribe(topic)
#        _print("MQTT Subscribed to " + topic)
#         while True:
         if True:
             mqtt_client.wait_msg()
         else:
             mqtt_client.check_msg()
             time.sleep(1)
#         disconnect()
    except Exception as e:
        disconnect()
        _print('ERROR MQTT Disconnection: ' + str(e))
        raise
    
def _print(msg):
    print('[MQTT]', msg)
    oled._print('[MQTT]', msg)