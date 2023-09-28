from carga import Carga
class Bidon(Carga):
    def __init__(self, contenido, capacidad, densidad):
        super().__init__(contenido)
        self._capacidad = capacidad
        self._densidad = densidad
    
    def __str__(self):
        string = super().__str__()
        string += f" - Capacidad: {self._capacidad} - Densidad: {self._densidad} - Peso: {self.peso()}"
        return string
    
    def peso(self):
        return self._densidad*self._capacidad
