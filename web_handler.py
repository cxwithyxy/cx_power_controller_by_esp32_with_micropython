from microWebSrv import MicroWebSrv

mws = None

def start():
    global mws
    mws = MicroWebSrv(webPath="/")
    mws.Start(threaded=True)
