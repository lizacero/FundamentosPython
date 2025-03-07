# Proyecto final
# Desarrollo de la lógica detrás de la tienda del buhonero de RE4

class objeto():
    def __init__(self,  nombre, p_compra):
        self.nombre = nombre
        self.p_compra = p_compra
        self.p_venta = p_compra*0.75

    def inv_buhonero(self, inventario, cantidad):
        indice = inventario.index(self)
        print(f"{self.nombre} x {cantidad[indice]} ({self.p_compra} $)")

    def inv_leon(self, inventario, cantidad):
        indice = inventario.index(self)
        print(f"{self.nombre} x {cantidad[indice]} ({self.p_venta} $)")

class arma(objeto):
    def __init__(self, nombre, p_compra, daño, vel_recarga, cadencia, capacidad):
        super().__init__(nombre, p_compra)
        self.daño = daño
        self.vel_recarga = vel_recarga
        self.cadencia = cadencia
        self.capacidad = capacidad

    # | niveles del arma - faltan niveles por comprar

    def inv_buhonero(self, inventario, cantidad):
        print(self.nombre, self.p_compra)

        print("  Daño      Vel. recarga  Cadencia  Capacidad")
        print("  "+"|"*self.daño + "-"*(6-self.daño), end="    ")
        print("|"*self.vel_recarga + "-"*(3-self.vel_recarga), end="           ")
        print("|"*self.cadencia + "-"*(3-self.cadencia), end="       ")
        print("|"*self.capacidad + "-"*(6-self.capacidad))

    
    # precio = 10000 - 8000(1-daño/5)
    def inv_mejora(self):
        print("Mejorar", self.nombre)

        print("1. Daño          " + "|"*self.daño + "-"*(6-self.daño), end="    ")
        print(10000 - 8000*(1 - self.daño/5), "$")
        print("2. Vel. Recarga  " + "|"*self.vel_recarga + "-"*(3-self.vel_recarga), end=" "*7)
        print(10000 - 8000*(1 - self.vel_recarga/2), "$")
        print("3. Cadencia      " + "|"*self.cadencia + "-"*(3-self.cadencia), end=" "*7)
        print(10000 - 8000*(1 - self.cadencia/2), "$")
        print("4. Capacidad     " + "|"*self.capacidad + "-"*(6-self.capacidad), end="    ")
        print(10000 - 8000*(1 - self.capacidad/5), "$")

Pistola = arma("Pistola", 4500, 4, 3, 1, 4)
Spray = objeto("Spray", 2000)

inventario = [Spray, Pistola]
cantidad = [2,1]

Pistola.inv_mejora()

# Spray.inv_buhonero(inventario,cantidad)
# Spray.inv_leon(inventario,cantidad)
