from persona import Persona

class Padron():
    def __init__(self, personas):
        self._personas = personas
    
    @property
    def personas(self):
        return self._personas

    @property
    def cantidad(self):
        return len(self._personas.values())
    
    @property
    def promedio_edades(self):
        ac = 0
        for v in self._personas.values():
            ac += v.edad
        
        return ac/self.cantidad
    
    def agregar(self, persona: Persona):
        self.personas[persona.documento] = persona