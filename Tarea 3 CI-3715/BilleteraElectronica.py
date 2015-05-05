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
     
    def saldo(self):
        saldoActual = 0
        for x in range(0,len(self.listaCreditos)):
            saldoActual += self.listaCreditos[x].monto
        return saldoActual    
        
    def recargar(self,mont,fech,id_):
        infoRecarga = self.Recarga(mont,fech,id_)
        self.listaCreditos.append(infoRecarga)
        
    def consumir(self,mont,fech,id_):
        infoConsumo = self.Consumo(mont,fech,id_)
        self.listaConsumos.append(infoConsumo)
        
    if __name__ == '__main__':
        pass
    
        