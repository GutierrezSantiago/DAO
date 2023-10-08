class Sucursal:
    def __init__(self, numero, superficie, facturacion):
        self._numero = numero
        self._superficie = superficie
        self._facturacion = facturacion

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def superficie(self):
        return self._superficie
    @superficie.setter
    def superficie(self, superficie):
        self._superficie = superficie
    
    @property
    def facturacion(self):
        return self._facturacion
    @facturacion.setter
    def facturacion(self, facturacion):
        self._facturacion = facturacion

    def resultado_comercial(self):
        pass
    
    def indice_de_rentabilidad(self):
        return (self.resultado_comercial()/1000)/self.superficie
    
    def es_rentable(self):
        pass

