## Procesamiento de palabras del Quijote

"""
Tomando el texto del libro ["El Quijote de La Mancha"](./quijote.txt) y el [diccionario del idioma inglés](./words_alpha.txt) calcular e informar 
* Cantidad de palabras únicas (sin repetición) del libro. 
* Cantidad de palabras del diccionario.
* Cantidad de palabras del libro que no existen en el diccionario.
* Listado ordenados de todas las palabras que no existen. 
"""
import re

def crear_conjunto_de_palabras_desde_txt(nombre_archivo):
    archivo = open(nombre_archivo)
    conjunto = set()
    for line in archivo.readlines():
        limpia = re.sub("[^a-zA-Z ]", " ", line)
        conjunto.update((limpia.lower().split()))
    
    return conjunto

def mostrar_elementos_conjunto_ordenados(conjunto):
    lista_ordenada = sorted(conjunto)
    for elemento in lista_ordenada:
        print(elemento)

def main():
    quijote = crear_conjunto_de_palabras_desde_txt("./conjuntos/quijote/quijote.txt")
    diccionario = crear_conjunto_de_palabras_desde_txt("./conjuntos/quijote/words_alpha.txt")
    conjunto_no_existe_diccionario = quijote - diccionario
    
    print(len(quijote))
    print(len(diccionario))
    print(len(conjunto_no_existe_diccionario))
    print(sorted(conjunto_no_existe_diccionario)[0:5])
    ##mostrar_elementos_conjunto_ordenados(conjunto_no_existe_diccionario)

    
if __name__=="__main__":
    main()