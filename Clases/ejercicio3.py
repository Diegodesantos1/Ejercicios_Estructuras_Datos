class Productos:
    def __init__ (self, alimentario, entretenimiento, servicio, precio_inicial):
        self.alimentario = alimentario
        self.entretenimiento = entretenimiento
        self.servicio = servicio
        self.precio_inicial = precio_inicial
    def iva ():
        precio_inicial = 100
        eleccion = int(input(("Bienvenido a su tienda online, que desea comprar con sus 100€: \n 1: Alimentos \n 2: Servicio \n 3: Entretenimiento\n\n")))
        if eleccion == 1:
            precio_final = precio_inicial * 1.04
            print(f"La compra de ha realizado correctamente, le ha costado {precio_final}€")
            exit()
        if eleccion == 2:
            precio_final = precio_inicial * 1.21
            print(f"La compra de ha realizado correctamente, le ha costado {precio_final}€")
            exit()
        if eleccion == 3:
            precio_final = precio_inicial * 1.1
            print(f"La compra de ha realizado correctamente, le ha costado {precio_final}e")
            exit()
        else:
            print("Opción no válida")
            exit()
Productos.iva()


