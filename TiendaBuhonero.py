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

class leon():
    def __init__(self, inventario, cantidad, dinero):
        self.inventario = inventario
        self.cantidad = cantidad
        self.dinero = dinero

    def vender(self, buhonero):
        bandera = False
        
        while bandera == False:
            posee = False
            n=1
            print("\n")
            print("----------- INVENTARIO -----------")
            print("\nDinero: ", self.dinero)
            for item in self.inventario:
                print(f"{n}.", end=" ")
                item.inv_leon(self.inventario, self.cantidad)
                n += 1
                print("\n")
            print(len(self.inventario)+1, "Volver")
            opcion = int(input("Vender: "))

            if opcion == len(self.inventario)+1:
                bandera = True
                break

            obj = self.inventario[opcion-1]
            indice = self.inventario.index(obj)

            self.dinero += obj.p_venta
            self.cantidad[indice] -= 1

            for i in buhonero.inv_tienda:
                if i == obj:
                    buhonero.cantidad[buhonero.inv_tienda.index(i)] +=1
                    posee == True
                    break

            if posee == False:
                buhonero.inv_tienda.append(obj)
                buhonero.cantidad.append(1)

            if self.cantidad[indice] == 0:
                del self.inventario[indice]
                del self.cantidad[indice]

class buhonero():
    def __init__(self, inv_tienda, cantidad):
       self.inv_tienda = inv_tienda
       self.cantidad = cantidad
    
    def vender(self, leon):
        bandera = False
        
        while bandera == False:
            posee = False
            n=1
            print("\n")
            print("----------- TIENDA -----------")
            print("\nDinero: ", leon.dinero)
            for item in self.inv_tienda:
                print(f"{n}.", end=" ")
                item.inv_buhonero(self.inv_tienda, self.cantidad)
                n+=1
                print("\n")
            print(len(self.inv_tienda)+1, "Volver")
            opcion = int(input("Comprar: "))

            if opcion == len(self.inv_tienda)+1:
                bandera = True
                break

            obj = self.inv_tienda[opcion-1]
            indice = self.inv_tienda.index(obj)

            if leon.dinero >= obj.p_compra:
                leon.dinero -=  obj.p_compra

                for i in leon.inventario:
                    if i == obj:
                        leon.cantidad[leon.inventario.index(i)] +=1
                        self.cantidad[indice] -=1
                        posee = True
                        break

                if posee == False:
                    leon.inventario.append(obj)
                    leon.cantidad.append(1)
                    self.cantidad[indice] -=1

                if self.cantidad[indice] == 0:
                    del self.inv_tienda[indice]
                    del self.cantidad[indice]

            else:
                print("Dinero insuficiente")

    def mejorar(self,leon):
        bandera = False
        while bandera == False:
            print("----------- MEJORAR -----------")
            print("\nDinero: ", leon.dinero)
            n=1
            for i in leon.inventario:
                if isinstance(i, arma) == True:
                    print(f"{n}.", end=" ")
                    i.inv_buhonero(leon.inventario, leon.cantidad)
                    print("\n")
                    n += 1
            print(n, "Volver")
            opcion = int(input("Selección: "))

            if opcion == n:
                bandera = True
                break

            num_arma = 0
            for i in leon.inventario:
                if isinstance(i,arma) == True:
                    num_arma += 1

                if isinstance(i, arma) == True and num_arma == opcion:
                    mejora = 0
                    while mejora != 5:
                        print("----------- MEJORAR -----------")
                        print("\nDinero: ", leon.dinero)
                        i.inv_mejora()
                        print("5. Volver")
                        mejora = int(input("Selección: "))
                        if mejora == 5:
                            break

                        if mejora == 1:
                            if i.daño < 6:
                                precio = 10000 - 8000*(1-i.daño/5)
                                if leon.dinero >= precio:
                                    leon.dinero -= precio
                                    i.daño +=1
                                else:
                                    print("Dinero insuficiente")
                            else:
                                print("Daño máximo alcanzado")
                        if mejora == 2:
                            if i.vel_recarga < 3:
                                precio = 10000 - 8000*(1-i.vel_recarga/2)
                                if leon.dinero >= precio:
                                    leon.dinero -= precio
                                    i.vel_recarga +=1
                                else:
                                    print("Dinero insuficiente")
                            else:
                                print("Velocidad de recarga máxima alcanzada")
                        if mejora == 3:
                            if i.cadencia < 3:
                                precio = 10000 - 8000*(1-i.cadencia/2)
                                if leon.dinero >= precio:
                                    leon.dinero -= precio
                                    i.cadencia +=1
                                else:
                                    print("Dinero insuficiente")
                            else:
                                print("Cadencia máxima alcanzada")
                        if mejora == 4:
                            if i.capacidad < 6:
                                precio = 10000 - 8000*(1-i.capacidad/5)
                                if leon.dinero >= precio:
                                    leon.dinero -= precio
                                    i.daño +=1
                                else:
                                    print("Dinero insuficiente")
                            else:
                                print("Capacidad máxima alcanzada")


def tienda_buhonero(buhonero, leon):
    seleccion = 0
    while seleccion != 4:
        print("\n---------------- TIENDA ----------------\n\n")
        print(" [ 1. Comprar ] [ 2. Vender ] [ 3. Mejorar ]")
        print("                [ 4. Salir ]\n\n")
        seleccion = int(input("Selección: "))

        if seleccion == 1:
            buhonero.vender(leon)
        elif seleccion == 2:
            leon.vender(buhonero)
        elif seleccion == 3:
            buhonero.mejorar(leon)
        else:
            print("\n???\n")

Granada =objeto("Granada", 1500)
Colgante = objeto("Colgante", 3000)
Magnum = arma("Magnum", 5000, 4,1,1,2)
Escopeta = arma("Escopeta", 3500, 4, 1, 1, 4)
Pistola = arma("Pistola", 4500, 4, 3, 1, 4)
Spray = objeto("Spray", 2000)

inventario = [Spray, Pistola, Magnum]
inv_tienda = [Granada,Colgante, Escopeta, Spray]
cant_tienda = [2,2,1,3]
cantidad = [2,1,1]
Leon = leon(inventario, cantidad, 20000)
Buhonero = buhonero(inv_tienda, cant_tienda)

#Pistola.inv_mejora()

# Buhonero.vender(Leon)
# Leon.vender(Buhonero)
# Buhonero.vender(Leon)
#Buhonero.mejorar(Leon)

tienda_buhonero(Buhonero, Leon)

# Spray.inv_buhonero(inventario,cantidad)
# Spray.inv_leon(inventario,cantidad)
