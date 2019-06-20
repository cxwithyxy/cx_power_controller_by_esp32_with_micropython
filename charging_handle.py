from machine import Pin

def charging_state(key = None):
    p4 = Pin(4, Pin.OUT)
    if key is None:
        return p4.value()
    else:
        p4.value(key)
 
def switch_charging_state():
    if charging_state() > 0:
        charging_state(0)
    else:
        charging_state(1)