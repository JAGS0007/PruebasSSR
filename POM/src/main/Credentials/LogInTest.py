# Equipo de QA
import time, sys, os
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import *
from ldap3 import Server, Connection, ALL, NTLM
from PIL import Image, ImageTk
from POM.src.main.Basic.FuncionesTest import Variables_Globales

#Este sección esta en construcción Es un adicional para demostrar mis conocimiento en el lenguaje
criteria = "(&(objectClass=user)(sAMAccountName=username))"
attributes = ['displayName', 'company']
dominio = 'DC=Despegar, DC=CORP'

def resource_path(relative_path):
    """Ing. De QA Jimmy Salcedo """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Ventana():

    def __init__(self, driver):
        self.driver = driver

    def ventana(self, t1):
        validate = lambda text: text.isdecimal()
        VentanaPrincipal = Tk()
        VentanaPrincipal.title("Inicio de sesión")
        VentanaPrincipal.state('zoomed')
        window_width = VentanaPrincipal.winfo_screenwidth()
        window_height = VentanaPrincipal.winfo_screenheight()
        background_image = Image.open(resource_path("Despegar.jpg"))
        image2 = background_image.resize((window_width, window_height))#, Image.ANTIALIAS)
        imagen2 = ImageTk.PhotoImage(image2)
        label_imagen1 = ttk.Label(VentanaPrincipal, image=imagen2).place(x=0, y=0, relwidth=1, relheight=1)
        image = Image.open(resource_path("Despegar2.png"))
        width, height = image.size
        window_width = 25  # Nuevo ancho deseado
        new_height = int(height * (window_width / width))
        image = image.resize((window_width, new_height))#, Image.ANTIALIAS)
        imagen = ImageTk.PhotoImage(image)
        label_imagen = ttk.Label(VentanaPrincipal, image=imagen).place(anchor='nw')
        Sesion = Frame(VentanaPrincipal, bg='white')
        Sesion.place(relheight=0.5, relwidth=0.25, relx=0.28, rely=0.25)
        list_label = ttk.Label(Sesion, text="Bienvenidos a la prueba de automatización", font=("Arial", 16),
                               background='white').place(relx=0.075, rely=0.05)
        list_label = ttk.Label(Sesion, text="        _____________________________________________        ",
                               font=("Arial", 12), foreground='#A3AFBD', background='white').place(relx=0, rely=0.15)
        usuario_label = ttk.Label(Sesion, text="USUARIO", font=("Arial", 10), foreground='#475F7B',
                                  background='white').place(relx=0.075, rely=0.25)
        usuario_entry = ttk.Entry(Sesion, width=45, font=("Arial", 12))
        usuario_entry.place(relx=0.075, rely=0.3)
        contraseña_label = ttk.Label(Sesion, text="CONTRASEÑA", font=("Arial", 10), foreground='#475F7B',
                                     background='white').place(relx=0.075, rely=0.4)
        contraseña_entry = ttk.Entry(Sesion, show="*", width=45, font=("Arial", 12))
        contraseña_entry.place(relx=0.075, rely=0.45)

        def on_select(event):
            global selected_option, selected_value
            selected_option = lista_list.get()
            selected_value = option_values[selected_option]

        option_values = {
            "": 0, "Alojamiento": 1, "Vuelo": 2, "Paquete": 3
        }
        selected_option, opcionRadioButton = tk.StringVar(), tk.StringVar()
        list_label = ttk.Label(Sesion, text="Información", font=("Arial", 10), foreground='#475F7B', background='white').place(
            relx=0.075, rely=0.55)
        lista_list = ttk.Combobox(Sesion, width=43, textvariable=selected_option, values=list(option_values.keys()),
                                  state="readonly", font=("Arial", 12))
        lista_list.place(relx=0.075, rely=0.6)
        Numero_label = ttk.Label(Sesion, text="Valor de presupuesto", font=("Arial", 10), foreground='#475F7B',
                                 background='white').place(relx=0.075, rely=0.7)
        Numero_entry = ttk.Entry(Sesion, validate="key", validatecommand=(VentanaPrincipal.register(validate), "%S"),
                                 width=45, font=("Arial", 12))
        Numero_entry.place(relx=0.075, rely=0.75)
        global ValorBoton
        ValorBoton = 0

        def Boton(Valor):
            global ValorBoton
            ValorBoton = Valor

        QA_boton = tk.Radiobutton(Sesion, bg='white', text='Equipo 1', value=1, variable=opcionRadioButton,
                                  command=lambda: Boton(1))
        QA_boton.place(relx=0.2, rely=0.85)
        DEV_boton = tk.Radiobutton(Sesion, bg='white', text='Equipo 2', value=2, variable=opcionRadioButton,
                                   command=lambda: Boton(2))
        DEV_boton.place(relx=0.65, rely=0.85)
        opcionRadioButton.set(None)

        def enviar_datos():
            global Valid, usuario, contraseña, Propiedad1
            usuario, contraseña, Numero, Propiedad1, lista, lista2 = 'Despegar\\' + usuario_entry.get(), contraseña_entry.get(), Numero_entry.get(), 0, \
            option_values[lista_list.get()], lista_list.get()
            if usuario_entry.get() == '' and contraseña == "" and lista == 0 and Numero == "" and ValorBoton == 0:
                messagebox.showerror("Invalidación",
                                     "Ingrese y Selecione los siguientes campos: \n\n- Usuario \n- Contraseña \n- RQ \n- Numero del RQ \n- Ambiente")
            elif usuario_entry.get() == '':
                messagebox.showerror('Invalidación', 'Ingrese el campo: \n\nUsuario')
            elif contraseña == '':
                messagebox.showerror('Invalidación', 'Ingrese el campo: \n\nContraseña')
            elif lista == 0:
                messagebox.showerror('Invalidación', 'Selecione: \n\nEl tipo de RQ')
            elif Numero == '':
                messagebox.showerror('Invalidación', 'Ingrese el campo: \n\nNumero de RQ')
            elif ValorBoton == 0:
                messagebox.showerror('Invalidación', 'Selecione: \n\nUn ambiente')
            else:
                server = Server('ldaps://Despegar', get_info=ALL, use_ssl=True)
                conn = Connection(server, user=usuario, password=contraseña, authentication=NTLM)  # , auto_bind=True)
                Valid = conn.bind()
                if Valid == True and lista != 0 and Numero != '' and ValorBoton == 1:
                    print('Es del equipo 1<br>')
                    print('El usuario ingresado es: ' + str(usuario_entry.get()) + '<br>')
                    print('Descripcion: ' + str(lista2) + ' - ' + str(Numero) + '<br>')
                    Propiedad1 = 1
                elif Valid == True and lista != 0 and Numero != '' and ValorBoton == 2:
                    print('Es del equipo 2<br>')
                    print('El usuario ingresado es: ' + str(usuario_entry.get()) + '<br>')
                    print('Descripcion: ' + str(lista2) + ' - ' + str(Numero) + '<br>')
                    Propiedad1 = 2
                else:
                    messagebox.showerror("Invalidación",
                                         "Las credenciales de usuario son invalidas\n\nPorfavor intente nuevamente\n\n\nNOTA:\nRecuerde si ingreso su usuario bien y la contraseña erronea\nDespues de 3 intentos se bloqueara su cuenta de ingreso")

            if Propiedad1 == 1 or Propiedad1 == 2:
                global user, password
                user, password = 'Despegar\\' + usuario_entry.get(), contraseña_entry.get()
                time.sleep(t1)
                conn.unbind()
                VentanaPrincipal.destroy()

        def bind_enter(event):
            enviar_datos()

        usuario_entry.focus_set()
        usuario_entry.bind("<Return>", bind_enter)
        contraseña_entry.bind("<Return>", bind_enter)
        lista_list.bind("<Return>", bind_enter)
        lista_list.bind("<<ComboboxSelected>>", on_select)
        Numero_entry.bind("<Return>", bind_enter)
        QA_boton.bind("<Return>", bind_enter)
        DEV_boton.bind("<Return>", bind_enter)
        enviar_button = tk.Button(Sesion, width=57, text="INGRESAR", command=enviar_datos, bg='#2c6de9', fg='white').place(
            relx=0.075, rely=0.92)
        VentanaPrincipal.wm_attributes('-topmost', 1)
        VentanaPrincipal.mainloop()
        driver = self.driver
        C = Variables_Globales(driver)
        C.Credenciales(str(user), str(password), t1)