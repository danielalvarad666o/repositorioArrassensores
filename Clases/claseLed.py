import datetime
import RPi.GPIO as GPIO
import time
from ClaseLista import lista

class Led(lista.Lista):
    def __init__(self,pin) -> None:
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        super().__init__()
        
    def encender(self,listasensores,lista,tipo):
        GPIO.output(self.pin, GPIO.HIGH)        
        self.info_led={"Clave":format(lista),"Sensor":tipo,"Value":"On","Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        listasensores.append(self.info_led)
        
        
    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)

        
    def parpadear(self, repeticiones:int):
        for i in range(repeticiones):
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(1)  # espera 1 segundo
            GPIO.output(self.pin, GPIO.LOW)
            time.sleep(1)  # espera 1 segundo
    def infoled(self,lista,listasensores):
        self.info={"Clave":format(lista),"Tipo":"LED","Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"Pin":self.pin}
        listasensores.append(self.info)
        return self.info
        
            