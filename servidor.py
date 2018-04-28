import tornado.ioloop
import tornado.web

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class GetECG(tornado.web.RequestHandler):
    def get(self):
        ecg = []
        print("Iniciando captura de ECG...")
        for i in range(10000):
            valor = mcp.read_adc(4)
            ecg.append(valor)
            print str(len(ecg)) + " - " + str(valor) 
            time.sleep(0.0001)
        print("Captura de ECG finalizada!")
        self.write({'valor':ecg})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ecg", GetECG),
    ])

if __name__ == "__main__":
    print("Server iniciado...")
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()