#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
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
        BillAlpha.recargar(1,"2/2/1992",111)
        
    #Resultado obtenido: No existe la función "recargar"
#-------------------------------------------------------------------------------
    
    #CASO INTERNO: probar que se almacenó la recarga hecha en una estructura 
    #              llamada listaCreditos
    # Resultado esperado: se consiga en alguna posición de la lista
    
    def testVerificarExistenciaDeRecarga(self):
        BillAlpha.recargar(2,"1/2/1993",455)
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
       self.assertEqual(-1, BillAlpha.recargar(-1,"4/5/1996",345))
        
    #Resultado obtenido: No niega la transacción.
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
