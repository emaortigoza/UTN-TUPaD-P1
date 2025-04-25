# usamos la funcion print para mostrar un mensaje en pantalla
print ("Hola Mundo")
# usamos la funcion input para pedir un dato al usuario
nombre = input("Cual es tu nombre? ")
# usamos la funcion print para mostrar un mensaje en pantalla
print ("Hola", nombre)
# usamos la funcion input para pedir un dato al usuario
edad = input("Cual es tu edad? ")
# usamos la funcion print para mostrar un mensaje en pantalla
print ("Hola", nombre , "tienes", edad, "años")

# usamos la funcion input para pedir un numero entero al usuario
numero_entero = input("Dame un numero entero: ")
# convertimos (casteamos) el dato a entero con int()
numero_entero = int(numero_entero)
# usamos la funcion print para mostrar un mensaje en pantalla
print ("El numero entero es: ", numero_entero)

# usamos la funcion input para pedir un numero decimal al usuario
numero_decimal = input("Dame un numero decimal: ")
# convertimos (casteamos) el dato a decimal con float()
numero_decimal = float(numero_decimal)
# usamos la funcion print para mostrar un mensaje en pantalla
print ("El numero decimal es: ", numero_decimal)

# operamos con los numeros ingresados
suma = numero_entero + numero_decimal
# usamos la funcion print para mostrar un mensaje en pantalla
print ("La suma es: ", suma)
# operamos con los numeros ingresados
resta = numero_entero - numero_decimal
# usamos la funcion print para mostrar un mensaje en pantalla
print ("La resta es: ", resta)