from empleado import Empleado

class Obrero(Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldoBasico, diasTrabajados):
        super().__init__(tipo, legajo, nombre, apellido, sueldoBasico)
        self._diasTrabajados = diasTrabajados   

    def __str__(self):
        super().__str__ + f" - Dias Trabajados: {self.diasTrabajados}"
    
    @property
    def diasTrabajados(self): return self._diasTrabajados
    
    def calcular_sueldo(self):
        return self.sueldo_basico*(self.diasTrabajados/20)
    
