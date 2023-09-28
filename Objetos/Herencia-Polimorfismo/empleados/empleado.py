class Empleado:
    def __init__(self, tipo, legajo, nombre, apellido, sueldo_basico):
        self._tipo = tipo
        self._legajo = legajo
        self._nombre = nombre
        self._apellido = apellido
        self._sueldo_basico = sueldo_basico
    
    def __str__(self):
        return f"Tipo: {self.tipo} - Legajo: {self.legajo} - Nombre: {self.nombre} - Apellido: {self.apellido} - Sueldo Básico: {self.sueldo_basico}"
    
    @property
    def tipo(self): return self._tipo    
    
    @property
    def legajo(self): return self._legajo
    
    @property
    def nombre(self): return self._nombre
    
    @property
    def apellido(self): return self._apellido
    
    @property
    def sueldo_basico(self): return self._sueldo_basico
    
    def calcular_sueldo(self):
        pass