import random


def jugar(): #va en parentesis sin argumentos, porque no recibirá parametros. Solo se ejecuta llamando a la función.
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, o 'ti' para tijeras.\n").lower() #convertimos la respuesta del user en minusculas para evitar problemas.
    computadora = random.choice(['pi', 'pa', 'ti'])