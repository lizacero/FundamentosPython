#CONDICIONALES

vidaPlayer = int(input("¿Cuál es la vida del Player?: "))
if vidaPlayer > 80:
    print("Estás bien de salud")
    print("Barra de vida Verde")
elif vidaPlayer >40 and vidaPlayer <=80:
    print("Tienes salud intermedia")
    print("Barra de vida Amarilla")
elif vidaPlayer >1 and vidaPlayer <=40:
    print("Tienes salud baja, ALERTA")
    print("Barra de vida Roja")
else:
    print("Has muerto")


#CÍCLICAS
#FOR

numero = 0
for numero in[1,2,3,4]:
    print(numero)
for numero in range(1,21):
    if numero == 5:
        continue   #se salta este valor
    print("La variable numero tiene un valor de:",numero)
print("Fin")

palabra = input("Escribe una palabra: ")
for x in palabra:
    if x == "a":
        break    #detiene la ejecución del código
    print(x)

num = int(input("Ingresa un número: "))
for i in range(1,11):
    print(num*i)

#WHILE

num2 = 0
num3 = 0
while num2 <= 10 and num3 <20:
    print (num2,num3)
    num2 +=1
    num3 +=3

