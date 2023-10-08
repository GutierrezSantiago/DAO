from empresa import Empresa
from sucursal import Sucursal
from super import Super
from hiper import Hiper
from mini import Mini
def principal():
    archivoCSV = open("./sucursales.csv")
    sucursales = []
    for line in archivoCSV.readlines():
        line = line.strip().split(",")
        if line[0] == "1":
            s = Hiper(line[1],int(line[2]),float(line[3]), float(line[4]))
        elif line[0] == "2":
            s = Super(line[1],int(line[2]),float(line[3]), bool(int(line[4])))
        else:
            s = Mini(line[1],int(line[2]),float(line[3]), float(line[4]))
        sucursales.append(s)

    empresa = Empresa(sucursales)
    print(f"Suma de ganancia: ${empresa.suma_de_ganancia()}")
    print(f"Cantidad de locales no rentables: {empresa.cantidad_de_locales_no_rentables()}")
    print(f"Local más rentable: " + empresa.local_mas_rentable())
    

if __name__=="__main__":
    principal()