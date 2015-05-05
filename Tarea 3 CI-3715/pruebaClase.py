import unittest
from collections import namedtuple
from BilleteraElectronica import BilleteraElectronica

class BilleteraElectronicaTester(unittest.TestCase):

    #CASO INTERNO: probar que se crea correctamente una instancia de la clase
    #Resultado esperado: TRUE

    def testClase(self):
        Billete = BilleteraElectronica("Dolar300","Hugo","Perez",1,1)

    #resultado obtenido: No existe el mòdulo llamado "BilleteraElectronica"
    
    #CASO INTERNO: probar que se llama correctamente la función recargar
    #Resultado esperado: TRUE
    
    def testRecargar(self):
        recargar(1,"2/2/1992",111)
        
    #Resultado obtenido: No existe la función "recargar"

if __name__ == '__main__':
    unittest.main()
