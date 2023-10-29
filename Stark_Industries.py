from data_stark import lista_personajes
from os import system
from funciones import*

while True:
    system("cls")
    respuesta = generar_menu_stark()

    match respuesta:
        
        case "a":
            print("\n---------NOMBRES DE SUPERHEROES---------\n")
            for superheroe in lista_personajes:
                nombre_heroe = superheroe["nombre"]

                print(f"{nombre_heroe:^40} ")
            print("\n")
          
        case "b":
            print("\n------NOMBRES-----------ALTURAS------\n")
            
            for superheroe in lista_personajes:
                nombre_heroe = superheroe["nombre"]
                altura_heroe = float(superheroe["altura"])

                print(f"{nombre_heroe:^20}   {altura_heroe:6.2f} cm")
            print("\n")

        case "c":
            print("\n------HEROE/S DE MAYOR ALTURA------")
            print("\n      NOMBRE     ALTURA\n")

            altura_maxima = separar_maximo(lista_personajes, "altura", float)

            for superheroe in lista_personajes:
                    altura_heroe = float(superheroe["altura"])
                    nombre_heroe = superheroe["nombre"]

                    if altura_heroe == altura_maxima:
                        print(f"    {nombre_heroe:^10}  {altura_heroe:6.2f} cm")
            print("\n")

        case "d":
            print("\n------HEROE/S DE MENOR ALTURA------")
            print("\n      NOMBRE        ALTURA\n")

            altura_minima = separar_minimo(lista_personajes, "altura", float)

            for superheroe in lista_personajes:
                    altura_heroe = float(superheroe["altura"])
                    nombre_heroe = superheroe["nombre"]
        

                    if altura_heroe == altura_minima:
                        print(f" {nombre_heroe:^10}  {altura_heroe:6.2f} cm")
            print("\n")

        case "e":
            print("\n----ALTURA PROMEDIO----")

            promedio = calcular_promedio(lista_personajes, "altura", float)

            print(f"{promedio:5.2f} cm")

            print("\n")

        case "f":
            peso_maximo = separar_maximo(lista_personajes, "peso")
            peso_minimo = separar_minimo(lista_personajes, "peso")

            print("\n----HEROE/S MAS PESADO----")
            for superheroe in lista_personajes:
                    peso_heroe = float(superheroe["peso"])
                    nombre_heroe = superheroe["nombre"]           
                    if peso_heroe == peso_maximo:
                        print(f" {nombre_heroe:10}  {peso_heroe:6.2f} kg")

            print("\n----HEROE/S MENOS PESADO----")
            for superheroe in lista_personajes:
                    peso_heroe = float(superheroe["peso"])
                    nombre_heroe = superheroe["nombre"]                           
                    if peso_heroe == peso_minimo:
                        print(f" {nombre_heroe:10}  {peso_heroe:6.2f} kg")

            print("\n")
        case "g":
            break

    system("pause")
    
   
    


    