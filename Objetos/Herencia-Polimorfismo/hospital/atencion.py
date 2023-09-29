class Atencion:
    def __init__(self, codigo, tipo_de_cobro):
        self._codigo = codigo
        self._tipo_de_cobro = tipo_de_cobro
    
    def __str__(self):
        tipo_de_cobro = ""
        if self.tipo_de_cobro == 1:
            tipo_de_cobro = "Efectivo"
        else:
            tipo_de_cobro = "Tarjeta de Credito"

        return f"Codigo: {self.codigo} - Tipo de Cobro: {tipo_de_cobro}"

    def importeACobrar(self):
        pass

    def esMedica(self):
        pass

    def medicaEnRango(self, limInf, limSup):
        bandera = self.esMedica()
        importeACobrar = self.importeACobrar()
        bandera = bandera and importeACobrar>limInf and importeACobrar<limSup
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def tipo_de_cobro(self):
        return self._tipo_de_cobro
    
    @tipo_de_cobro.setter
    def tipo_de_cobro(self, tipo_de_cobro):
        self._tipo_de_cobro = tipo_de_cobro