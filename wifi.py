from network import WLAN
from network import STA_IF
import machine
import oled

wlan = WLAN(STA_IF)
wlan.active(True)

def scan():
    wlan.active(True)
    _print(wlan.scan())

def connect(ssid, pw):
    wlan.active(True)
    nets = wlan.scan()
    if(wlan.isconnected()):
        _print('Already connected to "' + wlan.config('essid') + '". Disconnect?')
        ans = input()
        if (ans == "y" or ans == "Y"):
            wlan.disconnect()
        else:
            return
    _print('Connecting to "' + ssid + '" ...')
    wlan.connect(ssid, pw)         
    while not wlan.isconnected():
        try:
            machine.idle() # save power while waiting
        except KeyboardInterrupt:
            _print('Interrupted. Ending ...')
            return
    _print('Connection succeeded!')          
    _print('Connected to :"' + wlan.config('essid') + '"\nifconfig: ' + str(wlan.ifconfig()))
    
def status():
    if(wlan.isconnected()):
        _print('Connected to "' + wlan.config('essid') + '"')
        return 1
    else:
        _print('Not connected')
        return 0
        
def disconnect():
    if (wlan.isconnected()):
        wlan.disconnect()
        _print('Disconnected')
    else:
        _print('Not connected')
        
def _print(msg):
    print('[WLAN]', msg)
    oled._print('[WLAN]', msg)   
    
    
# wifi.connect("VM3827353", "Ywxneps3cxza")
