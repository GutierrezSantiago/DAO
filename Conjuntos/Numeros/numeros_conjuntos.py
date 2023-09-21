## Archivo de números
"""
Del archivo [numeros.txt](./numeros.txt) que contiene un número entero por cada línea, generar un conjunto que contenga todos los números del archivo y desde el conjunto calcular e informar:
 * Cantidad de números no repetidos
 * Suma de todos los números
 * Cantidad de impares
 * Promedio de pares 
"""

def crear_conjunto_desde_txt(nombre_archivo):
    archivo = open(nombre_archivo)
    conjunto = set()
    for line in archivo.readlines():
        conjunto.add(int(line.strip()))
    
    return conjunto

def sumatoria_conjunto(conjunto):
    ac = 0
    for numero in conjunto:
        ac = ac + numero
    return ac

def cantidad_impares(conjunto):
    contador = 0
    for numero in conjunto:
        if numero%2==1:
            contador += 1
    
    return contador

def promedio_pares(conjunto):
    ac, contador = 0, 0
    for numero in conjunto:
        if numero%2==0:
            ac += numero
            contador += 1
    
    if contador==0:
        return 0
    
    return ac/contador
            
def main():
    conjunto = crear_conjunto_desde_txt("./conjuntos/numeros/numeros.txt")
    print(f"Cantidad de números: {len(conjunto):8}")
    print(f"Sumatoria de números: {sumatoria_conjunto(conjunto):8}")
    print(f"Cantidad de impares: {cantidad_impares(conjunto):8}")
    print(f"Promedio de pares: {promedio_pares(conjunto):10.2f}")
    
    
    
if __name__=="__main__":
    main()