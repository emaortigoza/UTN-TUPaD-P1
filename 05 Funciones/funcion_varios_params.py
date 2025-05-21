# definicion de funciones
def obtener_resto(num1, num2):
     return num1 - num2 * (num1 // num2) #Sin usar operador %

def es_multiplo(x, y):
     return obtener_resto(x, y) == 0


#progama principal
a = int (input("Escribe un número: "))
b = int (input("Escribe otro número: "))

resto = obtener_resto(a, b)

print(f"El resto entre {a} y {b} es {resto}")
if es_multiplo(a, b):
    print(f"{a} es múltiplo de {b}")


