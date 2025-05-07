# Desarrollar un algoritmo que permita ingresar una cantidad de personas. La computadora debe pedir la edad de cada una y finalmente mostrar el porcentaje de personas que es mayor de edad.

EDAD_MINIMA = 18
cantidad_personas = int(input("Ingrese la cantidad de personas: "))
cantidad_personas_mayores = 0


for i in range(cantidad_personas):
     print("Ingrese la edad n°", i +1, ":")
     edad = int(input())
     if edad >= EDAD_MINIMA:
          cantidad_personas_mayores += 1
     
porc = (cantidad_personas_mayores / cantidad_personas) * 100
print("El porcentaje de personas mayores de edad es:", porc, "%")