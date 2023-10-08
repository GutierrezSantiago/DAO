from sucursal import Sucursal
from super import Super
from hiper import Hiper
from mini import Mini 
class Empresa:
    def __init__(self, sucursales):
        self._sucursales = sucursales
    
    @property
    def sucursales(self):
        return self._sucursales
    
    def suma_de_ganancia(self):
        resultados_comerciales = [s.resultado_comercial() for s in self.sucursales]
        return sum(resultados_comerciales)
    
    def cantidad_de_locales_no_rentables(self):
        resultados_no_rentables = list(filter(lambda s: not s.es_rentable(), self.sucursales))
        return len(resultados_no_rentables)
    
    def local_mas_rentable(self):
        masRentable = 0
        for s in self.sucursales:
            if masRentable == 0:
                masRentable=s
                continue
            if s.indice_de_rentabilidad()>masRentable.indice_de_rentabilidad():
                masRentable = s
                continue
                
        return f"Número de sucursal: {masRentable.numero} - Tipo de Sucursal: {masRentable.__class__.__name__}"
