#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

numero = 0
while numero <= 100:
    print(numero)
    numero += 1


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
contador = 0
while numero != 0:
    numero //= 10
    contador += 1
print("La cantidad de dígitos es:", contador)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma = 0
for i in range(valor1 + 1, valor2):
    suma += i
print("La suma de los números enteros entre", valor1, "y", valor2, "es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero = int(input("Ingrese un número entero (0 para salir): "))
suma = 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número entero (0 para salir): "))
print("La suma total es:", suma)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False
while not adivinado:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_secreto:
        adivinado = True
    else:
        print("Intenta nuevamente.")
print("¡Felicidades! Adivinaste el número en", intentos, "intentos. El número era:", numero_secreto)

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente

numero = 100
while numero >= 0:
    if numero % 2 == 0:
        print(numero)
    numero -= 1


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print("La suma de los números desde 0 hasta", numero, "es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numeros = []
for i in range(10):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)
    pares = sum(1 for num in numeros if num % 2 == 0)
    impares = sum(1 for num in numeros if num % 2 != 0)
    negativos = sum(1 for num in numeros if num < 0)
    positivos = sum(1 for num in numeros if num > 0)
    ceros = sum(1 for num in numeros if num == 0)
    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)
    print("Cantidad de números negativos:", negativos)
    print("Cantidad de números positivos:", positivos)
    
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 10 #cambiar este valor para probar con 100 números
numeros = []

print("Ingrese", cantidad_numeros, "números enteros:")

for i in range(cantidad_numeros):
    while True:
        try:
            numero = int(input(f"Número {i + 1}: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

media = sum(numeros) / cantidad_numeros
print(f"La media de los números ingresados es:", {media})


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = int(input("Ingrese un número entero: "))
numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10

print("El número invertido es:", numero_invertido)