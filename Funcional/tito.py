"""
Desarrollar un programa controlado por menú de opciones que permita simular el desplazamiento
de un robot sobre un plano cuyo tamaño es de 400 x 400, y las posiciones válidas se identifican
desde 0 como en un sistema de coordenadas cartesianas.
Inicialmente se genera la posición aleatoria del robot en forma de punto (x,y). Luego se presenta
un menú de opciones que permita los siguientes movimientos:

Opción N: Girar al norte y avanzar 10 pasos
Opción S: Girar al sur y avanzar 20 pasos
Opción E: Girar al este y avanzar 10 pasos
Opción O: Girar al oeste y avanzar 20 pasos
Opcion F: Finalizar

Luego de cada movimiento el programa debe informar la posición del robot.
Alternativas:

En lugar de ingresar cada movimiento individualmente, se puede recibir una cadena que contenga más de un movimiento, por ejemplo "NNEENSSNO".
En el caso de que una orden de movimiento lleve al robot fuera de los márgenes del plano, el movimiento debería finalizar en el borde.
"""
import random

def presentacion_menu():
    print("--TITO EL ROBOT--")
    print("N - Girar al norte y avanzar 10 pasos")
    print("S - Girar al sur y avanzar 20 pasos")
    print("E - Girar al este y avanzar 10 pasos")
    print("O - Girar al oeste y avanzar 20 pasos")
    print("F - Finalizar")

def solicitud_opcion():
    op = input("Ingrese una cadena de movimientos a realizar:")
    return op
    #if (op not in opciones):
    #    print("ERROR: Ingrese una opción valida.")
    #    input("Presione enter para continuar...")
    #return op

def ajustar_a_tablero(x, y, tablero):
    limiteN, limiteE = tablero
    if y>limiteN:
        x=limiteN
    if y<0:
        x=0
    if x>limiteE:
        x=limiteE
    if x<0:
        x=0
    return [x, y]

def informar_ubicacion(x, y):
    print(f"Tito se encuentra en la posición ({x}, {y})")

def incializar_tito(tablero):
    x = random.randint(0, tablero[0])
    y = random.randint(0, tablero[1])
    v = [x, y]
    return v

def verificar_pertenencia(movimiento, opciones):
        return movimiento in opciones     

def finalizar():
    print("Finalizando...")
    exit()
    
def menu_opciones():
    tablero = (400, 400)
    v = incializar_tito(tablero)
    
    menu = {
        "N": (lambda x,y: [x, y+10]),
        "S": (lambda x,y: [x, y-20]),
        "E": (lambda x,y: [x+10, y]),
        "O": (lambda x,y: [x-20, y]),
        "F": (lambda x,y: finalizar())
            
    }
    
    
    
    while True:
        presentacion_menu()
        
        print(f"Incializando tablero de {tablero[0]}x{tablero[1]} con Tito en posición aleatoria")
        informar_ubicacion(v[0], v[1])
        
        op = solicitud_opcion()
        
        for movimiento in op:
            if(not verificar_pertenencia(movimiento, menu.keys())):
                print(f"El caracter {movimiento} no corresponde a una opción.")
                continue
                    
            v = menu[movimiento](v[0], v[1])
            v = ajustar_a_tablero(v[0], v[1], tablero)
            informar_ubicacion(v[0], v[1])

def main():
    menu_opciones()

if __name__=="__main__":
    main()