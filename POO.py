class Celular():

    def __init__(self, marca, camara, memoria):
        self.marca = marca
        self.camara = camara
        self.memoria = memoria

    def mostrarCaracterísitcas(self):
        print("Marca: " + self.marca)
        print("Camara " + str(self.camara))
        print("Memoria: " + str(self.memoria))
    
    def encender(self):
        print("Celular encendido")

    def llamar(self):
        print("Haciendo llamada")
    
    def foto(self):
        print("Tomando foto")

    def apagar(self):
        print("Celular apagado")

Samsung = Celular("Samsung", 124, 2)
Iphone = Celular("Iphone", 150, 1)
Xiaomi = Celular("Samsung", 200, 3)

Xiaomi.marca = "Xiaomi"

Samsung.mostrarCaracterísitcas()
Iphone.mostrarCaracterísitcas()
Xiaomi.mostrarCaracterísitcas()

class Pajaro():
    
    def __init__(self, color, zona):
        self.color = color
        self.zona = zona

    def set_Color(self,color):
        self.color = color

    def get_Color(self):
        return self.color

    def tipo(self):
        print("General")
    

class Rapaz(Pajaro):
    def __init__(self, color, zona, presa):
        super().__init__(color, zona)
        self.presa = presa

    def Cazar(self):
        print(self.presa +  "Cazados")

    def tipo(self):
        print("Rapaz")

Aguila = Rapaz("Cafe", "Montañas", "Ratones")
Ave = Pajaro("Roja", "Bosque")
Aguila.Cazar()
print(Aguila.get_Color())

def tipoPajaro(pajaro):
    pajaro.tipo()

tipoPajaro(Aguila)
tipoPajaro(Ave)