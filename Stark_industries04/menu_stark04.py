#Escobar Tobias Fabricio 
#1-J

#Ejercicio Integrador Data Stark #04 

from os import system
system("cls")

from funciones_stark04 import *

def stark_marvel_app(lista:list):
    datos_normalizados = False
    seguir = True 
    while seguir:
        respuesta = stark_menu_principal(lista)
        if respuesta <1 or respuesta >6:
            print("ERROR. Elija una opcion de 1 a 7.")
        else:
            if not datos_normalizados and respuesta != 3:
                print("ERROR. Primero se deben normalizar los datos con el punto 3.")
            else:
                match respuesta:
                    case 1:
                        print(stark_imprimir_nombres_con_iniciales(lista_personajes))
                    case 2:
                        print(stark_generar_codigos_heroes(lista_personajes))
                    case 3:
                        stark_normalizar_datos(lista_personajes)
                        datos_normalizados = True
                    case 4:
                        stark_imprimir_indice_nombre(lista_personajes)
                    case 5:
                        stark_navegar_fichas(lista_personajes)
                    case 6:
                        seguir = False

stark_marvel_app(menu)