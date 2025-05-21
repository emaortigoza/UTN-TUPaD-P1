#Definicion de funciones

def siguiente (num):
    return num + 1  

def doble (num):
    return num * 2

#programa prinicipal
print(siguiente(8)) #9
siguiente_de_5 = siguiente(5)
print (f"EL siguiente de 5 es {siguiente_de_5}") #6


print(doble(siguiente(5))) #12