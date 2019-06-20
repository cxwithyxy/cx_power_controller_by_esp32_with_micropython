import wifi_handler
import charging_handle
from microWebSrv import MicroWebSrv

wifi_handler.connect()

mws = MicroWebSrv(webPath="/")
mws.Start(threaded=True)
print("===== system ready =====")
