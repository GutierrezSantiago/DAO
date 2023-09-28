from obrero import Obrero
from administrativo import Administrativo
from vendedor import Vendedor
from lectorCSVEmpleados import LectorCSVEmpleados

class PlantelDeEmpleados():
    def __init__(self, rutaCSV):
        lectorCSV = LectorCSVEmpleados(rutaCSV)
        self._empleados = lectorCSV.cargarEmpleadosCSV()
    
    @property
    def empleados(self): return self._empleados
    
    def calcularSueldosAPagar(self):
        sueldos = 0
        for emp in self.empleados.values():
            sueldos += emp.calcular_sueldo()
        return sueldos
    
    def contarEmpleadosPorTipo(self):
        empleados_por_tipo = dict()
        for emp in self.empleados.values():
            if emp.tipo not in empleados_por_tipo.keys():
                empleados_por_tipo[emp.tipo] = 1
            else:
                empleados_por_tipo[emp.tipo] += 1
        
        return empleados_por_tipo
    
    def buscarEmpleado(self, legajo):
        if legajo in self.empleados.keys():
            return self.empleados[legajo]
            