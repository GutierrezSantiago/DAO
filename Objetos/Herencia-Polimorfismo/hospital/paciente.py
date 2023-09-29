class Paciente:
    def __init__(self, nombre, sintoma, habitual):
        self._nombre = nombre
        self._sintoma = sintoma
        self._habitual = habitual

    def __str__(self):
        sintoma = ""
        habitual = ""

        if self.sintoma == 1:
            sintoma = "Corazon"
        elif self.sintoma == 2:
            sintoma = "Pulmon"
        else:
            sintoma = "Otras"
        
        if self.habitual:
            habitual = "Si"
        else:
            habitual = "No"

        return f"Nombre: {self.nombre} - Sintoma: {sintoma} - Habitual: {habitual}"
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def sintoma(self):
        return self._sintoma
    
    @sintoma.setter
    def sintoma(self, sintoma):
        self._sintoma = sintoma

    @property
    def habitual(self):
        return self._habitual
    
    @habitual.setter
    def habitual(self, habitual):
        self._habitual = habitual