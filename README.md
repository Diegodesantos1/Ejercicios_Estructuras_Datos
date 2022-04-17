<h1 align="center">Estructuras de datos</h1>

---
En este [repositorio](https://github.com/Diegodesantos1/Ejercicios_Estructuras_Datos) queda resuelto el ejercicio de estructuras de datos para POO. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual otras fuentes.
***
## Ejercicio 1

En este ejercicio he completado las clases que estaban creadas y he creado la función visitante la cual recorre el programa.

El código empleado para resolverlo es el siguiente: 

```python
class Bloque:
    # Un bloque es un conjunto de instrucciones ejecutadas
    # unas detrás de otras.
    def __init__(self):
        # Por defecto, un bloque no contiene ninguna instrucción.
        self.instrucciones = []
    def agregarInstruction(self, instruccion):
        self.instrucciones.append(instruccion)

class Si:
    # Representa una instrucción 'if'. 'condicion' es una cadena
    # de caracteres que contiene la evaluación de la condición,
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas
    # si no se verifica.
    def __init__(self, condicion, entonces, si_no):
        self.condicion = condicion
        self.entonces = entonces
        self.si_no = si_no
    def ejecutar(self):
        entonces = self.entonces
        si_no = self.si_no
        if self.condicion == True:
            Mostrar(entonces).mostrar()
        else:
            Mostrar(si_no).mostrar()


class MientrasQue:
    # Representa una instrucción 'while'.
    # 'condicion' es una cadena que contiene el valor evaluado
    # para decidir si el bucle continúa o no,
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle.
    def __init__(self, condicion, bloque):
        self.condicion = condicion
        self.bloque = bloque
    def bucle(self):
        variable1 = 1
        while variable1 <= self.condicion:
            Mostrar(self.bloque).mostrar()
            variable1 += 1

class Mostrar:
    # Una instrucción para mostrar un mensaje
    # en salida estándar.
    def __init__(self, mensaje):
        self.mensaje = mensaje
    def mostrar(self):
        print(self.mensaje)

def visitante(eleccion_visitante):
    if eleccion_visitante =="A":
        ok = "OK"
        ko = "KO"
        alternativa = Si(2+2 == 4, ok, ko)
        alternativa.ejecutar()
    elif eleccion_visitante == "B":
        alternativa = MientrasQue(int(input("Introduzca cuántas veces quiere ejecutar el bucle:\n")), input(
            "Introduzca el texto que desee:\n"))
        alternativa.bucle()
    else:
        print("No válido.")
        visitante(int(input("Si desea ejecutar: \n\n 1: Ejemplo del enunciado 1 \n\n 2: Bucle de la clase MientrasQue\n\n")))
```
## Ejercicio 2

En este ejercicio he aplicado MVC para generar un archivo de texto que devuelva una cadena de texto introducida en mayúsculas.

El código empleado para resolverlo es el siguiente:

```python
import os
import time
class Entrada:
    def __init__ (self, mensaje):
        self.mensaje = mensaje
    def mensaje(self):
        return self.mensaje
    def entrada_estandar():
        mensaje=str(input("Qué mensaje quieres escribir\n"))
        mensajefinal= mensaje.upper()
        print("Se va a generar el fichero de texto en unos instantes...")
        fichero = open("Ejercicio2.txt", "a")
        fichero.write(mensajefinal)
        fichero.close()
        time.sleep (10) #se borra tras 10 segundos
        os.remove("Ejercicio2.txt")
Entrada.entrada_estandar()
```
## Ejercicio 3

En este ejercicio había que implementar la tasa de IVA correspondiente en función del producto.

El código empleado para resolverlo es el siguiente:

```python
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
```
