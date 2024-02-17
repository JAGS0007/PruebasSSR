from POM.src.main.Anex.FuncionesExTest import *
from POM.src.main.Basic.FuncionesTest import Variables_Globales
class Resultado():

    def __init__(self, driver):
        self.driver = driver
        global FE, V
        FE = Funexcel(self.driver)
        V = Variables_Globales(self.driver)

    def Despegar(self, i, ruta, tipo, Escribir, t):
        e = V.Existe(tipo, Escribir, t)
        if (e == 'Existe'):
            print('El elemento se inserto correctamente')
            FE.writeData(ruta, 'Consulta', i, 15, 'Si cargo el HTML')
        else:
            print('No se inserto')
            FE.writeData(ruta, 'Consulta', i, 15, 'No cargo el HTML')
