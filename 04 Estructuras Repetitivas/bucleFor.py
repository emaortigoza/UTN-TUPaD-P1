# # El ciclo for se utiliza para iterar sobre una secuencia (como una lista, tupla o cadena) o un rango de números. En este caso, el ciclo itera desde 0 hasta 5 (6 no incluido) y en cada iteración imprime el valor de x y un mensaje.
# # El ciclo for es útil cuando se conoce de antemano el número de iteraciones que se desea realizar.

# for <variable> in range(<valor_inicial>, <valor_final>, <incremento>):
#     <instrucciones>
# for <variable> in range(<valor__fin):
for x in range(6): # va del 0 al 5 (5 no incluido)
    print(x, "Debo aprender ciclos")
print("Fin del programa")
print("/////////////////")
# for <variable> in range (<valor_inicial>, <valor_final>):
for x in range(1, 6): # Itera desde 1 hasta 5 (6 no incluido)
    print(x, "Debo aprender ciclos")
print("Fin del programa")
print("/////////////////")
# for <variable> in range (<valor_inicial>, <valor_final>, <incremento>):
for x in range(1, 10, 2): # Itera desde 1 hasta 9 (10 no incluido) con un incremento de 2
    print(x, "Debo aprender ciclos")
print("Fin del programa")
print("/////////////////")
# for <variable> in range (<valor_inicial>, <valor_final>, <incremento>):
for x in range(10, 0, -1): # Itera desde 10 hasta 1 (0 no incluido) con un decremento de 1
    print(x, "Debo aprender ciclos")
print("Fin del programa")
print("/////////////////")
