from collections import namedtuple

class BilleteraElectronica(object):

    Credito = namedtuple('Credito', 'monto fecha idEst') #Estructura del crédito
    listaCreditos = []

    def __init__(self,ident, nombres, apellidos, CI, PIN):
        self.identificador = ident
        self.nombre = nombres
        self.apellido = apellidos
        self.CI = CI
        self.PIN = PIN
        self.saldoActual = 0
        
    def recargar(self,mont,fech,id_):
        infoRecarga = self.Credito(mont,fech,id_)
        self.listaCreditos.append(infoRecarga)
