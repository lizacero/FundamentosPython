#Ejercicios de colecciones y datos compuestos

""" 1. Hacer un programa que permita añadir un número de armas seleccionado por el usuario al arsenal de Leon y mostrarlas. """

n = int(input("Cuántas armas desea agregar al arsenal: "))
armas=[""]*n

for i in range(n):
    armas[i] = input(f"Arma #{i+1}: ")

print("\tARSENAL DE LEON")
for n in armas:
    print(n)

""" 2. Almacenar 10 números enteros en una lista, determinar los números terminados en 5 y su posición en la lista. """

numeros = [0]*10
terminados5 = {}

for i in range(10):
    numeros[i] = int(input(f"Ingrese el numero {i+1}: "))

    if numeros[i]%10 ==5:
        terminados5[i] = numeros[i]

if len(terminados5) != 0 :
    print("t\TERMINADOS EN 5")

    for x in terminados5:
        print(f"{terminados5[x]} en la posición {x}")
else:
    print("Ningún número terminado en 5")


""" 3. Recibir n números enteros por teclado, añadir a una lista los que sean primos y mostrarlos por pantalla. """

n = int(input("Números a verificar: "))
primos = []

for i in range(n):
    divisores = 0 
    numero = int(input(f"Ingrese el número {i+1}: "))

    for j in range(1,numero+1):
        if numero%j == 0:
            divisores +=1
    if divisores == 2:
        primos.append(numero)

if len(primos) != 0:
    print("\tPrimos ingresados")
    for primo in primos:
        print(primo,end=" ")
else:
    print("No se ingresaron primos")

""" 4. Hacer un programa que muestre al jugador una lista de habilidades por aprender, cada una con un precio en puntos.
    El jugador con una cantidad de puntos base podrá elegir qué habilidad aprender la cual deberá ser eliminada de la lista.
    Mostrar al final las habilidades que faltan por aprender."""

habilidades = ["Bola de fuego", "Curación mágica", "Robo"]
hab_aprendidas = []
costo = [5,4,2]
puntos = int(input("Cantidad de punto: "))
opcion = 0
bandera = True

while bandera == True:
    print("\tHABILIDADES")
    print(f"\nPuntos: {puntos}\n")
    for i in range(len(habilidades)):
        print(f"{i}. {habilidades[i]} - {costo[i]} puntos")
    print(f"{len(habilidades)}. Salir")
    
    opcion = int(input("Selección: "))

    if opcion == len(habilidades):
        bandera = False
        break
    
    if puntos >= costo[opcion]:
        hab_aprendidas.append(habilidades[opcion])
        puntos -= costo[opcion]
        del habilidades[opcion]
        del costo[opcion]
    else:
        print("Puntos insuficientes")

print("Habilidades aprendias")
for x in hab_aprendidas:
    print(x)
print("\nHabilidades por aprender: ")
for x in habilidades:
    print(x)


""" 5. Crear un menú que permita:
    a. Crear un personaje, preguntando nombre, tipo y atributos (ataque, velocidad, magia)
    b. Mortrar el personaje
    c. Eliminar el personaje.
    d. Salir. """


opcion = 0
guardado = False
personajes = []

while opcion!=4:
    print("MENÚ CREACIÓN PERSONAJES")
    print("(1) para crear un personajes")
    print("(2) para mostrar el personajes")
    print("(3) para eliminar un personajes")
    print("(4) para salir")
    opcion= int(input("Ingresa tu opción: "))

    if opcion==1:
        #Crear personaje
        guardado = True
        personaje = {}
        personaje["nombre"] = input("Nombre del personaje: ")
        personaje["tipo"] = input("Tipo de personaje: ")
        personaje["ataque"]  = float(input("Ataque del personaje: "))
        personaje["vel"] = float(input("Velocidad del personaje: "))
        personaje["magia"] = float(input("Poder mágico del personaje: "))
        personajes.append(personaje)
        print("Personaje creado")
        
    elif opcion==2:
        #Mostrar datos del personaje
        if guardado==True:
            for i in personajes:
                print(f"PERSONAJE {i}: ")
                print("Nombre: ", i["nombre"])
                print("Tipo: ", i["tipo"])
                print("Ataque: ", i["ataque"])
                print("Velocidad: ", i["vel"])
                print("Magia: ", i["magia"])
        else:
            print("No existe ningún personaje creado, cree uno primero")
    elif opcion==3:
        #Eliminar personaje
        if guardado==True:
            guardado=False
            for i in range(len(personajes)):
                del personajes[0]
            print("Personaje eliminado")
        else:
            print("No existe ningún personaje creado, cree uno primero")
    elif opcion==4:
        #Cerrar programa
        print("Saliendo")
        break
    else:
        print("Opción incorrecta, elija de nuevo")
