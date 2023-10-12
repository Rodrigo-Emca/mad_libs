import random


def jugar(): #va en parentesis sin argumentos, porque no recibirá parametros. Solo se ejecuta llamando a la función.
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel, o 'ti' para tijeras.\n").lower() #convertimos la respuesta del user en minusculas para evitar problemas.
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return '¡Empate!'
    if gano_el_jugador(usuario, computadora):
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def gano_el_jugador(jugador, oponente):
    # Retornar True si gana el jugador. 
    # Tres posibilidades para ganar:
        # Piedra gana a Tijera
        # Tijera gana a Papel
        # Papel gana a Piedra
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else: 
        return False
    

print(jugar())