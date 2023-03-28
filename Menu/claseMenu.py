class Menus:    
    def Optiones(self):
     try:
        
        print("1)Info sensores")
        print("2)Ver Sensores")
        
        
        print("3)Salir")
        print("")
        option =int(input("Escoje una opcion: "))
        return option
     except:
         return "Opcion no valida intenta de nuevo"
        