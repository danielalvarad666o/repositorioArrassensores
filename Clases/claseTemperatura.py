import RPi.GPIO as GPIO
import Adafruit_DHT
import datetime


class SensorTemperaturaHumedad:
      
    def __init__(self, pin):
        
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT11
        super().__init__()
          
    def medir_temperatura_humedad(self, listasensores, lista,tipo):     
         humedad, temperatura = Adafruit_DHT.read(self.sensor, self.pin)
        
         self.temperatura_info = {"Clave": format(lista), "Sensor": tipo, "Value": "Temperatura: {}".format(temperatura), "Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
         listasensores.append(self.temperatura_info)
         self.temperatura_info1 = {"Clave": format(lista), "Sensor": tipo, "Value": "Humedad: {}".format(humedad), "Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
         listasensores.append(self.temperatura_info1)
    
          
            
           
            
       

            
    def infoT(self, lista, listasensores):
        self.info = {"Clave": format(lista), "Tipo": "Temperatura", "Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Pin": self.pin}
        listasensores.append(self.info)
        return self.info

