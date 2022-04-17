class Productos:
    def __init__ (self, alimentario, entretenimiento, servicio, precio_inicial):
        self.alimentario = alimentario
        self.entretenimiento = entretenimiento
        self.servicio = servicio
        self.precio_inicial = precio_inicial
    def alimentario(self):
        return self.alimentario
    def entretenimiento(self):
        return self.entretenimiento
    def servicio(self):
        return self.servicio
    def precio_inicial(self):
        return self.precio_inicial
    def iva ():
        precio_inicial = 100
        eleccion = int(input(("\n\n Bienvenido a su tienda online, que desea comprar con sus 100€: \n 1: Alimentos \n 2: Servicio \n 3: Entretenimiento \n 4: Terminar el programa\n")))
        if eleccion == 1:
            precio_final = round(precio_inicial * 1.04)
            print(f"La compra de ha realizado correctamente, le ha costado {precio_final}€")
            Productos.iva ()
        if eleccion == 2:
            precio_final = round(precio_inicial * 1.21)
            print(f"La compra de ha realizado correctamente, le ha costado {precio_final}€")
            Productos.iva ()
        if eleccion == 3:
            precio_final =round( precio_inicial * 1.1)
            print(f"La compra de ha realizado correctamente, le ha costado {precio_final}€")
            Productos.iva ()
        else:
            print("Opción no válida")
            exit()
Productos.iva()


