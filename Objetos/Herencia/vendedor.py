from empleado import Empleado


class Vendedor(Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldoBasico, importeTotalVentas):
        super().__init__(tipo, legajo, nombre, apellido, sueldoBasico)
        self._importeTotalVentas = importeTotalVentas
    
    
    def __str__(self):
        super().__str__ + f" - Importa Total Ventas: {self.importeTotalVentas}"
   
        
    @property
    def importeTotalVentas(self): return self._importeTotalVentas
    
    
    def calcular_sueldo(self):
        return self.sueldo_basico+(self.importeTotalVentas*0.01)
    
"""
En el caso de los obreros, el sueldo básico corresponde a un mes de 20 días laborables, y el sueldo a cobrar debe ser un propocional a la cantidad de días efectivamente trabajados.
En el caso de los administrativos, el sueldo a cobrar es igual al básico, pero se incrementa en 13% si le corresponde cobrar el presentismo.
Los vendedores cobrar el sueldo básico más un 1% del total vendido.
"""    