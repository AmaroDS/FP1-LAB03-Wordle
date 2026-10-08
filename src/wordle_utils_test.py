# Pruebas para las funciones de wordle_utils.py

from wordle_utils import *
from datetime import datetime


def test_es_palabra_valida():
    print("Probando es_palabra_valida...")
    assert es_palabra_valida("casar") == True
    assert es_palabra_valida("casa") == False
    assert es_palabra_valida("casarr") == False
    assert es_palabra_valida("c4sar") == False
    assert es_palabra_valida("casa ") == False
    assert es_palabra_valida(" casa") == False
    assert es_palabra_valida("CASAR") == True

def test_calcula_minutos_y_segundos():
    print("Probando es_palabra_valida...")
    assert calcula_minutos_y_segundos(datetime(2024, 1, 1, 23, 0, 0), datetime(2024, 1, 1, 23, 0, 30)) == (0, 30)
    assert calcula_minutos_y_segundos(datetime(2024, 1, 1, 23, 0, 0), datetime(2024, 1, 1, 23, 3, 45)) == (3, 45)
    assert calcula_minutos_y_segundos(datetime(2024, 1, 1, 23, 0, 0), datetime(2024, 1, 2, 0, 1, 15))==(61, 15)

def test_quitar_letra():
    print
    assert quitar_letra("casar", "a") == "csar"
    assert quitar_letra("casar", "c") == "asar"
    assert quitar_letra("casar", "r") == "casa"
    assert quitar_letra("casar", "z")== "casar"
    assert quitar_letra("aaaaa", "a") =="aaaa"
     
test_quitar_letra()
test_es_palabra_valida()
test_calcula_minutos_y_segundos()
print("✅Todas las pruebas pasaron correctamente.")