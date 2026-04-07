import random

# arreglar la s en bienvenido(s)
print("¡Bienvenidos al juego 'Adivina el número'!")
print("Intenta adivinar un número entre 1 y 100.")

#Recomiendo mantener el nombre de las variabls fiel al lenguage del resto del programa.
secreto = str(random.randint(1, 100))
intento = 0 
print(secreto) 
while True:
    user_guess = input("Introduzca su número:") 
    intento += 1

#sugiero arreglar el error de sintaxis en la linea 14 que decia user_gess en vez de user_guess
    if user_guess == secreto:  
        print("¡Felicitaciones, adivinaste el número!")
        break
    elif user_guess > secreto:  
        print("Su número es mayor que el objetivo.")
    elif user_guess < secreto:  
        print("Su número es inferior al objetivo.")