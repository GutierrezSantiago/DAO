from empleado import Empleado


class Administrativo(Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldoBasico, cobraPresentismo):
        super().__init__(tipo, legajo, nombre, apellido, sueldoBasico)
        self._cobraPresentismo = cobraPresentismo
    
    def __str__(self):
        if self.cobraPresentismo:
            cobra = "Si"
        else:
            cobra = "No"
            
        super().__str__ + f" - Cobra Presentismo: {cobra}"
    
    @property
    def cobraPresentismo(self): return self._cobraPresentismo
    
    def calcular_sueldo(self):
        return self.sueldo_basico*1.13 if self.cobraPresentismo else self.sueldo_basico
    
