"""

## Personas

Programar una clase Persona con atributos suficientes para almacenar documento, nombre,
apellido y edad de una persona. 

Crear un programa que permita ingresar los
datos de algunas personas por teclado y con esos datos cree instancias 
sin guardarlas en una estructura de datos y muestre por pantalla el estado de las mismas.

Al finalizar la carga el programa debe mostrar los datos de la persona de menor edad.

"""

from persona import Persona

def solicitarDatosPersona():
    nombre = input("Ingrese un nombre: ")
    apellido = input("Ingrese un apellido: ")
    documento = input("Ingrese un documento: ")
    edad = int(input("Ingrese una edad: "))
    return Persona(nombre, apellido, documento, edad)

def main():
    menor = None
    carga = ""
    while (True):
        carga = input("Si desea cargar una persona presiona enter, sino ingrese -1...")
        if carga == "-1":
            break
        persona = solicitarDatosPersona()
        print(persona)
        
        if (menor == None or menor.edad > persona.edad):
            menor = persona
    if (menor != None):
        print("La persona con menor edad fue:")
        print(menor)

if __name__=="__main__":
    main()