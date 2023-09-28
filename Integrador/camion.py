from carga import Carga
from caja import Caja
from packing import Packing
from bidon import Bidon

class Camion():
    def __init__(self, patente, estado, carga_maxima, cargas):
        self._patente = patente
        self._estado = estado
        self._carga_maxima = carga_maxima
        self._cargas = cargas
    
    def __str__(self):
        return f"Patente: {self._patente} - Estado: {self._estado} - Carga Máxima: {self._carga_maxima}"
    
    def cantidad_cargas(self):
        return len(self._cargas)
    
    def subir_carga(self, carga: Carga):
        self._cargas.append(self, carga)
    
    def bajar_carga(self, carga: Carga):
        self._cargas.remove(carga)

    def peso_cargas(self):
        ac = 0
        for c in self._cargas:
            ac += c.peso()
    
    def a_reparacion(self):
        self._estado = "En Reparacion"

    def sale_reparacion(self):
        self._estado = "Disponible"

    def en_viaje(self):
        self._estado = "De viaje"

    def de_regreso(self):
        self._estado = "Disponible"
    
    def listo_para_salir(self):
        return (self._estado == "Disponible" and self.peso_cargas >= 0.75*self._carga_maxima)

    def cargas_en_orden(self):
        string = f"Cargas del camión con patente {self._patente} en orden:"
        for c in self._cargas:
            string += "> " + type(c).__name__ + ": "
            string += c.__str__() + "\n"