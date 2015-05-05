from collections import namedtuple

class BilleteraElectronica(object):

    def __init__(self,ident, nombres, apellidos, CI, PIN):
        self.identificador = ident
        self.nombre = nombres
        self.apellido = apellidos
        self.CI = CI
        self.PIN = PIN
        self.saldoActual = 0
        
    def recargar(self,mont,fech,id_):
        pass
