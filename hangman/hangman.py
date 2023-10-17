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

    letras_por_adivinar = set(palabra)
    # set() permite crear un conjunto, a partir de la palabra recibida, de letras sin que se repitan. Ejemplo: si la palabra es "MOONGOSE", el conjunto se guardaria como {'M', 'O', 'N', 'G', 'S', 'E'} (Es decir: la letra O no se guardará más de una vez.)
    letras_adivinadas = 
    abecedario = 