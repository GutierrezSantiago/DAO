from tkinter import *
from tkinter.messagebox import *

class VentanaSaludo():
    def __init__(self):
        self.ventana = Tk()
        Label(self.ventana, text="Ingrese su nombre").pack()
        self.nombre = StringVar()
        Entry(self.ventana, textvariable=self.nombre).pack()
        Button(self.ventana, text="Saludar", command=self.saludar).pack()

    def saludar(self):
        showinfo("Saludo", f"Hola {self.nombre.get()}")
        self.nombre.set("")

    def mostrar(self):
        self.ventana.mainloop()

if __name__=="__main__":
    ventana = VentanaSaludo()
    ventana.mostrar()