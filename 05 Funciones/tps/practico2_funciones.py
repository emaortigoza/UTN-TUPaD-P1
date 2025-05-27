#1)Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

#Definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")


#Programa principal
imprimir_hola_mundo()

#2)Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

#Definicion de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}, que tengas un buen dia!")
#Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3)Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.


#Definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
#Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math
#Definicion de funciones
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El area del circulo es: {area}")
    return area
    
def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo es: {perimetro}")
    return perimetro

#Programa principal
radio = float(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función

#Definicion de funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas")
    return horas

#Programa principal
segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
import utils
#Definicion de funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#programa principal
numero = utils.leer_entero_validado("Ingrese un numero para ver su tabla de multiplicar: ", 1)
tabla_multiplicar(numero)


#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

#Definicion de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    
    print(f"Resultados:\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multiplicacion}\nDivisión: {division}")
    return (suma, resta, multiplicacion, division)

#Programa principal
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)



#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


#Definicion de funciones
def calcular_imc(peso, altura):
    if altura <= 0:
        print("Error: La altura debe ser mayor que cero.")
        return None
    imc = peso / (altura ** 2)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
    return imc



#Programa principal

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

calcular_imc(peso, altura)

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#Definicion de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")
    return fahrenheit


#Programa principal

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit (celsius)


#10-Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función

#Definicion de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de los numeros {a}, {b} y {c} es: {promedio}")
    return promedio


#Programa principal
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))
calcular_promedio(a, b, c)