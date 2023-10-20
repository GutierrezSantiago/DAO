from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from entidades import *
from ventanaNuevaPersona import VentanaNuevaPersona

class VentanaListado():
    def __init__(self, padron: Padron):
        self.padron = padron

        self.ventana = Tk()
        frameGrilla = Frame(self.ventana, padx=10, pady=10)

        self.arbol = ttk.Treeview(frameGrilla)
        self.arbol["columns"] = ("documento","nombre","apellido","edad")
        self.arbol.column("documento", width=50, anchor=CENTER)
        self.arbol.column("nombre", width=100, anchor=CENTER)
        self.arbol.column("apellido", width=100, anchor=CENTER)
        self.arbol.column("edad", width=100, anchor=CENTER)
        
        self.arbol.heading("documento", text="Documento")
        self.arbol.heading("nombre", text="Nombre")
        self.arbol.heading("apellido", text="Apellido")
        self.arbol.heading("edad", text="Edad")
        
        for persona in padron.personas.values():
            self.arbol.insert('', END, values=(persona.documento, persona.nombre, persona.apellido, persona.edad))
        
        self.arbol['show'] = 'headings'
        scrollbar = ttk.Scrollbar(frameGrilla, orient="vertical", command=self.arbol.yview)
        self.arbol.configure(yscrollcommand=scrollbar.set)
        self.arbol.pack(side="left")
        scrollbar.pack(side="right", fill="y")
        
        frameGrilla.pack()

        frameBotonesABM = Frame(self.ventana, padx=10, pady=4)
        Button(frameBotonesABM, text="Agregar", width=9, command=self.agregar, padx=2).grid(row=0, column=0, padx=10)        
        Button(frameBotonesABM, text="Editar", width=9, command=self.editar, padx=2).grid(row=0, column=1, padx=10)
        Button(frameBotonesABM, text="Eliminar", width=9, command=self.eliminar, padx=2).grid(row=0, column=3, padx=10)
        frameBotonesABM.pack()

        frameBotonesEstadisticas = Frame(self.ventana, padx=10, pady=4)
        Button(frameBotonesEstadisticas, width=38, text="Cantidad de Personas", command=self.agregar, padx=2, pady=1).grid(row=0, column=0, padx=10, pady=5)
        Button(frameBotonesEstadisticas, width=38, text="Cantidad de Mayores de Edad", command=self.agregar, padx=2, pady=1).grid(row=1, column=0, padx=10, pady=5)
        Button(frameBotonesEstadisticas, width=38, text="Cantidad de Personas por Apellido", command=self.agregar, padx=2, pady=1).grid(row=2, column=0, padx=10, pady=5)
        Button(frameBotonesEstadisticas, width=38, text="Personas cuyo nombre o apellido inicia con vocal", command=self.agregar, padx=2, pady=1).grid(row=3, column=0, padx=10, pady=5)
        frameBotonesEstadisticas.pack()
        
    def mostrar(self):
        self.ventana.mainloop()

    def validacionSeleccionInvalida(self):
        invalido = self.arbol.focus() == ""
        if (invalido): showerror(title="Error de selección", message="No hay ningun registro seleccionado.")
        return invalido
    
    def agregar(self):
        ventanaAgregar = VentanaNuevaPersona(0, "", "", 0)

    def editar(self):
        if self.validacionSeleccionInvalida(): return
        indiceSeleccionado = self.arbol.focus()
        valoresRegistro = self.arbol.item(indiceSeleccionado).get("values")
        documento = valoresRegistro[0]
        nombre = valoresRegistro[1]
        apellido = valoresRegistro[2]
        edad = valoresRegistro[3]
        print(f"{documento} {nombre} {apellido} {edad}")
        ventanaEditar = VentanaNuevaPersona(0, nombre, apellido, edad) # PREGUNTAR PROFE PORQUE NO FUNCIONA CUANDO TEST SOLO SI
        ventanaEditar.mostrar()

    def eliminar(self):
        if self.validacionSeleccionInvalida(): return
        indiceSeleccionado = self.arbol.focus()
        valoresRegistro = self.arbol.item(indiceSeleccionado).get("values")
        documento = valoresRegistro[0]
        self.padron.eliminarPorDocumento(int(documento)) # ACA SE PODRIA USAR POP PARA DEVOLVER EL VALOR E INFORMAR LOS DATOS DE LA PERSONA ELIMINADA
        self.arbol.delete(indiceSeleccionado)



    # HACER METODOS QUE CONSULTEN AL PADRON Y LO DEVUELVAN MEDIANTE MESSAGEBOX, CAMBIAR LOS COMMAND
    # VER COMO EDITAR (TRAER UN REGISTRO ESPECIFICO) -> SACAR DNI Y ACCEDER EN EL DICCIONARIO