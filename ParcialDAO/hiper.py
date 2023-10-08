from sucursal import Sucursal
class Hiper(Sucursal):
    def __init__(self, numero, superficie, facturacion, importeAlquileres):
        super().__init__(numero, superficie, facturacion)
        self._importeAlquileres = importeAlquileres
    
    @property
    def importeAlquileres(self):
        return self._importeAlquileres
    @importeAlquileres.setter
    def importeAlquileres(self, importeAlquileres):
        self._importeAlquileres = importeAlquileres

    def resultado_comercial(self):
        return self.facturacion*1000 + self.importeAlquileres
    
    def es_rentable(self):
        return self.indice_de_rentabilidad()>50