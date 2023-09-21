class Surtidor:
    def __init__(self, numero, cantidad, tipo):
        self.numero = realpart
        self.cantidad = imagpart
        self.tipo = tipo

def cargar_surtidor():
    numero = 
    can
    tipo = input

def inputRangoEntero(menor, mayor, mensaje):
    while True:
        numero = input(mensaje)
        if numero%1==0:
            print("El número ingresado debe ser entero. Presione enter para reingresar el número.")
        if menor<=numero and numero<=mayor:
            return numero
        print(f"El número debe estar entre {menor} y {mayor}. Presione enter para reingresar el número.")

    
def inputSuperiorA(limiteInferior, mensaje):
    while True:
        numero = input(mensaje)
        if numero%1==0:
            print("El número ingresado debe ser entero. Presione enter para reingresar el número.")
        if limiteInferior<=numero:
            return numero
        print(f"El número debe ser superior a {limiteInferior}. Presione enter para reingresar el número.")


def inputNumero():
    return inputRangoEntero(1, 30, "Ingrese el número de surtidor(1 a 30): ")

def inputCantidad():
    return 

def inputTipo():
    return inputRangoEntero(1, 3, "Ingrese el tipo de nafta\n1 - Nafta Super\n2 - Nafta Especial\n3 - Gas Oil \n-----:")                                          