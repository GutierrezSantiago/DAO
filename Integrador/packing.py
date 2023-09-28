from carga import Carga
class Packing(Carga):
    def __init__(self, contenido, peso_por_caja, cantidad, peso_estructura):
        super().__init__(contenido)
        self._peso_por_caja = peso_por_caja
        self._cantidad = cantidad
        self._peso_estructura = peso_estructura

    def __str__(self):
        string = super().__str__()
        string += f" - Peso por caja: {self._peso_por_caja} - Cantidad: {self._cantidad} - Peso estructura: {self._peso_estructura} - Peso total: {self.peso()}"
        return string

    def peso(self):
        return self._peso_por_caja*self._cantidad + self._peso_estructura