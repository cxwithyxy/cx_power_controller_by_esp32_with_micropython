from microWebSrv import MicroWebSrv
import charging_handler

mws = None

def start():
    global mws
    mws = MicroWebSrv(webPath="/")
    mws.Start(threaded=True)

def send_ok(httpResponse):
    httpResponse.WriteResponseOk( headers         = None,
                                contentType     = "text/html",
                                contentCharset  = "UTF-8",
                                content         = "ok" )

@MicroWebSrv.route('/power_on')
def handlerFuncGet(httpClient, httpResponse) :
    print("power_on")
    charging_handler.charging_state(1)
    send_ok(httpResponse)

@MicroWebSrv.route('/power_off')
def handlerFuncGet(httpClient, httpResponse) :
    print("power_off")
    charging_handler.charging_state(0)
    send_ok(httpResponse)