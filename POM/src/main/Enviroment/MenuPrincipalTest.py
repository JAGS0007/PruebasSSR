import unittest
from selenium import webdriver
from POM.src.main.Basic.NavegadorTest import Browser
from POM.src.main.Anex.LecturaDatosTest import *
import tkinter as tk

tg = 1

class Prueba(unittest.TestCase):

    def setUp(self):
        print('\nInicio del test\n')
        global B, V, LD, S, seleccionar
        chromeOptions = webdriver.ChromeOptions()
        #chromeOptions.add_argument('--headless')
        chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.maximize_window()

        #Inicializar
        B = Browser(self.driver)
        V = Variables_Globales(self.driver)
        LD = Lectura(self.driver)

    def test_Despegar(self):
        def enviar_informacion():
            seleccion = var.get()
            print("La opción seleccionada es:", seleccion)
            if seleccion == "Servicio de alojamiento":
                # Primer escenario de prueba
                root.destroy()
                print('Prueba 1 - Despegar Servicios de Alojamiento')
                B.Despegar(tg)
                V.Tiempo(tg)
                LD.Despegar(tg)
                V.Tiempo(tg)
            elif seleccion == 'Vuelos':
                root.destroy()
                # Segundo escenario de prueba
                print('Prueba 2 - Despegar Seleccionando Vuelos')
                B.Despegar(tg)
                V.Tiempo(tg)
                LD.Despegar(tg)
                V.Tiempo(tg)
            elif seleccion == 'Paquetes':
                # Tercer escenario de prueba
                root.destroy()
                print('Prueba 3 - Despegar Seleccionando Paquetes')
                B.Despegar(tg)
                V.Tiempo(tg)
                LD.Despegar(tg)
                V.Tiempo(tg)
        root = tk.Tk()
        root.title("Selección de opciones")
        var = tk.StringVar()
        def crear_opcion(texto):
            return tk.Radiobutton(root, text=texto, variable=var, value=texto)
        opcion1 = crear_opcion("Servicio de alojamiento")
        opcion2 = crear_opcion("Vuelos")
        opcion3 = crear_opcion("Paquetes")
        opcion1.pack()
        opcion2.pack()
        opcion3.pack()
        boton_enviar = tk.Button(root, text="Enviar", command=enviar_informacion)
        boton_enviar.pack()
        root.mainloop()

    def tearDown(self):
        print('\nFinal del test\n')
        self.driver.close()

if __name__ == '__main__':
    unittest.main()