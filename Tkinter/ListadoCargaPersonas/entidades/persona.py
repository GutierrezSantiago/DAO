class Persona:
    def __init__(self, nombre, apellido, documento, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._documento = documento
        self._edad = int(edad)

   
    @property
    def nombre(self):
        return self._nombre
            
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre  
    
    @property
    def apellido(self):
        return self._apellido
            
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido  
        
    @property
    def documento(self):
        return self._documento
            
    @documento.setter
    def documento(self, documento):
        self._documento = documento  
        
    @property
    def edad(self):
        return self._edad
            
    @edad.setter
    def edad(self, edad):
        self._edad = edad          
        
    def __str__(self):
       return f"Nombre: {self._nombre} - Apellido: {self._apellido} - Documento: {self._documento} - Edad: {self._edad}"
    
    def esMayor(self):
        return self._edad>=18
    
    def tieneApellidoVocal(self):
        return self._apellido[0] in 'AEIOU'