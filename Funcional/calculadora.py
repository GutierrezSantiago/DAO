"""
Desarollar un programa que implemente una calculadora básica. El mismo debe presentar un menú de opciones
con una opción por cada operación aritmética básica (suma, diferencia, producto y cociente).
"""
def presentacion_menu():
    print("--CALCULADORA--")
    print("1 - suma")
    print("2 - diferencia")
    print("3 - producto")
    print("4 - cociente")
    print("5 - salir")

def solicitud_opcion():
    op = int(input("Ingrese una opción:"))
    if (op<0 or op>5):
        print("ERROR: Ingrese una opción valida.")
        input("Presione enter para continuar...")
    return op-1

def solicitud_parametros_calculadora(cociente):
    x = int(input("Ingrese el primer número:"))
    y = int(input("Ingrese el segundo número:"))
    while (cociente):
        if (y==0):
            y = int(input("Ingrese un cociente valido (No es posible 0):"))
        else:
            break
    return x, y

def menu_opciones():
    suma = lambda x, y: x + y
    diferencia = lambda x, y: x - y
    producto = lambda x, y: x * y
    cociente = lambda x, y: x / y

    menu = [suma, diferencia, producto, cociente]

    while True:
        presentacion_menu()
        op = solicitud_opcion()
        if (op==4):
            print("Saliendo...")
            break
        x,y = solicitud_parametros_calculadora(op==3)
        resultado = menu[op](x, y)
        print("Procesando...")
        print(f"Resultado: {resultado}")

def main():
    menu_opciones()

if __name__=="__main__":
    main()