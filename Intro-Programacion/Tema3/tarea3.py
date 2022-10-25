# Primera parte:

def suma(a ,b , c):
    resultado = a + b + c
    return resultado


print("ingrese el primer valor:")
a = float(input("> :"))
print("ingrese el segundo valor:")
b = float(input("> :"))
print("ingrese el tercer valor:")
c = float(input("> :"))

print("la suma de todos los numeros es:" , suma(a,b,c))

# Segunda parte:


class claseCoche:
    def __init__(self , puertas):
        self.puertas =  puertas

    def suma_puerta (self):
        self.puertas = self.puertas + 1


print("\n")
micoche = claseCoche(2)
print("Cantidad de puertas del coche: ", micoche.puertas)

micoche.suma_puerta()
print("Cantidad de puertas del coche ahora: " , micoche.puertas)