def generar_menu_stark():
    print("--------------------------STARK INDUSTRIES--------------------------")
    opcion = (input("\na). Mostrar listado de nombres de superheroes\
                     \nb). Mostrar listado de nombres y alturas de superheroes\
                     \nc). Mostrar nombre y altura de superheroe/s mas altos\
                     \nd). Mostrar nombre y altura de superheroe/s mas bajos\
                     \ne). Mostrar altura promedio de los superheroes\
                     \nf). Mostrar nombre y peso de superheroes mas y menos pesados\
                     \ng). Salir\n\nElija una opcion: "))
    
    opcion = opcion.lower()
    return opcion
    

def separar_maximo (lista:list, clave:str, tipo_de_dato = float):
    maximo = 0
    bandera_primero = True
    for i in lista:
        maximo_lista = tipo_de_dato(i[clave])
        if maximo_lista > maximo or bandera_primero == True:
            maximo = maximo_lista
            bandera_primero = False
    
    return maximo

def separar_minimo (lista:list, clave:str, tipo_de_dato = float):
    minimo = 0
    bandera_primero = True
    for i in lista:
        minimo_lista = tipo_de_dato(i[clave])
        if minimo_lista < minimo or bandera_primero == True:
            minimo = minimo_lista
            bandera_primero = False
    
    return minimo

def calcular_promedio (lista:list, clave:str, tipo_de_dato = float):
    acumulador = 0

    for i in lista:
        valor = tipo_de_dato(i[clave])

        acumulador += valor

    return acumulador/len(lista)

