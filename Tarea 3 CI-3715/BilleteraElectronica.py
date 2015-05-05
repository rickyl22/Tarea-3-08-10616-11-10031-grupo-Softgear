'''
Created on May 4, 2015

@author: antonio
'''
from collections import namedtuple

class BilleteraElectronica(object):
    
    Consumo = namedtuple('Consumo', 'monto fecha idEst') #Estructura del consumo 
    Credito = namedtuple('Credito', 'monto fecha idEst') #Estructura del crédito 
    
    listaConsumos = [] 
    listaCreditos = []

    def __init__(self, nombres, apellidos, CI, PIN):
        self.nombre = nombres
        self.apellido = apellidos
        self.CI = CI
        self.PIN = PIN
        self.saldoActual = 0
     
    def saldo(self):
        return self.saldoActual    
        
    def recargar(self,mont,fech,id_):
        self.saldoActual += mont
        infoRecarga = self.Recarga(mont,fech,id_)
        self.listaCreditos.append(infoRecarga)
        
    def consumir(self,mont,fech,id_,pinUsuario):
        if self.saldoActual < mont:
            raise Exception("No hay suficiente saldo para realizar la operacion")
        elif pinUsuario != self.PIN:
            raise Exception("El PIN introducido es invalido")
        else:
            infoConsumo = self.Consumo(mont,fech,id_)
            self.listaConsumos.append(infoConsumo)
            self.saldoActual -= mont
        
    if __name__ == '__main__':
        pass
    
        