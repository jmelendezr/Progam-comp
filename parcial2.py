numero = int(input("Ingrese un entero positivo: "))
while (numero>1):
    if ((numero%2) == 0):
        numero = numero /2
        print (numero)
    else:
        numero = (numero*3) + 1
        print (numero)
