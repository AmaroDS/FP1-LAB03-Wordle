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
        

       
        



# TODO: Escribe la cabecera completa e implementa la función marcar_verdes

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
    # TODO: Implementa esta función
    return "_____"  # Elimina esta línea cuando la implementes


