import random

#Las palabras las tenemos en un archivo separado. Importamos un elemento de un archivo, que nosotros queramos.
from palabras import palabras

def obtener_palabra_valida(palabras):
    #Seleccionar una palabra al azar de la lista
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in  palabra:
        palabra = random.choice(palabras)

    return palabra.upper() 


def ahorcado():

    print("==============================================")
    print("    ¡Bienvenido/a al Juego del Ahorcado!      ")
    print("==============================================")

    palabra = obtener_palabra_valida(palabras)
