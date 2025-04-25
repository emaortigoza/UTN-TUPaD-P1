cant_numeros = 4
max_num = float('-inf') # -infinito
min_num = float('inf') # +infinito
pos_max = -1
pos_min = -1

for cont in range(1, cant_numeros+1):54
     print("Ingrese un numero: ", cont)
     num = int(input())
     if num > max_num:
           max_num = num
           pos_max = cont
     if num < min_num:
           min_num = num
           pos_min = cont

print("El maximo es: ", max_num, "en la posicion: ", pos_max)
print("El minimo es: ", min_num, "en la posicion: ", pos_min)
