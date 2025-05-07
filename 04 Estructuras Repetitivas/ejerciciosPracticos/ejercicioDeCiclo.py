numero = int(input("Ingrese un número positivo: "))

if numero > 0:
     if numero % 2 != 0:
            numero -= 1
     cont = numero
     while cont >= 0:
            print(cont, end=" ")
            cont -= 2
else:
     print("El número no es positivo.")