from ClaseLista import lista
import random

class Claves(lista.Lista):
    
    
    def __init__(self):
        super().__init__()
        
    def crearclaves(self,cantidad):
         
         while len(self.lista) < cantidad:
          clave = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))
          if clave not in self.lista:
            self.lista.append(clave)
            super().crearjson(self.lista,"Claves")
         return self.lista
     
     
     

