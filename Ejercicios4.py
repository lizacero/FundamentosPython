#Ejercicios de Funciones

""" 1. Realizar una función que permita calcular la tabla de multiplicar de un número hasta el 10, 
    o hasta un valor ingresado por el usuario. """

def tabla(num,mult=10):
    print(f"TABLA DE MULTIPLICAR DEL {num}")
    for i in range(1,mult+1):
        print(f"{num} * {i} = {num*i}")

tabla(4,5)

""" 2. Realizar una función que permita recibir varias listas y combinarlas. """

def combinar(*args):
    lista_final = []
    for lista in args:
        for n in lista:
            lista_final.append(n)
    return lista_final

a=[2,4,6]
b=[True,False]
c=["Hola", "Mundo"]
d= combinar(a,b,c)

print(d)

""" 3. Hacer una función que permita llenar una lista de tamaño ingresado por el usuario y otra que
    permita recorrer y mostrar una o más listas. """

def llenar(tamaño):
    lista = [0]*tamaño
    for i in range(tamaño):
        lista[i]= int(input(f"Valor #{i}: "))
    return lista

def mostrar(*args):
    num_lista = 1
    for lista in args:
        print(f"LISTA {num_lista}: ")
        for i in lista:
            print(i,end=" ")
        print("\n")
        num_lista +=1

a= llenar(5)
b= llenar(3)
mostrar(a,b)

""" 4. Hacer una función para crear personajes con los siguientes atributos:
    Nombre, vida, daño base, arma (multiplicador de daño) y defensa"""

def crear_personaje(nombre, vida, daño_base, arma, defensa):
    personaje = {}
    personaje["nombre"] = nombre
    personaje["vida"] = vida
    personaje["daño"] = daño_base
    personaje["arma"] = arma
    personaje["defensa"] = defensa
    print("PERSONAJE CREADO EXITOSASMENTE")
    print("Nombre: ", personaje["nombre"])
    print("Vida: ", personaje["vida"])
    print("Daño: ", personaje["daño"])
    print("Multiplicador de arma: ", personaje["arma"])
    print("Defensa: ", personaje["defensa"])
    return personaje

guerrero = crear_personaje("Guerrero", 200, 100, 2, 35)

""" 5. Hacer una función que permita calcular el daño recibido po un jugador al luchar con un enemigo,
    así como el daño que recibirá el enemigo. El daño deberá ser calculado de la siguiente forma.
        Daño = (Daño base * Multiplicador de arma) -  Defensa
    Mostrar el daño realizado por el jugador y el enemigo. Si alguno muere decir quién ganó el combate. """

def calc_daño(jugador,enemigo):
    daño_jug = enemigo["daño"]*enemigo["arma"] - jugador["defensa"]
    daño_ene = jugador["daño"]*jugador["arma"] - enemigo["defensa"]

    if daño_jug < 0:
        daño_jug = 0
    if daño_ene < 0:
        daño_ene = 0

    print(f"{jugador["nombre"]} recibió {daño_jug} puntos de daño")
    print(f"{enemigo["nombre"]} recibió {daño_ene} puntos de daño")

    if daño_jug >= jugador["vida"]:
        print(f"\n{jugador["nombre"]} perdió el enfrentamiento")
    else:
        print(f"\n{jugador["nombre"]} tiene {jugador["vida"]-daño_jug} puntos de vida restantes")

    if daño_ene >= enemigo["vida"]:
        print(f"\n{enemigo["nombre"]} perdió el enfrentamiento")
    else:
        print(f"\n{enemigo["nombre"]} tiene {enemigo["vida"]-daño_ene} puntos de vida restantes")

    return daño_jug,daño_ene

guerrero = crear_personaje("Link", 100, 20, 2, 20)
slime = crear_personaje("Slime", 30, 5, 1, 5)

calc_daño(guerrero, slime)