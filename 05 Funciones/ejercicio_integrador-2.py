#Definicion de funciones
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
     n = int(input(f"{mensaje}"))
     while n < min or n > max:
         n = int(input(f"ERROR. {mensaje}"))
     return n   

def sumatoria_divisores_propios(numero):
     sumatoria = 0
     for i in range(1, numero // 2 + 1):
          if numero % i == 0:
               sumatoria += i
     return sumatoria

def es_perfecto(numero):
    return sumatoria_divisores_propios(numero) == numero


def informar_si_numero_es_perfecto(numero):
     if es_perfecto(numero):
         print(f"El numero {numero} es perfecto")
     else:
         print(f"El numero {numero} no es perfecto")



#Programa principal
num = leer_entero_validado("Ingrese un numero natural: ", 1)
informar_si_numero_es_perfecto(num)