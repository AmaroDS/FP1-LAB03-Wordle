from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    return len(cadena) == 5 and cadena.isalpha()

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """ 
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.
    

    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """
    diferencia = fin - inicio
    minutos= int(diferencia.total_seconds()) // 60
    segundos = int(diferencia.total_seconds()) % 60 #hacemos el módulo porque el resto nos da los segundos

    return minutos, segundos


def quitar_letra(cadena: str, letra: str) -> str:
    res = "" #variable que guarda letras
    borra = True
    for i in cadena:
        if letra != i or not borra:
            res += i
        else:
            borra = False
    return res

def marcar_verdes(palabra_secreta: str, intento: str) -> tuple :
    verdes = ""
    restantes = ""

    for i in range(5):
        if palabra_secreta[i] == intento[i]:
            verdes += "V"
        else:
            verdes += "_"
            restantes += palabra_secreta[i]
    return verdes, restantes

def marcar_amarillos(intento: str, verdes: str, restantes: str) -> str:
    colores = ""

    for i in range (0,5):
        if verdes[i] == "V":
            colores += "V"
        else:
            if intento[i] in restantes:
                colores += "A"
                restantes = restantes.replace(intento[i], "", 1)
            else:
                colores += "_"
    return colores

# TODO: Escribe la cabecera completa e implementa la función marcar_amarillos

def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """
    verdes, restantes = marcar_verdes(palabra_secreta, intento)
    return marcar_amarillos(intento, verdes, restantes)


