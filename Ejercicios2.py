#Ejercicios de estructuras condicionales y cíclicas

""" 1. Para comprar una poción roja, Link necesita 30 rupias. Hacer un programa que permita ingresar un número
    de rupias y mostrar su puede comprar o no la poción, en caso de que no, decir cuantas rupias le faltan."""

rupias = int(input("Ingrese el número de rupias: "))
faltante = 0

if rupias<30:
    faltante = 30- rupias
    print("Faltan",faltante,"rupias para comprar la poción")
    print(f"No puedes comprar la poción, te faltan {30-rupias} rupias")  #Otra forma de escribirlo
else:
    print("Puede comprar la poción")


""" 2. Hacer un programa que permita ingresar el nombre de un estudiante y 3 notas con valor de 0 a 5.
    Calcular el promedio y si es mayor o igual a 3 mostrar por pantalla "Aprobado", de lo contrario "Reprobado"."""

nombre = input("Ingrese el nombre: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1+nota2+nota3)/3

if promedio<3:
    print("Reprobado con",round(promedio,2))  #round para limitar el número de decimales del resultado
else:
    print("Aprobado con",round(promedio,2))

""" 3. Realizar un problema que permita ingresar una contraseña de por lo menos 7 caracteres. Luego preguntarla
    y verificar si es correcta o no, en caso de no serlo, seguir preguntando hasta que se ingrese la correcta."""

password= input("Cree una contraseña de almenos 7 caracteres: ")
contador = 0
caracteres = False

while caracteres==False:
    for x in password:
        contador +=1
    if contador>=7:
        print("Cantidad caracteres válida")
        caracteres = True
    else:
        print("La contraseña debe tener al menos 7 caracteres")
        password = input("Cree una contraseña de almenos 7 caracteres: ")
        caracteres = False

verificar = input("Ingrese la contraseña: ")

while password!=verificar:
    print("Contraseña incorrecta")
    verificar = input("Ingrese la contraseña: ")

print("Contraseña correcta")

""" 4. Mostrar por pantalla los primeros n términos de la serie Fibonacci que comienza en 0 y 1 y genera los
    siguientes términos con la suma de los dos anteriores, en donde n es un número ingresado por el usuario."""

n = int(input("Ingrese un número: "))
n1 = 0
n2 = 1
for x in range(n):
    n3 = n1+n2
    print(n3)
    n1=n2
    n2=n3

""" 5. Crear un menú que permita:
    a. Crear un personaje, preguntando nombre, tipo y atributos (ataque, velocidad, magia)
    b. Mortrar el personaje
    c. Eliminar el personaje.
    d. Salir. """

opcion = 0
guardado = False

while opcion!=4:
    print("MENÚ CREACIÓN PERSONAJES")
    print("(1) para crear un personaje")
    print("(2) para mostrar el personaje")
    print("(3) para eliminar un personaje")
    print("(4) para salir")
    opcion= int(input("Ingresa tu opción: "))
    if opcion==1:
        #Crear personaje
        nombre = input("Nombre del personaje: ")
        tipo = input("Tipo de personaje: ")
        ataque  = float(input("Ataque del personaje: "))
        vel = float(input("Velocidad del personaje: "))
        magia = float(input("Poder mágico del personaje: "))
        print("Personaje creado")
        guardado = True
    elif opcion==2:
        #Mostrar datos del personaje
        if guardado==True:
            print(nombre)
            print(tipo)
            print(ataque)
            print(vel)
            print(magia)
        else:
            print("No existe ningún personaje creado, cree uno primero")
    elif opcion==3:
        #Eliminar personaje
        if guardado==True:
            nombre=""
            tipo=""
            ataque=""
            vel=""
            magia=""
            guardado=False
            print("Personaje eliminado")
        else:
            print("No existe ningún personaje creado, cree uno primero")
    elif opcion==4:
        #Cerrar programa
        print("Saliendo")
        break
    else:
        print("Opción incorrecta, elija de nuevo")

