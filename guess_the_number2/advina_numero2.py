import random

def adivina_el_numero_computadora(x):
    print("==================================")
    print("    ¡Bienvenido/a al Juego!       ")
    print("==================================")
    print(f"Selecciona un número entre 1 y {x} parza que la computadora intente adivinar.")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    
    #Usamos un ciclo while porque no sabemos cuántos intentos va a requerir, cuantas itereaciones vamos a necesitar
    while respuesta != "c":
        #generar predicción
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else: 
            prediccion = limite_inferior

        #Obtener respuesta del usuario.
        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C).")
