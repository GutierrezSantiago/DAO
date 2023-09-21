"""
Generar 1000 números enteros al azar entre -1000000 y 1000000. Investigar cómo generar los números con un flujo en lugar de un ciclo for
Informar:

El menor de todos.
La cantidad de pares.
El promedio de los impares.
El cuadrado de todos los que se encuentren entre 10 y 100 sin incluirlos
Los múltiplos de 3 del punto anterior (los multiplos de 3 de los cuadrados calculados)
Todos los múltiplos de 7 ordenados en forma descendente.
El promedio de los impares negativos.
La desviación estandar de todos.
Si existe o no algún múltiplo de 127.
Generar una lista que contenga únicamente los que terminan en 2 o 3.
"""
from random import randint
from functools import reduce
import math

def generar_numeros(n):
    return [randint(-1000000, 1000000) for i in range(n)]

def menor_no_lambda(a, b):
    if (a<b):
        return a
    else:
        return b
    
def bubble_sort(sequence):
    n = len(sequence)
    for i in range(n-1):
        for j in range(n-i-1):
            if(sequence[j] < sequence[j+1]):
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    return sequence


    

def main():
    v = generar_numeros(1000)
        
    promedio = lambda lista: (reduce( lambda x, y: x + y,lista))/(len(lista))
    menor = lambda lista: (reduce(menor_no_lambda, lista))
    pares_impares = lambda resto, lista: filter(lambda n: n%2==resto, lista)
    cantidad_pares = lambda lista: len(pares_impares(0, lista))
    promedio_impares = lambda lista: promedio(pares_impares(1, lista))
    lista_cuadrado = lambda lista: map(lambda x: x*x, lista)
    lista_entre_intervalo_abierto = lambda limiteInf, limiteSup, lista: filter(lambda n: n>limiteInf and n<limiteSup, lista)
    lista_cuadrado_de_intervalo_abierto = lambda limiteInf, limiteSup, lista: lista_cuadrado(lista_cuadrado_de_intervalo_abierto(limiteInf, limiteSup, lista))
    lista_multiplos = lambda numero, lista: filter(lambda n: n%numero==0,lista)
    lista_multiplos_lista_cuadrado_intervalo = lambda numero, limiteInf, limiteSup, lista: lista_multiplos(numero, lista_cuadrado_de_intervalo_abierto(limiteInf, limiteSup, lista))
    multiplos_de_7_ordenados_descendente =  lambda lista: bubble_sort(lista_multiplos(7, lista))
    promedio_impares_negativos = lambda lista: promedio(reduce(lambda n: n<0, pares_impares(1, lista)))
    desviacion_estandar = lambda promedio, lista: math.sqrt(sum(map(lambda x: (x - promedio) ** 2, lista)) / len(lista)) 
    existe_multiplo_127 = lambda lista: len(lista_multiplos(127 ,lista))>0
    lista_terminan_en_2_o_3 = lambda lista: filter(lambda n: (abs(n))%10==2 or n%10==3,lista)
    
    print("Menor:")
    print(menor(v))
    print("Cantida pares:")
    print(cantidad_pares(v))
    print("Promedio impares:")
    print(promedio_impares(v))
    print("Cuadrado de todos los que se encuentren entre 10 y 100 sin incluirlos:")
    print(lista_cuadrado_de_intervalo_abierto(10, 100, v))
    print("Los multiplos de 3 de los cuadrados calculados:")
    print(lista_multiplos_lista_cuadrado_intervalo(3, 10, 100, v))
    print("Multiplos de 7 ordenados en orden descendente:")
    print(multiplos_de_7_ordenados_descendente(v))
    print("Promedio de impares negativos:")
    print(promedio_impares_negativos(v))
    print("Desviación estandar:")
    print(desviacion_estandar(v))
    print("Existe multiplo de 127:")
    print(existe_multiplo_127(v))
    print("Terminan en 2 o 3:")
    print(lista_terminan_en_2_o_3(v))

if __name__=="__main__":
    main()