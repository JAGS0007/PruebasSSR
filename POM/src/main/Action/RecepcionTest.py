from POM.src.main.Anex.FuncionesExTest import *
from POM.src.main.Anex.EscrituraDatosTest import *
from POM.src.main.Action.ConsultarTest import Consultar
from POM.src.main.Basic.FuncionesTest import Variables_Globales
import pyautogui

class Datos():

    def __init__(self, driver):
        self.driver = driver
        global FE, Es, C, V, D, Con
        FE = Funexcel(self.driver)
        Es = Escribir(self.driver)
        C = Consultar(self.driver)
        V = Variables_Globales(self.driver)

    def Despegar(self, ruta, t):
        filas = FE.getRowCount(ruta, 'Vacaciones')
        for i in range(3, filas + 1):
            Plan = FE.readData(ruta, 'Vacaciones', i, 1)
            Cart1 = FE.readData(ruta, 'Vacaciones', i, 2)
            Ciudad1 = FE.readData(ruta, 'Vacaciones', i, 3)
            Ciudad2 = FE.readData(ruta, 'Vacaciones', i, 4)
            Mes1 = FE.readData(ruta, 'Vacaciones', i, 5)
            Dia1 = FE.readData(ruta, 'Vacaciones', i, 6)
            Mes2 = FE.readData(ruta, 'Vacaciones', i, 7)
            Dia2 = FE.readData(ruta, 'Vacaciones', i, 8)
            Adul = FE.readData(ruta, 'Vacaciones', i, 9)
            Menor = FE.readData(ruta, 'Vacaciones', i, 10)
            Opcion = FE.readData(ruta, 'Vacaciones', i, 11)
            Presupuesto = FE.readData(ruta, 'Vacaciones', i, 12)
            Nom = FE.readData(ruta, 'Vacaciones', i, 13)
            Ape = FE.readData(ruta, 'Vacaciones', i, 14)
            Nac = FE.readData(ruta, 'Vacaciones', i, 15)
            Email = FE.readData(ruta, 'Vacaciones', i, 16)
            Cmovil = FE.readData(ruta, 'Vacaciones', i, 17)
            Pais = FE.readData(ruta, 'Vacaciones', i, 18)
            NumC = FE.readData(ruta, 'Vacaciones', i, 19)
            NumT = FE.readData(ruta, 'Vacaciones', i, 20)
            Titu = FE.readData(ruta, 'Vacaciones', i, 21)
            Fecha = FE.readData(ruta, 'Vacaciones', i, 22)
            Cod = FE.readData(ruta, 'Vacaciones', i, 23)
            DocTitu = FE.readData(ruta, 'Vacaciones', i, 24)
            print('\nEn esta prueba se realizo el plan de: {}'.format(Plan))
            C.Despegar(i, Plan, Es.Caracter(Plan, Cart1, t), Ciudad1, Ciudad2, Es.Mes(Mes1, t), Dia1, Es.Mes(Mes2, t), Dia2, Adul, Menor, Opcion, Presupuesto, Nom, Ape, Nac, Email, Cmovil, Pais, NumC, NumT
                       , Titu, Fecha, Cod, DocTitu, ruta, t)
        else:
            print('finalizo')
            V.Tiempo(t)