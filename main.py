from Clases.ejercicio1 import visitante
def eleccion_ejercicio():
    variable = int(input("\nSeleccione que ejercicio desea ejecutar: (1-3)\n"))
    if variable == 1:
        visitante(str(input("Si desea ejecutar: \n\n A: Ejemplo del enunciado 1 \n\n B: Bucle de la clase MientrasQue\n\n")))
    if variable == 2:
        from Clases import ejercicio2
    if variable == 3:
        from Clases import ejercicio3
    else:
        eleccion_ejercicio()
eleccion_ejercicio()