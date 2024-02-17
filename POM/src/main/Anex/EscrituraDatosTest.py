from POM.src.main.Basic.FuncionesTest import Variables_Globales
from selenium.common.exceptions import TimeoutException

class Escribir():

    def __init__(self, driver):
        global V
        self.driver = driver
        V = Variables_Globales(self.driver)

    def Caracter(self, Plan, Cart, t):
        global Pos1, Pos2, Pos3
        if Plan == 'Alojamientos':
            if Cart == 'Todos':
                Pos1 = 1
            elif Cart == 'Hoteles':
                Pos1 = 2
            elif Cart == 'Alquiler':
                Pos1 = 3
            return Pos1
        elif Plan == 'Vuelos':
            pass
        elif Plan == 'Paquetes':
            pass

    def Mes(self, Mes, t):
        global Pos1
        if Mes == 'Ene':
            Pos1 = 1
        elif Mes == 'Feb':
            Pos1 = 2
        elif Mes == 'Mar':
            Pos1 = 3
        elif Mes == 'Abr':
            Pos1 = 4
        elif Mes == 'May':
            Pos1 = 5
        elif Mes == 'Jun':
            Pos1 = 6
        elif Mes == 'Jul':
            Pos1 = 7
        elif Mes == 'Ago':
            Pos1 = 8
        elif Mes == 'Sep':
            Pos1 = 9
        elif Mes == 'Oct':
            Pos1 = 10
        elif Mes == 'Nov':
            Pos1 = 11
        elif Mes == 'Dic':
            Pos1 = 12
        return Pos1