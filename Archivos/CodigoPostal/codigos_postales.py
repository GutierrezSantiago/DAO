"""
Lectura de códigos postales
El archivo cp.csv contiene el listado de los códigos postales de tres provincias argentinas. En cada línea se encuentran, separados por un símbolo de punto y coma (;) los siguientes datos:

Provincia, representada por una letra mayúscula según el estándar ISO correspondiente.
Código, es un número entero de cuatro dígitos que identifica una localidad o varias localidades vecinas. Puede estar repetido.
Nombre, es el nombre de la localidad correspondiente a ese código.

Se requiere leer todo el contenido del archivo y guardarlo en una lista que contenga un elemento por cada línea. En cada elemento debe almacenarse alguna estructura de datos que permita acceder individualmente a cada dato que conforma un codigo postal.
Luego de la carga el programa debe permitir el ingreso de uno o más códigos numéricos y listar provincia y nombre de todas las localidades asignadas a dichos códigos.
"""

def obtener_iterable(csv):
    lista = []
    for line in csv.readlines():
        datos = line.strip().split(";")
        lista.append(datos)
    return lista

def procesar_archivo(nombre_csv):
    csv = open(nombre_csv)
    lista = obtener_iterable(csv)
    csv.close()
    return lista

def obtener_codigos_a_buscar():
    lista_codigos = []
    while(True):
        codigo = input("Ingrese un codigo postal para agregar al a busqueda\n(-1 para comenzar la busqueda):")
        if (codigo == "-1"): break
        lista_codigos.append(codigo)
    
    return lista_codigos

def buscar_x_codigos(lista_cp, lista_codigos_a_buscar):
    lista_localidades = []
    for cp in lista_cp:
        if (cp[1] in lista_codigos_a_buscar):
            lista_localidades.append(cp)
    return lista_localidades

def mostrar_resultados_busqueda(lista_filtrada):
    contador = 0
    print(f"Número|Provincia|Localidad")
    print(f"-"*40)
    for cp in lista_filtrada:
        contador+=1
        print(f"{contador:^6}|{cp[0]:^9}|{cp[2]}")

def main():
    lista_cp = procesar_archivo("cp.csv")
    lista_codigos_a_buscar = obtener_codigos_a_buscar()
    lista_filtrada = buscar_x_codigos(lista_cp, lista_codigos_a_buscar)
    mostrar_resultados_busqueda(lista_filtrada)

if __name__=="__main__":
    main()

    