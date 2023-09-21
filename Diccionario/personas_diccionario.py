## Padrón de personas
"""
El archivo [personas.csv](./personas.csv) contiene un padrón de personas a razón de una persona por línea y en cada una separadas con comas el documento, nombre, apellido y edad.
Desarrollar un programa en python que lea el archivo y guarde todo su contenido en un diccionario indexado por documento. Luego el programa debe ofrecer un menú con las siguientes opciones:
* Búsqueda por documento: que solicite un documento y si lo encuentra muestre todos los datos de la persona encontrada y un mensaje adecuado si no la encuentra.
* Búsqueda por apellido: que solicite un apellido y muestre por pantalla todos los datos de todas las personas cuyo apellido sea igual al ingresado. 
* Mostrar el promedio de edades de todos.
"""



def cargar_diccionario(path):
    archivo = open(path)
    diccionario = dict()
    for line in archivo.readlines():
        datos = (line.strip().split(","))
        diccionario[datos[0]] = datos[1:]
        
    return diccionario

def calcular_promedio_edades(diccionario):
    ac, contador = 0, 0
    for v in diccionario.values():
        ac += int(v[2])
        contador += 1
    
    return ac/contador

def buscar_por_documento(diccionario):
    documento = input("Ingrese un documento a buscar: ")
    for k, v in diccionario.items():
        if documento == k:
            return f"DNI: {k} - Nombre: {v[0]} - Apellido: {v[1]} - Edad: {v[2]}"

    return f"No se encontro ninguna persona con el DNI: {documento}"

def buscar_por_apellido(diccionario):
    apellido = input("Ingrese un apellido a buscar: ")
    existe = False
    
    for k, v in diccionario.items():
        if v[1] == apellido.upper():
            existe = True
            print(f"DNI: {k} - Nombre: {v[0]} - Apellido: {v[1]} - Edad: {v[2]}")
    
    if existe == False:
        print(f"No se encontro ningun persona con el apellido: {apellido}")
    
def main():
    diccionario = cargar_diccionario("./diccionarios/personas/personas.csv")
    buscar_doc = buscar_por_documento(diccionario)
    print(buscar_doc)
    print()
    buscar_por_apellido(diccionario)
    print()
    print(f"Promedio de edades: {calcular_promedio_edades(diccionario)}")
    
if __name__=="__main__":
    main()