from tkinter import *
from tkinter.messagebox import *
#from entidades import Persona

class VentanaNuevaPersona():
    def __init__(self, documento, nombre, apellido, edad):
        self.ventana = Tk()
        frameEntrys = Frame(self.ventana, padx=10, pady=10)
        Label(frameEntrys, text="Documento: ", padx=2, pady=3).grid(row=3, column=0)
        self.documento = IntVar(value=documento)
        Entry(frameEntrys, textvariable=self.documento).grid(row=3, column=1, padx=2, pady=3)
        Label(frameEntrys, text="Nombre: ", padx=2, pady=3).grid(row=0, column=0)
        self.nombre = StringVar(value=nombre)
        Entry(frameEntrys, textvariable=self.nombre).grid(row=0, column=1, padx=2, pady=3)
        Label(frameEntrys, text="Apellido: ", padx=2, pady=3).grid(row=1, column=0)
        self.apellido = StringVar(value=apellido)
        Entry(frameEntrys, textvariable=self.apellido).grid(row=1, column=1, padx=2, pady=3)
        Label(frameEntrys, text="Edad: ", padx=2, pady=3).grid(row=2, column=0)
        self.edad = IntVar(value=edad)
        Entry(frameEntrys, textvariable=self.edad).grid(row=2, column=1, padx=2, pady=3)
        frameEntrys.pack()

        frameBotones = Frame(self.ventana, padx=10, pady=8)
        Button(frameBotones, text="Agregar", command=self.aceptar, padx=2).grid(row=4, column=0, padx=10)        
        Button(frameBotones, text="Cancelar", command=self.ventana.destroy, padx=2).grid(row=4, column=1, padx=10)
        frameBotones.pack(side=TOP)

    def mostrar(self):
        self.ventana.mainloop()

    def aceptar(self, ventanaListado):
        persona = 0# Persona(self.nombre, self.apellido, self.documento. self.edad)
        return persona # Agregar aca al padron
