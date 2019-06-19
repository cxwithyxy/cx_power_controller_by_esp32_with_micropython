from machine import Pin
import utime
p4 = Pin(4, Pin.OUT)

while True:
    utime.sleep(3)
    if p4.value() > 0:
        p4.value(0)
    else:
        p4.value(1)

