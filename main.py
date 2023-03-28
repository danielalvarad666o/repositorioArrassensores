from Menu import claseMenu
from Interface import InterfacedelasClases
from Clases import claseClaves
cla=claseClaves.Claves()

cla.crearclaves(3)
lainterface=InterfacedelasClases.interface()
elmenu=claseMenu.Menus()


option=0

while option !=3:
    option=elmenu.Optiones()
    if option==1:
        lainterface.verinfosensores()
    
    elif option ==2:
        lainterface.sensoresFuncion()
