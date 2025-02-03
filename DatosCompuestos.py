listaUno = [4,75,31,"Nombre",True] #Python permite asignar diferentes tipos de datos
print(listaUno[0])

listaUno[0]=False #Modificar datos
print(listaUno[0])

for i in listaUno: #Muestra todos los datos de la lista
    print(i)

#_____________________________________________________________________________________
tuplaUno = (54,23,"Hola",False)
print(tuplaUno[1])

lista1 = [45, "Hola", False, "Mañana"]
lista2 = [454, 65, 12, 3, 0, 1245]
#lista2.sort()
#lista2.reverse()
#del lista2[2]
#numpos3 = lista2.pop(3)
#print(lista2.index(12))  #si hay datos repetidos, solo me muestra el primero
#print(lista2.count(12))
#lista2.append("hola")
#lista2.insert(2,False)
#lista1.extend(lista2)
print(len(lista2))

print(lista2)

#______________________________________________________________________________________
diccionario1 = {"071":"Jesus","045":"Carlos","953":"Sofía", 23:48, 1:True}
print(diccionario1[1])   #Se llama la llave

diccionario1["045"] = 12
print(diccionario1)

print(diccionario1.values())  #Imprime solo los valores
print(diccionario1.keys())  #Imprime solo las llaves
print(diccionario1.items())  #Imprime los items

listaArmas = [""]*3

for i in range(len(listaArmas)):
    listaArmas[i] = input("Ingresa nombre del arma: ")

print("\tARMAS INGRESADAS")

print(listaArmas)