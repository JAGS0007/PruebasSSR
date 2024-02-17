import datetime
import pyautogui
from POM.src.main.Basic.FuncionesTest import Variables_Globales
from POM.src.main.Anex.ResultadoTest import Resultado
from selenium.common.exceptions import TimeoutException


class Consultar():

    def __init__(self, driver):
        global V, Result
        self.driver = driver
        V = Variables_Globales(self.driver)
        Result = Resultado(self.driver)

    def Despegar(self, i, Plan, Cart1, Ciudad1, Ciudad2, Mes1, Dia1, Mes2, Dia2, Adul, Menor, Opcion, Presupuesto, Nom, Ape, Nac, Email, Cmovil, Pais, NumC, NumT
                       , Titu, Fecha, Cod, DocTitu, ruta, t):
        date = datetime.datetime.now()
        '''if Plan == 'Alojaminetos':
        elif Plan == 'Vuelos':
        elif Plan == 'Paquetes':'''
        V.Click_Mix('link', Plan, t)
        if Plan == 'Alojamientos':
            try:
                V.Click_Mix('xpath','//*[@id="searchbox-sbox-box-hotels"]/div/div/div/div/div[2]/div[2]/div/div/div[{}]'.format(Cart1),t)
                V.Text_Mix('xpath', "//input[contains(@placeholder,'Ingresa una ciudad, alojamiento o punto de interés')]", Ciudad1, t)
                pyautogui.press('tab')
                if Mes1 == date.month:
                    V.Click_Mix('xpath', '//*[@id="searchbox-sbox-box-hotels"]/div/div/div/div/div[3]/div[2]/div/div[1]/div/div/div', t)
                    V.Click_Mix('xpath', "//*[@id='component-modals']/div[1]/div[1]/div/div[1]/div[3]/div[{}]".format(Dia1), t)
                if Mes2 >= date.month:
                    V.Click_Mix('xpath', "//*[@id='component-modals']/div[1]/div[1]/div/div[1]/div[3]/div[{}]".format(Dia2), t)
                V.Click_Mix('xpath', '//*[@id="component-modals"]/div[1]/div[2]/div[1]/button', t)
                V.Click_Mix('xpath', '//*[@id="searchbox-sbox-box-hotels"]/div/div/div/div/div[3]/div[3]/div', t)
                V.Tiempo(t)
                V.Click_Mix('xpath', '//*[@id="component-modals"]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/button[2]', t)
                V.Click_Mix('xpath', '//*[@id="component-modals"]/div[2]/div/div/div[2]/a[1]', t)
                V.Click_Mix('xpath', '//*[@id="searchbox-sbox-box-hotels"]/div/div/div/div/div[3]/button', t)
            except TimeoutException as ex:
                assert False, 'No existe'
            Result.Despegar(i, ruta, 'id', 'curPage', t)