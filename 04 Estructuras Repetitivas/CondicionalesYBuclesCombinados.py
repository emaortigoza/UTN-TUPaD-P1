sueldo_anual = 0
cont_meses = 1

print("Ingrese el sueldo del mes n° ", cont_meses, ": ")
sueldo_anual = float(input())
while cont_meses < 12 and sueldo_anual > 0:
    sueldo_anual += sueldo_anual
    cont_meses += 1
    print("Ingrese el sueldo del mes n° ", cont_meses, ": ")
    sueldo_anual = float(input())

    if sueldo_anual > 0:
        sueldo_anual += sueldo_anual
    print("El sueldo anual es: ", sueldo_anual)