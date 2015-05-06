#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple
import datetime

class BilleteraElectronica(object):

    Credito = namedtuple('Credito', 'monto fecha idEst') #Estructura del crédito
    Consumo = namedtuple('Consumo', 'monto fecha idEst') #Estructura del consumo
    
    listaCreditos = []
    listaConsumos = []
    
    def __init__(self,ident, nombres, apellidos, CI, PIN):
        self.identificador = ident
        self.nombre = nombres
        self.apellido = apellidos
        self.CI = CI
        self.PIN = PIN
        self.saldoActual = 0
        
    def recargar(self,mont,fech,id_):
        if (mont < 0):
            print("El monto de recarga no puede ser negativo")
            return -1
        infoRecarga = self.Credito(mont,fech,id_)
        self.listaCreditos.append(infoRecarga)
        self.saldoActual += mont
        return 0
    
    def consumir(self,mont,fecha,ident,pinUsuario):
        if (mont < 0):
            print("El monto de recarga no puede ser negativo")
            return -1
        if pinUsuario != self.PIN:
            raise Exception("El PIN introducido es invalido")
        elif self.saldoActual < mont:
            raise Exception("No hay suficiente saldo para realizar la operacion")
        else:
            infoConsumo = self.Consumo(mont,fecha,ident)
            self.listaConsumos.append(infoConsumo)
            self.saldoActual -= mont
        
if __name__ == '__main__':
        fecha = datetime.datetime(2014,13,40)
