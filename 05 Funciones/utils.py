def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
     n = int(input(f"{mensaje}"))
     while n < min or n > max:
         n = int(input(f"ERROR. {mensaje}"))
     return n   


def imprimir_simbolo(simbolo, veces):
     print(sucesion_simbolos(simbolo, veces))

def sucesion_simbolos(simbolo, veces):
     sucesion = ""
     for i in range(veces):
          sucesion += simbolo
     return sucesion