print("Hola")

while 2 == 3:
     print("Debo aprender ciclos")
print("Fin del programa")
print("/////////////////")
# while <condicion>:
#     <instrucciones>

while 2 == 2:
    print("Debo aprender ciclos")
print("Fin del programa")
print("/////////////////")
# se genera un bucle infinito porque la condicion es siempre verdadera

# while _ bandera:

umbral = 10
sumatoria = 0
cont = 0
while sumatoria < umbral:
    cont += 1 # cont = cont + 1
    print("Ingrese un numero: ")
    num = int(input())
    sumatoria += num # sumatoria = sumatoria + num

print ("El promedio es: ", (sumatoria / cont))

