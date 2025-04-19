EDAD_MINIMA = 21
edad = int(input("Ingrese su edad: "))
categoria = input("Ingrese su categoria (A, B, C, D, E, F, G): ").upper()

if edad >= EDAD_MINIMA and categoria == "D":
     print("Puede conducir ambulancias")
else:
     print("No puede conducir ambulancias")
# El operador and se utiliza para combinar dos condiciones. Ambas condiciones deben ser verdaderas para que la expresión completa sea verdadera.