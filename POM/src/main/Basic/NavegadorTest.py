from POM.src.main.Basic.FuncionesTest import Variables_Globales


class Browser():

    def __init__(self, driver):
        global V
        self.driver = driver
        V = Variables_Globales(driver)

    def Despegar(self, t):
        V.Navegador('https://www.despegar.com.co/', t)