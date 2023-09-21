class Cliente:
    def __init__(self, numero, nombre, antiguedad, mascota):
        self._numero = numero
        self._nombre = nombre
        self._antiguedad = antiguedad
        self._mascota = mascota

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def antiguedad(self):
        return self._antiguedad

    @antiguedad.setter
    def antiguedad(self, value):
        self._antiguedad = value

    @property
    def mascota(self):
        return self._mascota

    @mascota.setter
    def mascota(self, value):
        self._mascota = value

    def __str__(self):
        return f"Numero: {self._numero} - Nombre: {self._nombre} - Antigüedad: {self._antiguedad} \n Mascota: {self._mascota}"
    
    def getEdadMascota(self):
        return self._mascota.edad
    