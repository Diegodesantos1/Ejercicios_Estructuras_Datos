import os
import time
class Entrada:
    def entrada_estandar():
        mensaje=str(input("Qué mensaje quieres escribir\n"))
        print("Se va a generar el fichero de texto en unos instantes...")
        fichero = open("Ejercicio2.txt", "a")
        fichero.write(mensaje)
        fichero.close()
        time.sleep (10) #se borra tras 10 segundos
        os.remove("Ejercicio2.txt")
Entrada.entrada_estandar()