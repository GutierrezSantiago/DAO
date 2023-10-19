from VentanaNuevaPersona import *
from VentanaListado import *
from padron import *
from persona import Persona
from lectorCSVPersonas import lectorCSVPersonas

def main():
    lectorCSV = lectorCSVPersonas("./resources/personas.csv")
    personas =  lectorCSV.cargarDiccionario()
    padron = Padron(personas)
    

if __name__="__main__":
    main()