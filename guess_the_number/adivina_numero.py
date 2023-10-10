import random #nos da acceso a todos los elementos del modulo random de Python


def adivina_el_numero(x):

    print("==================================")
    print("    ¡Bienvenido/a al Juego!       ")
    print("==================================")
    print("Tu meta es adivinar el número generado por la computadora.")
    
    #randint es rand por random int por entero. Lo que devuelve un numero entero aleatorio. 
    #Recibe dos parametros: a y b. El numero que se genera, va a ser mayor o igual a a, y menor o igual a b.
    numero_aleatorio = random.randint(1, x)

    prediccion = 0 #el valor inicial lo ponemos en 0 para que no coincida de ninguna manera con el numero random. Si le asignamos 1, por ejemplo, y el numero random es 1, el usuario no tiene rondas para jugar porque el número ya está adivinado.

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: ")) #El valor que ingrese el usuario, por el input, se asignará a la variable prediccion. El int inicial, trabaja lo ingresado como un número, ya que input siempre toma lo ingresado como string.

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. El número que ingresaste es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. El número que ingresaste es muy grande.")

    print(f"¡Felicitaciones! ¡Adivinaste el número! Era el {numero_aleatorio}.")


adivina_el_numero(10) #el parametro es x, pero cuando llamo a la función debo darle el numero para que establezca el juego, con un numero random entre 1 y 10.