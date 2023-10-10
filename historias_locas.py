# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ____________________.

organización = "freeCodeCamp"

print("Aprende a programar con " + organización)
print("Aprende a programar con {}".format(organización))
print(f"Aprende a programar con {organización}") # f string es una forma mas simple de printear

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo plural: ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con nosotros y alcanza tus {sustantivo_plural}!"

print(madlib)