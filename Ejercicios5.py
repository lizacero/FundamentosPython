#Ejercicios de POO
from math import pi

""" 1. Hacer una clase auto con los atributos: color, placa, marca y precio. Además del método: 
    mostrar_atributos() y calcular_impuesto() que será del 1% del precio."""

# class auto():
#     def __init__(self, color, placa, marca, precio):
#         self.color = color
#         self.placa = placa
#         self.marca = marca
#         self.precio = precio

#     def mostrar_atributos(self):
#         print("Auto")
#         print("Color: ", self.color)
#         print("Placa: ", self.placa)
#         print("Marca: ", self.marca)
#         print("Precio: ", self.precio)

#     def calcular_impuesto(self):
#         print("Impuesto: ", self.precio*0.01)

# Chevrolet = auto("Rojo", "123QWE", "Crevrolet", 100)

# Chevrolet.mostrar_atributos()
# Chevrolet.calcular_impuesto()

""" 2. Implementar la siguiente clase:
    Estudiante: - Nombre
                - Código
                - Asignatura
                - Nota1
                - Nota2
                - Nota3
                - Nota4
        - Mostrar_datos()
        - Calificación() """

# class estudiante():
#     def __init__(self, nombre, codigo, asignatura, nota1, nota2, nota3, nota4):
#         self.nombre = nombre
#         self.codigo = codigo
#         self.asignatura = asignatura
#         self.nota1 = nota1
#         self.nota2 = nota2
#         self.nota3 = nota3
#         self.nota4 = nota4

#     def mostrar_datos(self):
#         print("Estudiante: ",self.nombre)
#         print("Código: ",self.codigo)
#         print("Asignatura: ",self.asignatura)
#         print("Nota 1: ",self.nota1)
#         print("Nota 2: ",self.nota2)
#         print("Nota 3: ",self.nota3)
#         print("Nota 4: ",self.nota4)

#     def calificacion(self):
#         promedio = (self.nota1+self.nota2+self.nota3+self.nota4)/4
#         if promedio >= 3:
#             print("Estudiante aprobado con ", promedio)
#         else:
#             print("Estudiante reprobado con ", promedio)

# Estudiante1 = estudiante("Lola", 1223, "Matemáticas", 3,5,2,4)

# Estudiante1.mostrar_datos()
# Estudiante1.calificacion()

""" 3. Hacer un programa que permita clasificar los ítems de una tienda, se deberá recibir un
    inventario con un número de ítems y dividirlos en 3 grupos: Comida, herramientas y aseo. """

# class producto():
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio

#     def datos(self):
#         print(f"{self.nombre}: {self.precio}")

# class comida(producto):
#     def __init__(self, nombre, precio, caducidad):
#         super().__init__(nombre, precio)
#         self.caducidad = caducidad

#     def datos(self):
#         print(f"{self.nombre}: {self.precio}")
#         print(f"Caducidad: {self.caducidad}")

# class herramientas(producto):
#     def __init__(self, nombre, precio, material):
#         super().__init__(nombre, precio)
#         self.material = material

#     def datos(self):
#         print(f"{self.nombre}: {self.precio}")
#         print(f"Material: {self.material}")
        
# class aseo(producto):
#     def __init__(self, nombre, precio, uso):
#         super().__init__(nombre, precio)
#         self.uso = uso

#     def datos(self):
#         print(f"{self.nombre}: {self.precio}")
#         print(f"Uso: {self.uso}")

# class tienda():
#     def __init__(self, inventario):
#         self.inventario = inventario

#     def comida(self):
#         print("---COMIDA---")
#         for item in self.inventario:
#             if isinstance(item,comida) == True:
#                 item.datos()
#                 print("\n")

#     def herramientas(self):
#         print("---HERRAMIENTAS---")
#         for item in self.inventario:
#             if isinstance(item,herramientas) == True:
#                 item.datos()
#                 print("\n")

#     def aseo(self):
#         print("---ASEO---")
#         for item in self.inventario:
#             if isinstance(item,aseo) == True:
#                 item.datos()
#                 print("\n")
        
# manzana = comida("Manzana", 3000, "22/03/24")
# pera = comida("Pera", 4000, "25/03/24")
# chocolate = comida("Chocolate", 2500,"12/07/24")
# martillo = herramientas("Martillo", 45000, "Metal")
# destornillador = herramientas("Destornillador", 37000, "Metal y plástico")
# detergente = aseo("Detergente", 7000, "1 tapa de detergente por cada 5 litros de agua")

# inventario = [manzana, destornillador, detergente, chocolate, martillo, pera]

# Tiendita = tienda(inventario)

# Tiendita.comida()
# Tiendita.herramientas()
# Tiendita.aseo()


""" 4. Crear la clase Figuras geométricas con los métodos calc_área() y calc_perímetro(). De esta
    clase, heredar las clases triángulo rectángulo, rectángulo y círculo, y sobrescribir los métodos
    calc_área() y calc_perímetro() en cada caso"""

# class figuras():
#     def __init__(self,figura):
#         self.figura = figura

#     def calc_area(self):
#         pass

#     def calc_per(self):
#         pass

# class rectangulo(figuras):
#     def __init__(self, figura, lado1, lado2):
#         super().__init__(figura)
#         self.lado1 = lado1
#         self.lado2 = lado2

#     def calc_area(self):
#         return self.lado1*self.lado2

#     def calc_per(self):
#         return 2*self.lado1 + 2*self.lado2

#     def datos(self):
#         print(self.figura)
#         print(f"Lado 1 : {self.lado1}  Lado 2 : {self.lado2}")
#         print("Área: ", self.calc_area())
#         print("Perímetro: ", self.calc_per())

# class trian_rect(figuras):
#     def __init__(self, figura, base, altura):
#         super().__init__(figura)
#         self.base = base
#         self.altura = altura

#     def calc_area(self):
#         return (self.base*self.altura)/2

#     def calc_per(self):
#         hip = (self.base**2 + self.altura**2)**(1/2)
#         return self.base + self.altura + hip 

#     def datos(self):
#         print(self.figura)
#         print(f"Base : {self.base}  Altura : {self.altura}")
#         print("Área: ", self.calc_area())
#         print("Perímetro: ", self.calc_per())

# class circulo(figuras):
#     def __init__(self, figura, radio):
#         super().__init__(figura)
#         self.radio = radio

#     def calc_area(self):
#         return pi*self.radio**2

#     def calc_per(self):
#         return 2*pi*self.radio

#     def datos(self):
#         print(self.figura)
#         print(f"Radio : {self.radio} ")
#         print("Área: ", self.calc_area())
#         print("Perímetro: ", self.calc_per())



# rect = rectangulo("Rectángulo", 3,2)
# rect.datos()
# tri = trian_rect("Triángulo", 3,4)
# tri.datos()
# circ = circulo("Círculo", 2)
# circ.datos()

""" 5. Implementar las siguientes clases:
    Libro:  - Título
            - Autor
            - ISBN
            - Estado (prestado o disponible)
        - Datos()
    Biblioteca: - Libros
        - BuscarLibro()
        - Prestados()
    Persona:- Nombre
            - Código
            - Libros prestados
        - Prestar()
        - Devolver()"""

class libro():
    def __init__(self, titulo, autor, isbn, estado):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = estado

    def datos(self):
        print("Título: ", self.titulo)
        print("Autor: ", self.autor)
        print("ISBN: ", self.isbn)
        if self.estado == True:
            print("Estado: Disponible")
        else:
            print("Estado: Prestado")    

class biblioteca():
    def __init__(self, libros):
        self.libros = libros

    def buscarLibro(self,nombre):
        for libro in self.libros:
            if nombre.upper() == libro.titulo.upper():
                print("LIBRO ENCONTRADO!")
                libro.datos()

    def prestados(self):
        print("LIBROS PRESTADOS")
        for libro in self.libros:
            if libro.estado == False:
                libro.datos()
                print("\n")

class persona():
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.libros_pres = []

    def prestar(self,biblioteca):
        print("\nLIBROS DISPONIBLES PARA PRÉSTAMO")
        for libro in biblioteca.libros:
            if libro.estado == True:
                libro.datos()
                print("\n")

        seleccion = input("Nombre del libro: ")
        for libro in biblioteca.libros:
            if seleccion.upper() == libro.titulo.upper():
                self.libros_pres.append(libro)
                libro.estado = False
                print("\nLibro prestado correctamente")
                break

    def devolver(self):
        print("PRESTADOS: ")
        for libro in self.libros_pres:
            libro.datos()
            print("\n")

        seleccion= input("Nombre del libro a devolver: ")
        for libro in self.libros_pres:
            if seleccion.upper() == libro.titulo.upper():
                libro.estado = True
                del self.libros_pres[self.libros_pres.index(libro)]
            break

misery = libro("Misery","Stephen King", "9993409023", True)
cien_años = libro("Cien años de soledad", "Gabriel García Marquez", "9273823293", True)
la_fundacion = libro("La fundación", "Isaac Asimov","99731263834",True)
libros = [misery,cien_años,la_fundacion]

jorge = persona("Jorge","123534")

biblio = biblioteca(libros)

#biblio.buscarLibro("misEry")

jorge.prestar(biblio)
jorge.prestar(biblio)
biblio.prestados()
jorge.devolver()
biblio.prestados()