from empleado import Empleado
from obrero import Obrero
from administrativo import Administrativo
from vendedor import Vendedor

class LectorCSVEmpleados:
    def __init__(self, path):
        self._path = path
    
    @property
    def path(self): return self._path
        
    def cargarEmpleadosCSV(self):
        archivoCSV = open(self.path, 'r')
        
        empleados = dict()
        
        for line in archivoCSV.readlines():
            line = line.strip().split(";")
            if line[0] == "1":
                emp = Obrero(line[0], line[1], line[2], line[3], float(line[4]), int(line[5]))
            elif line[0] == "2":
                emp = Administrativo(line[0], line[1], line[2], line[3], float(line[4]), bool(line[5]))
            else:
                emp = Vendedor(line[0], line[1], line[2], line[3], float(line[4]), float(line[5]))
            
            empleados[emp.legajo] = emp
                    
        archivoCSV.close()
        
        return empleados