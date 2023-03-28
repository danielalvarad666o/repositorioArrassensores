import json
import os
from Clases import claseLed,claseUltrasonico,claseTemperatura,claseClaves
from Mongoclass import mongo
import time

#------------------------------------
#
#
#
#Inicializadores
cla=claseClaves.Claves()

led=claseLed.Led(21)
sensorU = claseUltrasonico.SensorUltrasónico(trigger_pin=18, echo_pin=24)
sensorT= claseTemperatura.SensorTemperaturaHumedad(5)
conec=mongo.MongoDBClient("mongodb+srv://root:2tCVgy$_DEa!ZYB@5b.y2llyqd.mongodb.net/test")



#----------------------------------------


class interface:
    
    def __init__(self) -> None:
      self.lista1=[]
      self.lista=[]
      self.listadesensores=[]
      
      with open("Claves.json", "r") as f:
         self.lista = json.load(f)
      led.infoled(self.lista[0],self.listadesensores)
      sensorT.infoT(self.lista[1],self.listadesensores)
      sensorU.infoU(self.lista[2],self.listadesensores)
      with open('sensoresInfo.json','w') as file:
              json.dump(self.listadesensores,file,indent=5)

    
    
    
    def sensoresFuncion(self) -> None:
     conecciondesesnores=conec.connect() 
     
     i = 0
     with open("Claves.json", "r") as f:
         self.lista = json.load(f)
     while True:
        
         led.encender(self.lista1, self.lista[0],self.listadesensores[0])
         sensorT.medir_temperatura_humedad(self.lista1, self.lista[1],self.listadesensores[1])
         
         sensorU.medir_distancia(self.lista1, self.lista[2],self.listadesensores[2])
     
         
         
         
         if conecciondesesnores:
          if os.path.exists("Temporal.json"):
            with open("Temporal.json", "r") as f:
                self.lista3 = json.load(f)
            conec.update_all_documents("Arras","Sensores",self.lista3)
            
            
            os.remove("Temporal.json")
          with open('sensores.json','w') as file:
            json.dump(self.lista1,file,indent=5)
          
          conec.update_all_documents("Arras","Sensores",self.lista1)
       
          
         
         
          for sesnor in self.lista1:
              print("------------------------------Tabla-------------------------------------------------------")
              print()
              print("Clave: " ,format( sesnor["Clave"])+"\t ||Sensor: ",format( sesnor["Sensor"])+"\t ||Value: ",format( sesnor["Value"])+"\t || Fecha: ",format( sesnor["Fecha"]))
          print()
          print("_"*100)
          self.lista1 = []
          led.apagar()
          time.sleep(5)
          i=1+i
          if i==3:
           respuesta = input("¿Desea continuar? (s/n): ")
           if respuesta.lower() == "n":
                 break  # Detiene el bucle infinito
         else: 
             with open('Temporal.json','w') as file:
              json.dump(self.lista1,file,indent=5)
             for sesnor in self.lista1:
              print("------------------------------Tabla-------------------------------------------------------")
              print()
              print("Clave: ",format( sesnor["Clave"])+"\t ||Sensor: ",format( sesnor["Sensor"])+"\t ||Value: ",format( sesnor["Value"])+"\t || Fecha: ",format( sesnor["Fecha"]))
             
             led.apagar()
             time.sleep(5)
             i=i+1
             if i==3:
              respuesta = input("¿Desea continuar? (s/n): ")
              if respuesta.lower() == "n":
                  break  # Detiene el bucle infinito
          
    
    
    def jugarconed(self):
          conecciondesesnores=conec.connect() 
          
          i = 0
          with open("Claves.json", "r") as f:
           self.lista = json.load(f)
           
          print("1)Prender led")
          print("2)Parpadiar led")
          print("3)Apagar led")
          
          try: 
            opt=int(input("Escoje una opction "))
            if opt==1:
              led.encender(self.lista1,self.lista[0])
            elif opt==2:
              led.parpadear(9)
            elif opt ==3:
              led.apagar()
              
          except:
            print("Option no valida ")
        
    def verinfosensores(self):
       
      
      
       
       
      
         
       
      
      
       cantidad=len(self.listadesensores)
       for sesnor in self.listadesensores:
         print("Clave: " ,format( sesnor["Clave"])+"\t Tipo: ",format( sesnor["Tipo"])+"\t Fecha: ",format( sesnor["Fecha"])+"\t Pin:",format(sesnor["Pin"]))
       
       print("_"*100)
       print("Cantidad de sensores: " + str( cantidad))
       self.listadesensores.clear()
       print()
         
      
       
       
         
       
       
      
        
    
          
        