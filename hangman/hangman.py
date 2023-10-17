import random
import string

#Las palabras las tenemos en un archivo separado. Importamos un elemento de un archivo, que nosotros queramos.
from palabras import palabras
from vidas_diagrama import vidas_diccionario_visual

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

    letras_adivinadas = set()
    #Este set lo inicializamos con un set vacio, para crear un conjunto nuevo, que no tendrá nada inicialmente. 
    
    abecedario = set(string.ascii_uppercase)
    #Nos retornará un diccionario con todas las letras en mayuscula, escepto la ñ. Se puede agregar manualmente.

    vidas = 7
    #Trabaja junto al archivo vidas_diagrama, como un diccionario visual. Dependiendo de la cantidad de vidas, se visualizará un diagrama. 
    
    while len(letras_por_adivinar) > 0 and vidas > 0 :
        #Mensaje inicial para informar al usuario de sus vidas y las letras adivinadas.
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}.")

        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) # mostrar estado del ahorcado.
        print(f"Palabra: {' '.join(palabra_lista)}") #Mostrar las letras separadas por un espacio.

        letra_usuario = input("Escoge una letra: ").upper() #Toma la letra ingresada y la pasa a mayuscula, guardandola en la variable.

        #Si la letra escogida por el usuario, esta en el diccionario y no está en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #Nos preguntamos si la letra esta en la palabra por adivinar, o no.
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('') #Si la letra está, se quita de la lista de palabras pendientes por adivinar.
            else: #Si no está, le sacamos una vida.
                vidas = vidas - 1
                print(f'\n Tu letra, {letra_usuario} no está en la palabra.')
        #Si la letra elegida por el usuario ya fue ingresada.
        else:
            print(f"\nYa escogiste esa letra. Por favor, elige una letra nueva.")
