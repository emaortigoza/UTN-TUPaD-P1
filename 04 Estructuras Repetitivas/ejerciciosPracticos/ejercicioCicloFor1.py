#Desarrollar un algoritmo que permita ingresar un numero entero entre 1 y 10 (inclusive). La computadora debe mostrar la tabla de multiplicar del numero ingresado

numero = int(input("Ingrese un numero entre 1 y 10 (inclusive): "))

if numero >= 1 and numero <= 10:
     print("Tabla de multiplicar del ", numero, ":")
     for i in range(1, 11):
          resultado = numero * i
          print(numero, "x", i, "=", resultado)
else:
     print("El numero ingresado no es valido. Debe ser entre 1 y 10 (inclusive).")