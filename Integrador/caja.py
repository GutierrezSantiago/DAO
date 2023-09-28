from carga import Carga
class Caja(Carga):
    def __init__(self, contenido, peso):
        super().__init__(contenido)
        self._peso = peso
    
    def __str__(self):
        string = super().__str__()
        string += f" - Peso: {self.peso()}"
        return string
    
    def peso(self):
        return self._peso