from funciones_stark05 import *

def stark_marvel_app(lista:list,lista_pj):
    """
    Brief:
    Crea un menu de stark el cual dependendiendo la opcion que ingreso el usuario,llama a la funcion que corresponda.

    Parametro/s:
    Recibe la lista de la cual va a imprimir sus opciones

    Return:
    Nada
    """
    datos_normalizados = False
    seguir = True 
    while seguir:
        respuesta = stark_menu_principal(lista)
        if respuesta <1 or respuesta >7:
            print("ERROR. Elija una opcion de 1 a 7.")
        else:
            if not datos_normalizados and respuesta != 1:
                print("ERROR. Primero se deben normalizar los datos con el punto 3.")
            else:
                match respuesta:
                    case 1:
                        normalizar_datos(lista_pj)
                        datos_normalizados = True
                    case 2:
                        lista_csv = generar_csv("heroes.csv",lista_pj)
                        
                    case 3:
                        lista_csv = listar_heroes_por_altura_csv("heroes.csv")
                        print(lista_csv)

                    case 4:
                        lista_json = generar_json("heroes.json",lista_pj,"heroes")
                        print(lista_json)
            
                    case 5:
                        lista_json = (listar_heroes_por_peso_json("heroes.json"))
                        print(lista_json)
                        
                    case 6:
                        orden = input("Ingrese un orden: ASC para ordenar de forma ascendente, DESC para  ordenar de forma descendente: ")
                        while orden != "DESC" and orden != "ASC":
                            orden = input("Ingrese un orden: ASC para ordenar de forma ascendente, DESC para  ordenar de forma descendente: ")
                        orden_lower = orden.lower()
                        ordenar_lista_fuerza(lista_pj,orden_lower)
                    case 7:
                        seguir = False


stark_marvel_app(menu,lista_personajes)