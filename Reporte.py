import allure, pytest
from allure_commons.types import AttachmentType
from POM.src.main.Enviroment.MenuPrincipalN import PruebaDeRegresion
from selenium import webdriver
from POM.src.main.Basic.FuncionesTest import Variables_Globales

@pytest.mark.usefixtures('log_on_failure')
def test_Reporte():
    I = PruebaDeRegresion()
    # Proceso
    I.setUp()
    I.Despegar()
    I.tearDown()
    print('\nPrueba de ejemplo de reporte HTML\n')

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(webdriver.Chrome().get_screenshot_as_png(), name='Error', attachment_type=AttachmentType.PNG)