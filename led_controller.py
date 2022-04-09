import machine
import time
import _thread as th

led_blink = True

def toggle(led):
    led.value(not led.value())
    return

def setup(pinNo):
    return machine.Pin(pinNo, machine.Pin.OUT)

def blink(led, delay):
    global led_blink
    
    while led_blink:
        led.value(not led.value())
        time.sleep(delay)
    led.off()
        
def blink_times(led, seconds, times, init=False):
    blinkDuration = seconds / times;
    led.value(init)
    for i in range(times):
        toggle(led)
        time.sleep(blinkDuration)
        
def start_blinking(led, delay):
    global led_blink
    
    led_blink = True
    th.start_new_thread(blink, (led, delay,))
    
def stop_blinking():
    global led_blink
    
    led_blink = False
    