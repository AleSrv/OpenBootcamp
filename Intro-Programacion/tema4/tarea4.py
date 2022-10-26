# if
numeroIf = 0

if (numeroIf > 0):
    print("Número Positivo")
elif(numeroIf < 0):
    print("Número Negativo")
else:
    print("El Número es 0")

#while

numeroWhile = 0

while (numeroWhile < 3):
    print(numeroWhile)
    numeroWhile +=1

#Do while
numeroWhile = 0

while True:
    print(numeroWhile)
    numeroWhile +=1
    if (numeroWhile < 3):
        break

# bucle for
numeroFor = 0

for numeroFor in range(3):
    print(numeroFor)
    numeroFor +=1

#Switch (Python no hay switch)

estacion = "verano"

def switch (estacion):
    if (estacion == "verano"):
        print("Es verano")
    elif (estacion == "invierno"):
        print("Es invierno")
    elif (estacion == "primavera"):
        print("Es primavera")
    elif (estacion == "otoño"):
        print("Es otoño")
    else:
        print("No es una estacion")

switch(estacion)






