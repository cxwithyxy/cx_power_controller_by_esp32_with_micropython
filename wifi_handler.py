import network

wlan = network.WLAN(network.STA_IF)

def read_wifi_json():
    wifi = file_tools.read_json("wifi.json")
    return wifi["ssid"], wifi["password"]

def connect():
    global wlan
    if not wlan.isconnected():
        ssid, password = read_wifi_json()
        wlan.active(True)
        wlan.connect(ssid, password)

def get_ip():
    return wlan.ifconfig()


# wlan.scan()
# wlan.isconnected()
# wlan.config('mac')