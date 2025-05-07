#Desarrollar un algoritmo que permita ingresar el nombre y la edad ( por separado) de diferentes personas. La carga termina cuando cuando en el nombre de la proxima persona se ingresa un asterisco (*). La computadora debe mostrar como se llama la persona mas joven

CORTE = "*"
NOMBRE_INVALIDO = "xxxxxxxxxx"
edad_min = float("inf")
nombre_joven = NOMBRE_INVALIDO

nombre = input("Ingrese su nombre ("+ CORTE +" para terminar): ")

while nombre != CORTE:
     edad = int(input("Ingrese su edad de " + nombre + ": "))
     if edad < edad_min:
          edad_min = edad
          nombre_joven = nombre
     nombre = input("Ingrese otro nombre ("+ CORTE +" para terminar): ")

if nombre_joven == NOMBRE_INVALIDO:
     print("No se ingresaron nombres")
else:
     print("La persona más joven ( ", edad_min ," años) es : ", nombre_joven)