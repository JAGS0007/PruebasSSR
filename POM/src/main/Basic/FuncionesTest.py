import time, pyautogui, keyboard

from allure_commons.types import AttachmentType
import pytest, datetime, allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Variables_Globales():

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, times):
        t = time.sleep(times)
        return t

    def Captura(self, producto, times):
        self.Tiempo(times)
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        allure.attach(self.driver.get_screenshot_as_png(), name='Captura_{}_{}'.format(producto,timestamp), attachment_type=AttachmentType.PNG)

    def Navegador(self, url, times):
        self.driver.get(url)
        self.driver.maximize_window()
        print('\nPagina abierta:\n'+ str(url))
        self.Tiempo(times)

    def Credenciales(self, usuario, contraseña, times):
        keyboard.write(usuario)
        pyautogui.press("tab")
        keyboard.write(contraseña)
        time.sleep(times)
        pyautogui.press("enter")
        self.Tiempo(times)

    #Funcion para validar Xpath
    def selXpath(self, elemento, times):
        self.Tiempo(times)
        val = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script('arguments[0].scrollIntoView();', val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def selId(self, elemento, times):
        self.Tiempo(times)
        val = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script('arguments[0].scrollIntoView();', val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def selLink(self, elemento, times):
        self.Tiempo(times)
        val = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, elemento)))
        val = self.driver.execute_script('arguments[0].scrollIntoView();', val)
        val = self.driver.find_element(By.LINK_TEXT, elemento)
        return val

    def selCss(self, elemento, times):
        self.Tiempo(times)
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
        val = self.driver.execute_script('arguments[0].scrollIntoView();', val)
        val = self.driver.find_element(By.CSS_SELECTOR, elemento)
        return val

    #Funcion texto Xpath y ID
    def Text_Mix(self, tipo, selector, texto, times):
        if(tipo=='xpath'):
            try:
                val = self.selXpath(selector, times)
                val.send_keys(texto)
                print('Escribiendo en el campo {} con el texto -> {} '.format(selector, texto))
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)
        elif (tipo == 'id'):
            try:
                val = self.selId(selector, times)
                val.send_keys(texto)
                print('Escribiendo en el campo {} con el texto -> {} '.format(selector, texto))
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)

    #Funcion Click Xpath y ID
    def Click_Mix(self, tipo, selector, times):
        if (tipo == 'xpath'):
            try:
                val = self.selXpath(selector, times)
                print('Dar click en el campo -> {} '.format(selector))
                val.click()
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)
        elif (tipo == 'id'):
            try:
                val = self.selId(selector, times)
                val.click()
                print('Dar click en el campo -> {} '.format(selector))
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento:\n'+ selector)
        elif (tipo == 'link'):
            try:
                val = self.selLink(selector, times)
                print('Dar click en el campo -> {} '.format(selector))
                val.click()
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)
        elif (tipo == 'css'):
            try:
                val = self.selCss(selector, times)
                print('Dar click en el campo -> {} '.format(selector))
                val.click()
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)

    # Funcion Selecionar
    def Select_Mix_Type(self, localizador, selector, tipo, dato, times):
        if (localizador == 'xpath'):
            try:
                val = self.selXpath(selector, times)
                val = Select(val)
                if (tipo == 'texto'):
                    val.select_by_visible_text(dato)
                elif (tipo == 'index'):
                    val.select_by_index(dato)
                elif (tipo == 'value'):
                    val.select_by_value(dato)
                print('El campo seleccionado es -> {} '.format(dato))
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)
        elif (localizador == 'id'):
            try:
                val = self.selId(selector, times)
                val = Select(val)
                if (tipo == 'texto'):
                    val.select_by_visible_text(dato)
                elif (tipo == 'index'):
                    val.select_by_index(dato)
                elif (tipo == 'value'):
                    val.select_by_value(dato)
                print('El campo seleccionado es -> {} '.format(dato))
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)

    #Funcion Cargar Archivo
    def Upload_Mix(self, tipo, selector, ruta, times):
        if (tipo == 'xpath'):
            try:
                val = self.selXpath(selector, times)
                val.send_keys(ruta)
                print('Se carga el archivo -> {} '.format(ruta))
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento:\n' + tipo)
        elif (tipo == 'id'):
            try:
                val = self.selId(selector, times)
                val.send_keys(ruta)
                print('Se carga el archivo -> {} '.format(ruta))
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento:\n' + tipo)

    def Check_Mix_Multiplex(self, tipo, times, *args):
        if (tipo == 'xpath'):
            try:
                for num in args:
                    val = self.selXpath(num, times)
                    val.click()
                    print('Se carga el archivo -> {} '.format(num))
            except TimeoutException as ex:
                for num in args:
                    print(ex.msg)
                    print('No se encontro el elemento:\n' + num)
        elif (tipo == 'id'):
            try:
                for num in args:
                    val = self.selId(num, times)
                    val.click()
                    print('Se carga el archivo -> {} '.format(num))
            except TimeoutException as ex:
                for num in args:
                    print(ex.msg)
                    print('No se encontro el elemento:\n' + num)

    def Existe(self, tipo, selector, times):
        if (tipo == 'link'):
            try:
                val = self.selLink(selector, times)
                print('El elemento {} -> existe '.format(selector))
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)
                return "No Existe"
        elif (tipo == 'xpath'):
            try:
                val = self.selXpath(selector, times)
                print('El elemento {} -> existe '.format(selector))
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)
                return "No Existe"
        elif (tipo == 'id'):
            try:
                val = self.selId(selector, times)
                print('El elemento {} -> existe '.format(selector))
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print('No se encontro el elemento: -> ' + selector)
                return "No Existe"