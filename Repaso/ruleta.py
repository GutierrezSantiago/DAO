"""
Desarrollar un programa que simule el juego de la ruleta.
Para ello generar al azar 1000 tiradas y luego informar:
• Cantidad de pares e impares
• Cantidad de tiradas por cada docena
• Porcentaje de ceros sobre el total de jugadas.
• Cantidad de rojos y de negros
"""
import random

def generar_tirada():
    return random.randint(0,36)

def es_par(numero):
    return numero%2==0

def esta_en_lista(numero, lista):
    return numero in lista 

def definirDocena(numero):
    return (numero-1)//12
    


def main():
    listaRojos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    ceros = 0
    pares = 0
    rojos = 0
    vectorDocena = [0,0,0]

    for i in range(1000):
        tirada = generar_tirada()
        if tirada == 0:
            ceros+=1
            continue

        indiceDocena = definirDocena(tirada)
        vectorDocena[indiceDocena] += 1
        if es_par(tirada):
            pares += 1
        if esta_en_lista(tirada, listaRojos):
            rojos += 1
    
    print(f"Porcentaje de ceros: {ceros/10}%")
    print(f"Cantidad de pares: {pares}")
    print(f"Cantidad de impares: {1000-pares}")
    print(f"Cantidad de rojos: {rojos}")
    print(f"Cantidad de negros: {1000-rojos}")
    print(f"Cantidad en primer docena: {vectorDocena[0]}")
    print(f"Cantidad en segunda docena: {vectorDocena[1]}")
    print(f"Cantidad en tercer docena: {vectorDocena[2]}")

if __name__=="__main__":
    main()