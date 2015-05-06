#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import datetime
from collections import namedtuple
from BilleteraElectronica import BilleteraElectronica

#Instancia para probar la función recargar
BillAlpha = BilleteraElectronica("Bill","Pedro","Molinaro",5555555,123)

class BilleteraElectronicaTester(unittest.TestCase):

    #CASO INTERNO: probar que se crea correctamente una instancia de la clase
    #Resultado esperado: TRUE

    def testClase(self):
        Billete = BilleteraElectronica("Dolar300","Hugo","Perez",1,1)

    #resultado obtenido: No existe el mòdulo llamado "BilleteraElectronica"
#-------------------------------------------------------------------------------    
    #CASO INTERNO: probar que se llama correctamente la función recargar
    #Resultado esperado: TRUE
    
    def testRecargar(self):
        BillAlpha.recargar(1,datetime.datetime(2012,12,15),111)
        
    #Resultado obtenido: No existe la función "recargar"
#-------------------------------------------------------------------------------
    
    #CASO INTERNO: probar que se almacenó la recarga hecha en una estructura 
    #              llamada listaCreditos
    # Resultado esperado: se consiga en alguna posición de la lista
    
    def testVerificarExistenciaDeRecarga(self):
        BillAlpha.recargar(2,datetime.datetime(1193,5,6),455)
        tester = False
        for i in range(0,len(BillAlpha.listaCreditos)):
            if (BillAlpha.listaCreditos[i].monto == 2):
                tester = True
        assert(tester)
        
    #Resultado obtenido: Falla al no existir la lista de creditos
#-------------------------------------------------------------------------------

    #CASO BORDE: probar que el monto introducido sea un número Natural
    #Resultado esperado: De un mensaje de monto invalido.
    
    def testMontoNatural(self):
       self.assertEqual(-1, BillAlpha.recargar(-1,datetime.datetime(1996,4,6),345))
        
    #Resultado obtenido: No niega la transacción.
#-------------------------------------------------------------------------------

    #CASO BORDE: probar que la fecha sea válida 
    #Resultado esperado: que de error por introducir dia 32
    
    def testValidezFecha(self):
        try:
            BillAlpha.recargar(1,datetime.datetime(2012,12,32),111)
        except Exception:
            pass
        else:
            self.fail("El metodo debio tirar error! Cantidad de dias erroneo para el mes")
        
    #Resultado obtenido: no da error por trabajarse con strings
    
#-------------------------------------------------------------------------------    
    #CASO INTERNO: probar que se llama correctamente la función consumir
    #Resultado esperado: TRUE
    
    def testLLamadaConsumir(self):
        BillAlpha.consumir(0,datetime.datetime(2012,12,15),111,123)
        
    #Resultado obtenido: No existe la función "consumir"
#-------------------------------------------------------------------------------

    #CASO INTERNO: probar que se introduzca un PIN invalido
    #Resultado esperado: Exception
    
    def testConsumirPinErroneo(self): 
           
        try:
            BillAlpha.consumir(1,datetime.datetime(2012,12,15),1113522,12343423423)
        except Exception:
            pass
        else:
            self.fail("El metodo debio tirar error! El PIN ingresado es erroneo")
        
        
    #Resultado obtenido: El metodo se ejecuta
#-------------------------------------------------------------------------------

    #CASO INTERNO: probar que se introduzca monto mayor al saldo
    #Resultado esperado: Exception
    
    def testSaldoInsuficiente(self): 
        BillAlpha2 = BilleteraElectronica("Bill","Pedro","Molinaro",55555555,123)   
        try:
            BillAlpha2.consumir(100,datetime.datetime(2012,12,15),111,123)
        except Exception:
            pass
        else:
            self.fail("El metodo debio tirar error! El monto es mayor al Saldo")
        
        
    #Resultado obtenido: El metodo se ejecuta
#-------------------------------------------------------------------------------

    #CASO INTERNO: probar que se almacenó la recarga hecha en una estructura 
    #              llamada listaCreditos
    # Resultado esperado: se consiga en alguna posición de la lista
    
    def testVerificarExistenciaDeConsumo(self):
        BillAlpha.recargar(100,datetime.datetime(1193,5,6),455)
        BillAlpha.consumir(50,datetime.datetime(1193,5,6),455,123)
        tester = False
        for i in range(0,len(BillAlpha.listaConsumos)):
            if (BillAlpha.listaConsumos[i].monto == 50):
                tester = True
        assert(tester)
        
    #Resultado obtenido: Falla al no existir la lista de consumos
#-------------------------------------------------------------------------------
  

if __name__ == '__main__':
    unittest.main()
