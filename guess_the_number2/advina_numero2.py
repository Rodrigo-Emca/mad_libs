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
        #Usamos .lower para prevenir que el usuario ingrese una letra en minuscula.
        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C).").lower

        if respuesta == "a":
            limite_superior = prediccion - 1
            #Frente a la respuesta del usuario a, la computadora reformulara su predicción restandole 1.
            # Si el usuario piensa en el numero 6, la computadora predijo el numero 8, y el usuario responde "a", no hace falta buscar entre todos los numeros nuevamente, sino que debe tomar su predicción (8), restarle 1 y volver a preguntar. 
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"¡Siii! La computadora adivinó tu número correctamente: {prediccion}")
