import random

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