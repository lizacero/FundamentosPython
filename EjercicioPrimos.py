#Números primos

nPrimo = int(input("Ingresa un número a verificar: "))
contador = 0

for i in range(1,nPrimo+1):
    if nPrimo%i == 0:
        contador += 1

if contador == 2:
    print(f"{nPrimo} SI es un número primo")
else:
    print(f"{nPrimo} NO es un número primo")