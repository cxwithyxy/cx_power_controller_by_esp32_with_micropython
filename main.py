import wifi_handler
import charging_handler
import web_handler


wifi_handler.connect()
web_handler.start()

print("===== system ready =====")
