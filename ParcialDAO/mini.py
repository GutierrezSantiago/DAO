from sucursal import Sucursal
class Mini(Sucursal):
    def __init__(self, numero, superficie, facturacion, importeAlquiler):
        super().__init__(numero, superficie, facturacion)
        self._importeAlquiler = importeAlquiler
    
    @property
    def importeAlquiler(self):
        return self._importeAlquiler
    @importeAlquiler.setter
    def importeAlquiler(self, importeAlquiler):
        self._importeAlquiler = importeAlquiler

    def resultado_comercial(self):
        return self.facturacion*1000 - self.importeAlquiler
    
    def es_rentable(self):
        return self.indice_de_rentabilidad()>35