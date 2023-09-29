from atencion import Atencion

class Farmacia(Atencion):
    def __init__(self, codigo, tipo_de_cobro, importe_total, descuento):
        super().__init__(codigo, tipo_de_cobro)
        self._importe_total = importe_total
        self._descuento = descuento

    def __str__(self):
        descuento = ""
        if self.descuento == 0:
            descuento = "No"
        else:
            descuento = f"{self.descuento}%"
        return super().__str__() + f" - Importe total base: {self.importe_total} - Descuento: {descuento}"
    
    def importeACobrar(self):
        importeFinal = self.importe_total

        if self.descuento != 0:
            importeFinal*=(1-self.descuento)

        if self.tipo_de_cobro == 2: 
            importeFinal*=1.3
        else:
            importeFinal*=0.95

        return importeFinal
    
    def esMedica(self):
        return False
    
    @property
    def importe_total(self):
        return self._importe_total
    
    @importe_total.setter
    def importe_total(self, importe_total):
        self._importe_total = importe_total

    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, descuento):
        # VALIDACINO 0 o positivo?
        self._descuento = descuento