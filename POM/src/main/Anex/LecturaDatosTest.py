import os.path
from POM.src.main.Basic.FuncionesTest import Variables_Globales
from POM.src.main.Action.RecepcionTest import Datos

class Lectura():

    def __init__(self, driver):
        global L, V
        self.driver = driver
        L = Datos(self.driver)
        V = Variables_Globales(self.driver)

    def Despegar(self, t):
        archivo = "TestMaster.xlsx"
        ruta = os.path.join(os.path.dirname(__file__), archivo)
        L.Despegar(ruta, t)