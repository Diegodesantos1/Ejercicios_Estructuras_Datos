
def eleccion_ejercicio():
    variable = int(input("\nSeleccione que ejercicio desea ejecutar: (1-3)\n"))
    if variable == 1:
        from Clases import ejercicio1
    if variable == 2:
        from Clases import ejercicio2
    if variable == 3:
        from Clases import ejercicio3
    else:
        eleccion_ejercicio()
eleccion_ejercicio()