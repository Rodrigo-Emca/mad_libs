import random


def jugar(): #va en parentesis sin argumentos, porque no recibirá parametros. Solo se ejecuta llamando a la función.
    usuario = input("Escoge una opción: escribe 'piedra', 'papel' o 'tijera'.\n").lower() #convertimos la respuesta del user en minusculas para evitar problemas.
    computadora = random.choice(['piedra', 'papel', 'tijera'])
    print(f"Elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")

    if usuario == computadora:
        return '¡Empate!'
    if gano_el_jugador(usuario, computadora):
        return '¡Ganaste!'
    
    return '¡Perdiste!'


def gano_el_jugador(jugador, oponente):
    # Retornar True si gana el jugador. 
    # Tres posibilidades papelra ganar:
        # piedra gana a tijera
        # tijera gana a papel
        # papel gana a piedra
    if ((jugador == 'piedra' and oponente == 'tijera')
        or (jugador == 'tijera' and oponente == 'papel')
        or (jugador == 'papel' and oponente == 'piedra')):
        return True
    else: 
        return False
    

print(jugar())