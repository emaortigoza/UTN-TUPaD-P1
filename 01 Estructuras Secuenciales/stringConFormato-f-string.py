nombre = input("Cual es tu nombre? ")
edad = input(f"Cual es tu edad?, {nombre} ")

saludo = f"Hola {nombre}"
print(saludo)
print("Tu nombre es: ", nombre, "y tienes: ", edad, "años")
print("Tu nombre es: " + nombre + " y tienes: " + str(edad) + " años")
print(f"Tu nombre es: {nombre} y tienes: {edad} años")