"""

Una Veterinaria encargada del cuidado de mascotas ha solicitado la
realización de un software para obtener resultados sobre sus clientes y sus
respectivas mascotas. (Suponer que cada cliente posee una sola mascota)
Se sabe que cada Cliente de esta veterinaria tiene: un numero de cliente, un
nombre, una antigüedad (hace cuántos años que son clientes de la veterinaria) y una
Mascota.
De la Mascota se dispone los siguientes datos: el nombre y la edad.
El software requiere cargar por teclado los datos de varios clientes y almacenarlos en alguna colección adecuada.
Se pide:

Mostrar la cantidad de clientes.
Mostrar el promedio de edad de las mascotas.
Informar cuántos clientes tienen una antigüedad mayor igual a 5 años.
Listado de los datos de todos los clientes cuya mascota tiene más de 5 años de edad.

"""
from cliente import Cliente
from mascota import Mascota

def cargarDatosMascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))
    return Mascota(nombre, edad)
    
def cargarDatosCliente():
    numero = input("Ingrese el numero del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    antiguedad = int(input("Ingrese la antigüedad del cliente: "))
    mascota = cargarDatosMascota()
    return Cliente(numero, nombre, antiguedad, mascota)

def cargarClientes():
    lista_clientes = []
    carga = ""
    while(True):
        carga = input("Si desea cargar un cliente presione enter, sino ingrese -1 ...")
        if carga == "-1":
            break
        cliente = cargarDatosCliente()
        lista_clientes.append(cliente)
        print("Cliente cargado!")
    
    return lista_clientes

def getPromedioEdadMascotas(clientes):
    ac, cont = 0, 0
    for c in clientes:
        ac += c.getEdadMascota()
        cont += 1
    
    return ac/cont
        
def main():
    clientes = cargarClientes()
    cantidad_clientes = len(clientes)
    promedio_edad_mascotas = getPromedioEdadMascotas(clientes)
    cantidad_antigued_mayor_igual_5 = len(list(filter(lambda c: c.antiguedad>=5, clientes)))
    lista_clientes_edad_mascotas_mayor_5 = filter(lambda c: c.getEdadMascota()>5, clientes)
    
    print(f"Cantidad de clientes: {cantidad_clientes}")
    print(f"Promedio edad de mascotas: {promedio_edad_mascotas}")
    print(f"Cantidad de clientes con antiguedad mayor o igual a 5 años: {cantidad_antigued_mayor_igual_5}")
    print(f"Listado de datos de clientes cuya mascota tiene una edad mayor a 5 años:")
    for c in lista_clientes_edad_mascotas_mayor_5:
        print(c)
    
if __name__=="__main__":
    main()