from sucursal import Sucursal
class Super(Sucursal):
    def __init__(self, numero, superficie, facturacion, esMayorista):
        super().__init__(numero, superficie, facturacion)
        self._esMayorista = esMayorista
    
    @property
    def esMayorista(self):
        return self._esMayorista
    @esMayorista.setter
    def esMayorista(self, esMayorista):
        self._esMayorista = esMayorista
        
    def resultado_comercial(self):
        return self.facturacion*1000
    
    def es_rentable(self):
        valorCritico = 40
        if self.esMayorista: 
            valorCritico+=5
        return self.indice_de_rentabilidad()>valorCritico