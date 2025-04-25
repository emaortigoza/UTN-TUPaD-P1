cant_numeros = 5
sumatoria = 0

for cont in range(cant_numeros):
    print("Ingrese un numero: ")
    num = int(input())
    sumatoria += num # sumatoria = sumatoria + num
    

print("La sumatoria es: ", sumatoria)
print("El promedio es: ", (sumatoria / cant_numeros))

