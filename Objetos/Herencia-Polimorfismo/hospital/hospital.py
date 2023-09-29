from atencion import Atencion
class Hospital:
    def __init__(self, razon_social, atenciones):
        self._razon_social = razon_social
        self._atenciones = atenciones
    
    def __str__(self):
        return f"Hospital:\nRazon Social: {self.razon_social}\nAtenciones: {len(self.atenciones)}"

    
    @property
    def razon_social(self):
        return self._razon_social
        
    @razon_social.setter
    def razon_social(self, razon_social):
        self._razon_social = razon_social
        
    @property
    def atenciones(self):
        return self._atenciones
    
    @atenciones.setter
    def atenciones(self, atenciones):
        self._atenciones = atenciones
    
    def addAtencion(self, atencion: Atencion):
        self.atenciones[atencion.codigo] = atencion
    
    def importe_total_atencion_consulta(self):
        ac = 0
        atenciones = filter(lambda a: a.esMedica() ,self.atenciones)
        for a in atenciones:
            ac += a.importeACobrar()
        
        return ac

    def importe_promedio_atenciones(self, limInf, limSup):
        ac, cont = 0, 0
        atenciones = filter(lambda a: a.medicaEnRango(limInf, limSup), self.atenciones)
        for a in atenciones:
            ac += a.importeACobrar()
            cont += 1
        
        return ac/cont
    
    def codigo_primera_atencion_habitual(self):
        for v in self.atenciones.values():
            if v.esMedica() & v.paciente.habitual:
                return v.codigo
        
        return 0

