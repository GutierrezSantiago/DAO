
## Listado de personas

"""
Desarrollar un programa que lea el archivo personas.csv y permita realizar una busqueda por apellido.
El archivo posee separados por comas el documento, nombre, apellido y edad de un padrÃ³n de personas.
El programa debe leer el archivo y sin almacenarlo en niguna estructura de datos listar nombre y edad de todas las personas cuyo apellido coincida con el ingresado por el usuario.
"""


def mostrar_x_apellido(apellido, archivo):
    existe = False
    contador = 0
    for linea in archivo.readlines():
        datos = linea.strip().split(",")
        if datos[2] == apellido.upper():
            existe = True
            contador += 1
            print(f"{contador} - Nombre: {datos[1]} - Edad: {datos[3]}")
    if existe == False:
        print(f"No se encontro el apellido {apellido}")

def main():
    apellido = input("Ingrese un apellido:")
    archivo = open("personas.csv")
    mostrar_x_apellido(apellido, archivo)
    archivo.close()

if __name__=="__main__":
    main()