import random

def adivina_el_numero(x):

    print("==================================")
    print("    ¡Bienvenido/a al Juego!       ")
    print("==================================")
    print("Tu meta es adivinar el número generado por la computadora.")
    
    #randint es rand por random int por entero. Lo que devuelve un numero entero aleatorio. 
    #Recibe dos parametros: a y b. El numero que se genera, va a ser mayor o igual a a, y menor o igual a b.
    numero_aleatorio = random.randint(1, x)