def funcionSaludar(nombre):
    print(f"Hola {nombre}")
    print("¿Cómo estás?")

funcionSaludar("Roberto")

def calcularSuma(a, b, c, d="Saludo", e="GoodBye"):
    print(a+b*c)
    print(d, e)

calcularSuma(4,90,6,e="Hi")

def multiplicarNums(*args, **kwargs):
    for i in args:
        print(i)
    for n in kwargs:
        print(kwargs[n])

multiplicarNums(2, 2, 3, d="Hola", b="False")

def Promedio(nota1, nota2, nota3):
    return(nota1+nota2+nota3)/3

promedio = Promedio(4, 3, 5)
print(promedio)