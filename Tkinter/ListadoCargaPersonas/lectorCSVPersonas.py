from persona import Persona

class lectorCSVPersonas():
    def __init__(self, ruta):
        self._ruta = ruta
    
    
    def cargarDiccionario(self):
        archivo = open(self._ruta, "r")
        personas = dict()
        for linea in archivo.readlines():
            linea = linea.strip().split(",")
            persona = Persona(linea[1], linea[2], linea[0], int(linea[3]))
            personas[persona.documento] = persona
        
        archivo.close()
        return personas
    
    def cargarLista(self):
        archivo = open(self._ruta, "r")
        personas = []
        for linea in archivo.readlines():
            linea = linea.strip().split(",")
            persona = Persona(linea[1], linea[2], linea[0], int(linea[3]))
            personas.append(persona)
        
        archivo.close()
        return personas