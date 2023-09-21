"""
## Personas (desde archivo)

Programar una clase Persona con atributos suficientes para almacenar documento, nombre,
apellido y edad de una persona.
Crear un programa que lea el archivo personas.csv, cree una instancia de Persona
por cada línea del archivo y guarde todas las instancias en un diccionario indexado por documento.

A continuación, desde el diccionario informe:

* Cantidad de personas cargadas
* Cantidad de personas mayores de edad
* Listado de nombres y apellidos de aquellas personas cuyo apellido empiece en vocal
* Cantidad de personas por cada apellido


"""

from persona import Persona

def cargarDiccionario(ruta_archivo):
    archivo = open(ruta_archivo, "r")
    personas = dict()
    for linea in archivo.readlines():
        linea = linea.strip().split(",")
        persona = Persona(linea[1], linea[2], linea[0], int(linea[3]))
        personas[persona.documento] = persona
    
    archivo.close()
    return personas

def obtenerCantidadesPorApellidos(personas):
    cant_ape = dict()
    for p in personas.values():
        if p.apellido in cant_ape:
            cant_ape[p.apellido] += 1
        else:
            cant_ape[p.apellido] = 1
    
    return cant_ape

def main():
    personas = cargarDiccionario("personas.csv")
    cantidad = len(personas)
    cantidadMayor = len(list(filter(lambda persona: persona.esMayor() , personas.values())))
    print()
    personasIniciaVocal = map(lambda persona: f"Nombre: {persona.nombre} - Apellido: {persona.apellido}" ,list(filter(lambda persona: persona.tieneApellidoVocal() ,personas.values())))
    
    print(f"Cantidad de personas: {cantidad}")
    print(f"Cantidad de personas: {cantidadMayor}")
    print("Listado de nombre y apellido de personas cuyo apellido comienza con vocal:")
    for nombreApellido in personasIniciaVocal:
        print (nombreApellido)
    cant_ape = obtenerCantidadesPorApellidos(personas)
    print("Cantidad de personas por apellido:")
    for k, v in cant_ape.items():
        print(f"Apellido: {k} Cantidad: {v}")
    
        
if __name__=="__main__":
    main()
    