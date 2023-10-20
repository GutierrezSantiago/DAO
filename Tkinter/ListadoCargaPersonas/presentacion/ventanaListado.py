from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from entidades import *
from ventanaNuevaPersona import VentanaNuevaPersona

class VentanaListado():
    def __init__(self, padron: Padron):
        self.ventana = Tk()
        frameGrilla = Frame(self.ventana, padx=10, pady=10)

        arbol = ttk.Treeview(frameGrilla)
        arbol["columns"] = ("documento","nombre","apellido","edad")
        arbol.column("documento", width=50, anchor=CENTER)
        arbol.column("nombre", width=100, anchor=CENTER)
        arbol.column("apellido", width=100, anchor=CENTER)
        arbol.column("edad", width=100, anchor=CENTER)
        
        arbol.heading("documento", text="Documento")
        arbol.heading("nombre", text="Nombre")
        arbol.heading("apellido", text="Apellido")
        arbol.heading("edad", text="Edad")
        
        for persona in padron.personas.values():
            arbol.insert('', END, values=(persona.documento, persona.nombre, persona.apellido, persona.edad))
        
        arbol['show'] = 'headings'
        scrollbar = ttk.Scrollbar(frameGrilla, orient="vertical", command=arbol.yview)
        arbol.configure(yscrollcommand=scrollbar.set)
        arbol.pack(side="left")
        scrollbar.pack(side="right", fill="y")
        
        frameGrilla.pack()

        frameBotonesABM = Frame(self.ventana, padx=10, pady=4)
        Button(frameBotonesABM, text="Agregar", width=9, command=self.agregar, padx=2).grid(row=0, column=0, padx=10)        
        Button(frameBotonesABM, text="Editar", width=9, command=self.editar, padx=2).grid(row=0, column=1, padx=10)
        Button(frameBotonesABM, text="Eliminar", width=9, command=self.eliminar, padx=2).grid(row=0, column=3, padx=10)
        frameBotonesABM.pack()

        frameBotonesEstadisticas = Frame(self.ventana, padx=10, pady=4)
        Button(frameBotonesEstadisticas, width=38, text="Cantidad de Personas", command=self.padron.cantidad, padx=2, pady=1).grid(row=0, column=0, padx=10, pady=5)
        Button(frameBotonesEstadisticas, width=38, text="Cantidad de Mayores de Edad", command=self.cantidadMayores, padx=2, pady=1).grid(row=1, column=0, padx=10, pady=5)
        Button(frameBotonesEstadisticas, width=38, text="Cantidad de Personas por Apellido", command=self.cantidadPersonasXApellido, padx=2, pady=1).grid(row=2, column=0, padx=10, pady=5)
        Button(frameBotonesEstadisticas, width=38, text="Personas cuyo nombre o apellido inicia con vocal", command=self.cantidadVocal, padx=2, pady=1).grid(row=3, column=0, padx=10, pady=5)
        frameBotonesEstadisticas.pack()
    
    def mostrar(self):
        self.ventana.mainloop()

    def aceptar(self):
        pass # Eliminar

    def agregar(self):
        pass

    def editar(self):
        pass

    def eliminar(self):
        pass

    # HACER METODOS QUE CONSULTEN AL PADRON Y LO DEVUELVAN MEDIANTE MESSAGEBOX, CAMBIAR LOS COMMAND
    # VER COMO EDITAR (TRAER UN REGISTRO ESPECIFICO) -> SACAR DNI Y ACCEDER EN EL DICCIONARIO