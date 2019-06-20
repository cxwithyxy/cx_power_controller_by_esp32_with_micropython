from machine import Pin
import utime
import microWebSrv
import wifi_handler
from microWebSrv import MicroWebSrv

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

# while True:
#     utime.sleep(3)
#     switch_charging_state()

wifi_handler.connect()
# wifi_handler.get_ip()
mws = MicroWebSrv(webPath="/")
mws.Start(threaded=True)
print("===== system ready =====")
