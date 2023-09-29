from atencion import Atencion
from paciente import Paciente

class Medica(Atencion):
    def __init__(self, codigo, tipo_de_cobro, paciente, importe):
        super().__init__(codigo, tipo_de_cobro)
        self._paciente = paciente
        self._importe = importe
    
    def __str__(self):
        return super().__str__() + f" - Importe base: {self.importe} - Paciente: [{self.paciente.__str__()}]"

    def importeACobrar(self):
        importeFinal = self._importe
        if self.paciente.habitual: importeFinal*=0.75
        if self.tipo_de_cobro == 2: 
            importeFinal*=1.2
        else:
            importeFinal*=0.9
        return importeFinal
    
    def esMedica(self):
        return True
    
    @property
    def paciente(self):
        return self._paciente
    
    @paciente.setter
    def paciente(self, paciente):
        self._paciente = paciente

    @property
    def importe(self):
        return self._importe
    
    @importe.setter
    def importe(self, importe):
        self._importe = importe