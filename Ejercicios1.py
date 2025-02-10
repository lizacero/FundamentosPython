#Ejercicios de variables, inputs y operadores

""" 1. Recibir el nombre del usuario por teclado y mostrar por pantalla "Hola (nombre)"""

nombre = str(input("Escribe tu nombre "))
print("Hola", nombre)

# 2. Realiza un programa que permita leer un número y mostrar su tabla de multiplicar del 1 al 10

numero = int(input("Ingrese un número: "))
print(numero*1)
print(numero*2)
print(numero*3)
print(numero*4)
print(numero*5)
print(numero*6)
print(numero*7)
print(numero*8)
print(numero*9)
print(numero*10)

""" 3. Calcular el resultado de la siguiente operación y mostrarlo en pantalla"""

resultado= ((45-3**2)**(1/2))/(2*3) - 1
print(resultado)

""" 4. Recibir un número de tres cifras y mostrar sus dígitos del primero al último"""

cifras = int(input("Ingrese un número de 3 cifras: "))
digito1 = (cifras%1000)//100
digito2 = (cifras%100)//10
digito3 = cifras%10
print( digito1, digito2, digito3)

""" 5. En un videojuego el personaje principal recibe un aumento de daño del 10% con cada nivel que sube.
    Recibir por teclado el nivel y daño base del personaje y mostrar cuál será su daño final."""

nivel = int(input("Ingrese su nivel: "))
dahnoBase = float(input("Ingrese el daño base: "))
resultado = (dahnoBase*0.1*nivel)+dahnoBase
print(resultado)