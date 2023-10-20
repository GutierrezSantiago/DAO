def cargarRutasModulos():
    import os, sys

    rutaDirectorio = os.path.dirname(os.path.abspath(__file__))
    listadoDirectorios = []

    items = os.listdir(rutaDirectorio)

    for item in items:
        rutaItem = os.path.join(rutaDirectorio, item)  
        if os.path.isdir(rutaItem):
            sys.path.append(rutaItem)

cargarRutasModulos()

from entidades import *
from persistencia import *
from presentacion import *

def inicializar():
    lectorCSV = lectorCSVPersonas("./resources/personas.csv")
    personas =  lectorCSV.cargarDiccionario()
    padron = Padron(personas)
    
    ventana = VentanaListado(padron)
    ventana.mostrar()


            

if __name__=="__main__":
    inicializar()
    