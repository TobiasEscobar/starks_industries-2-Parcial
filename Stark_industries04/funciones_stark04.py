# Desafío #04:
# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
# escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
# un string, etc y que contendrá) y que es lo que retorna la función!

import re
from data_stark import *

# 1.1.
def extraer_iniciales(nombre_heroe:str)->str:
    """
    Brief: Extrae las iniciales en mayúsculas de un nombre de héroe.

    Param: 
    - nombre_heroe (str): El nombre del héroe del cual se extraerán las iniciales.

    Returns:
    str: Las iniciales en mayúsculas de cada palabra en el nombre del héroe, separadas por puntos.
    Si el nombre está vacío o no contiene letras, devuelve "N/A".
    """
    if nombre_heroe == "":
        return print("N/A")
    else:
        nombre = re.findall(r'[A-Z]+', nombre_heroe)
        iniciales = ".".join(nombre) + "."
        return iniciales

# 1.2. 
def obtener_dato_formato(dato:str)->str:
    """
    Brief: Formatea el dato en minúsculas y reemplaza espacios y guiones por guiones bajos.

    Param:
    dato (str): El dato a formatear.

    Returns:
    str: El dato formateado en minúsculas con espacios y guiones reemplazados por guiones bajos.
    Si el dato no es una cadena de texto, devuelve False.
    """
    if type(dato) == str:
        dato = dato.lower()  
        dato = re.sub(r'[\s-]', '_', dato)
        return dato
    else:
        return False

# 1.3.
def stark_imprimir_nombre_con_iniciales(nombre_heroe:str)->str:
    """
    Brief: Imprime el nombre del héroe con sus iniciales en un formato específico.

    Param:
    nombre_heroe (dict): Un diccionario que contiene al menos la clave 'nombre' con el nombre del héroe.

    Returns:
    bool: Devuelve True si el nombre del héroe se imprime correctamente en un formato especial.
    Si el tipo de dato de nombre_heroe no es un diccionario o no contiene la clave 'nombre', devuelve False.
    """
    if type(nombre_heroe) != dict or "nombre" not in nombre_heroe:
        return False
    else:
        nombre = nombre_heroe['nombre']
        formato = obtener_dato_formato(nombre)
        iniciales = extraer_iniciales(nombre)
        nombre_con_iniciales = f"* {formato} ({iniciales})"
        print(nombre_con_iniciales)
        return True

# 1.4.
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    """
    Brief: Imprime los nombres de héroes con sus iniciales en un formato específico.

    Param:
    lista_heroes (list): Una lista que contiene diccionarios con los nombres de los héroes.

    Returns:
    bool: Devuelve True si los nombres de los héroes se imprimen correctamente en un formato especial.
    Si lista_heroes no es una lista o está vacía, devuelve False.
    """
    if type(lista_heroes) != list or len(lista_heroes) == 0:
        return False
    else:
        for heroe in lista_heroes:
            stark_imprimir_nombre_con_iniciales(heroe)
        return True

#2.1.
def generar_codigo_heroe(heroe, id):
    """
    Brief: Genera un código de identificación basado en el género y un ID.

    Param:
    heroe (dict): Un diccionario que contiene la clave 'genero' con el género del héroe.
    id (int): El ID para combinar con el género y generar el código.

    Returns:
    str: Devuelve un código de identificación que combina el género del héroe con el ID proporcionado.
    Si el héroe no tiene un género válido ('M', 'F', 'NB') o falta la clave 'genero', devuelve "N/A".
    """
    if "genero" not in heroe or heroe["genero"] not in ["M", "F", "NB"]:
        return "N/A"

    if heroe["genero"] == "M":
        inicial = "1"
    elif heroe["genero"] == "F":
        inicial = "2"
    else:
        inicial = "0"

    genero = heroe["genero"]

    ceros_restantes = str(id).zfill(10 - len(f"{inicial}-{genero}")) 
    codigo = f"{genero}-{inicial}{ceros_restantes}"

    return codigo 

# 2.2. 
def stark_generar_codigos_heroes(lista_heroes):
    """
    Brief: Genera un mensaje con códigos para los héroes en una lista.

    Param:
    lista_heroes (list): Una lista que contiene diccionarios con información de los héroes.

    Returns:
    str or bool: Devuelve un mensaje con los códigos asignados a los héroes.
    Si la lista de héroes está vacía o no todos los elementos son diccionarios, devuelve False.
    """
    if not lista_heroes or not all(isinstance(heroe, dict) for heroe in lista_heroes):
        return False

    mensaje = ""
    cantidad_codigos = 0
    for index, personaje in enumerate(lista_heroes, start=1):
        codigo = generar_codigo_heroe(personaje, index)
        if codigo != 'N/A':
            nombre_abreviado = ''.join(word[0].upper() for word in personaje['nombre'].split())
            mensaje += f"* {personaje['nombre']} ({nombre_abreviado}.) | {codigo}\n"
            cantidad_codigos += 1

    mensaje += f"Se asignaron {cantidad_codigos:02d} códigos\n"
    return mensaje

def sacar_espacios(numero:str):
    """
    Brief: Elimina espacios en blanco al inicio y final de una cadena.

    Param:
    numero (str): La cadena de texto de la cual se desean eliminar los espacios.

    Returns:
    str: Devuelve la cadena sin espacios en blanco al inicio o final.
    """
    numero_sin_espacios = numero.strip()
    return numero_sin_espacios

# 3.1. 
def sanitizar_entero(numero_str:str):
    """
    Brief: Convierte una cadena en un número entero después de sanearla.

    Param:
    numero_str (str): La cadena que se desea convertir en un número entero.

    Returns:
    int: Devuelve el número entero obtenido después de sanear la cadena.
    Si la cadena no representa un número o es negativa, devuelve -1 o -2 respectivamente.
    """
    num_sin_espacios = sacar_espacios(numero_str)

    if not num_sin_espacios.isdigit():
        return -1

    numero = int(num_sin_espacios)
    if numero < 0:
        return -2

    return numero

# 3.2.
def sanitizar_flotante(numero_str):
    """
    Brief: Convierte una cadena en un número flotante después de sanearla.

    Param:
    numero_str (str): La cadena que se desea convertir en un número flotante.

    Returns:
    float: Devuelve el número flotante obtenido después de sanear la cadena.
    Si la cadena no representa un número, es negativa, o tiene un formato incorrecto, devuelve un valor indicativo.
    - Si es un número flotante válido, devuelve el número flotante.
    - Si es un número flotante negativo, devuelve -2.
    - Si la cadena tiene caracteres inválidos, devuelve -1.
    - Si la cadena no coincide con un formato adecuado, devuelve -3.
    """
    num_sin_espacios = sacar_espacios(numero_str)
    if re.match(r'^\d+\.\d+$', num_sin_espacios):
        numero_float = float(num_sin_espacios)
    elif re.match(r'^-\d+\.\d+$', num_sin_espacios):
        numero_float = -2
    elif re.search(r'[^0-9.-]', num_sin_espacios):
        numero_float = -1
    else:
        numero_float = -3
    
    return numero_float

#3.3.
def sanitizar_string(valor_str:str,valor_por_defecto = "-"):
    """
    Brief: Modifica una cadena de texto según ciertas reglas establecidas.

    Param:
    valor_str (str): La cadena de texto que se desea modificar.
    valor_por_defecto (str): El valor por defecto que se utilizará si la cadena es vacía.

    Returns:
    str: Devuelve la cadena de texto modificada según las reglas establecidas.
    - Si la cadena original es vacía y el valor por defecto no lo es, devuelve el valor por defecto en minúsculas sin espacios al inicio o final.
    - Si la cadena contiene números, devuelve "N/A".
    - Si la cadena contiene una barra "/", reemplaza la barra por un espacio y devuelve la cadena en minúsculas sin espacios al inicio o final.
    - En otros casos, devuelve la cadena original en minúsculas sin espacios al inicio o final.
    """
    if len(valor_str) == 0 and len(valor_por_defecto)>0:
        string_con_espacios = valor_por_defecto.lower()
        string = string_con_espacios.strip()

    else:
        verificar_string = re.search(r"[0-9]",valor_str)
        verificar_barra = re.search(r"/",valor_str)
        if verificar_string:
            string = "N/A"
        else:
            if verificar_barra:
                string_con_espacios = re.sub(r"/"," ",valor_str)
                string_con_espacios_minusculas = string_con_espacios.lower()
                string = string_con_espacios_minusculas.strip()
            else:
                string = valor_str.lower()

    return string

#3.4.
def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):
    """
    Brief: Modifica un valor específico de un héroe según su clave y el tipo de dato deseado.

    Param:
    heroe (dict): El diccionario que representa al héroe.
    clave (str): La clave del diccionario que se desea modificar.
    tipo_dato (str): El tipo de dato al que se desea convertir el valor de la clave.

    Returns:
    bool: Devuelve True si la modificación se realizó con éxito, False si no se pudo realizar.
    - Verifica si el tipo de dato es reconocido ('string', 'flotante', 'entero'). Si no lo es, devuelve False.
    - Verifica si la clave especificada existe en el diccionario del héroe. Si no existe, devuelve False.
    - Si el tipo de dato es 'string', modifica la clave del héroe usando la función sanitizar_string.
    - Si el tipo de dato es 'flotante', modifica la clave del héroe usando la función sanitizar_flotante.
    - Si el tipo de dato es 'entero', modifica la clave del héroe usando la función sanitizar_entero.
    """
    estado = True
    tipo_dato_minuscula = tipo_dato.lower()
    lista_tipo_dato = ["string","flotante","entero"]

    if tipo_dato_minuscula not in lista_tipo_dato: 
        print("Tipo de dato No reconocido")
        estado = False
    if clave not in heroe:
        print("La clave especificada no existe en el heroe.")
        estado = False

    if tipo_dato == "string":
        heroe[clave] = sanitizar_string(heroe[clave])
    elif tipo_dato == "flotante":
        heroe[clave] = sanitizar_flotante(heroe[clave])
    elif tipo_dato == "entero":
        heroe[clave] = sanitizar_entero(heroe[clave])

    return estado

def stark_normalizar_datos(lista_heroes:list):
    """
    Brief: Normaliza los datos de una lista de héroes ajustando tipos de datos específicos.

    Param:
    lista_heroes (list): Una lista que contiene diccionarios con información de los héroes.

    Returns:
    None: No devuelve ningún valor explícito.

    Description:
    - Si la lista de héroes no está vacía, itera sobre cada héroe en la lista.
    - Utiliza la función sanitizar_dato para ajustar el tipo de datos de ciertas claves de cada héroe.
    - Las claves 'altura', 'peso' y 'fuerza' se convierten a tipo flotante.
    - Las claves 'color_ojos' y 'color_pelo' se convierten a tipo string.
    - La clave 'inteligencia' se convierte a tipo entero.
    - Imprime un mensaje indicando que los datos han sido normalizados si la lista no está vacía.
    - Si la lista de héroes está vacía, imprime un mensaje de error.
    """
    if len(lista_heroes)>0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe,"altura","Flotante") 
            sanitizar_dato(heroe,"peso","Flotante")
            sanitizar_dato(heroe,"color_ojos","String")
            sanitizar_dato(heroe,"color_pelo","String") 
            sanitizar_dato(heroe,"fuerza","Flotante")
            sanitizar_dato(heroe,"inteligencia","Entero")   
        print("Datos normalizados.")
    else:
        print("Error: Lista de heroes vacia")

def stark_imprimir_indice_nombre(lista_heroes:list):
    """
    Brief: Imprime un índice normalizado basado en los nombres de una lista de héroes.

    Param:
    lista_heroes (list): Una lista que contiene diccionarios con información de los héroes.

    Returns:
    None: No devuelve ningún valor explícito.

    Description:
    - Si la lista de héroes no está vacía, itera sobre cada héroe en la lista.
    - Obtiene el nombre del héroe, elimina espacios en los extremos, reemplaza "the" por espacios y normaliza espacios.
    - Imprime el nombre final con espacios reemplazados por guiones.
    - Si la lista de héroes está vacía, imprime un mensaje indicando que está vacía.
    """
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            nombre = heroe["nombre"]
            nombre_sin_espacios = nombre.strip()
            nombre_normalizado = nombre_sin_espacios.replace("the", " ")
            nombre_final = re.sub(r'\s+', '-', nombre_normalizado)

            print(nombre_final)
    else:
        print("Lista de héroes vacía")

def generar_separador(patron:str,largo:int, imprimir: bool = True):
    """
    Brief: Genera una cadena repetida basada en un patrón y un largo determinado.

    Param:
    patron (str): El patrón a repetir para generar la cadena.
    largo (int): La longitud de la cadena a generar.
    imprimir (bool): Un valor booleano que indica si se debe imprimir la cadena generada. Por defecto, es True.

    Returns:
    str: Devuelve la cadena generada según el patrón y el largo especificados.
    - Si el patrón tiene una longitud mayor a 0 y menor o igual a 2, y el largo está en el rango [1, 235],
    genera una cadena repitiendo el patrón según el largo especificado.
    - Si imprimir es True, imprime la cadena generada.
    - Si alguna condición no se cumple, devuelve "N/A" y no imprime nada.
    """
    if len(patron)>0 and len(patron)<=2 and largo>=1 and largo<=235:
        string_generado = patron * largo
        if imprimir:
            print(string_generado)
    else:
        string_generado = "N/A"

    return string_generado

def generar_encabezado(titulo:str):
    """
    Brief: Genera un encabezado con un título en mayúsculas y un separador de asteriscos.

    Param:
    titulo (str): El título que se convertirá a mayúsculas y se utilizará en el encabezado.

    Returns:
    str: Devuelve una cadena que representa un encabezado con el título en mayúsculas entre separadores de asteriscos.
    - Convierte el título a mayúsculas.
    - Genera un separador utilizando la función generar_separador con el patrón "*" y una longitud de 120, sin imprimirlo.
    - Crea el encabezado con el título en mayúsculas y entre los separadores generados.
    """
    titulo_mayusucla = titulo.upper()
    separador = generar_separador("*",120,False)
    string_encabezado = f"{separador}\n{titulo_mayusucla}\n{separador}"
    return string_encabezado

def imprimir_ficha_heroe(heroe:dict,id):
    encabezado_principal = generar_encabezado("PRINCIPAL")
    nombre_con_iniciales = stark_imprimir_nombre_con_iniciales(heroe)
    identidad_secreta = obtener_dato_formato(heroe["identidad"])
    consultora = obtener_dato_formato(heroe["empresa"])
    codigo_heroe = generar_codigo_heroe(heroe,id)
    string_info_principal = f"{encabezado_principal}\n\tNOMBRE DEL HEROE:\t\t {nombre_con_iniciales}\n\tIDENTIDAD SECRETA:\t\t{identidad_secreta}\n\tCONSULTORA:\t\t\t{consultora}\n\tCODIGO DE HEROE:\t\t{codigo_heroe}"
    encabezado_fisico = generar_encabezado("FISICO")
    altura = "{:.2f}".format(float(heroe["altura"]))
    peso = "{:.2f}".format(float(heroe["peso"]))
    fuerza = heroe["fuerza"]

    string_info_fisico = f"{encabezado_fisico}\n\tALTURA:\t\t{altura} cm.\n\tPESO:\t\t{peso} kg.\n\tFUERZA:\t\t{fuerza} N"
    encabezado_señas = generar_encabezado("SEÑAS PARTICULARES")
    color_ojos = heroe["color_ojos"]
    color_pelo = heroe["color_pelo"]
    string_info_señas = f"{encabezado_señas}\n\tCOLOR DE OJOS:\t\t{color_ojos}\n\tCOLOR DE PELO:\t\t{color_pelo}"


    string_principal = f"{string_info_principal}\n{string_info_fisico}\n{string_info_señas}"
    return string_principal

def stark_navegar_fichas(lista_heroes):
    if len(lista_heroes)<0:
        print("La lista de héroes está vacía.")
        return

    indice_actual = 0

    while True:
        print(imprimir_ficha_heroe(lista_heroes[indice_actual],indice_actual+1))

        opcion = input("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ 3 ] Salir\nIngrese su opción: ")

        if opcion == '1':
            indice_actual = (indice_actual - 1)
            if indice_actual == -1 :
                indice_actual = 23
        elif opcion == '2':
            indice_actual = (indice_actual + 1)
            if indice_actual == 24 :
                indice_actual = 0
        elif opcion == '3':
            print("Salio del menu")
            break
        else:
            print("Ingrese una opción valida")





menu = ["--------------------------------------------------------------------------------------\n\t\t\t\t MENU PRINCIPAL\n--------------------------------------------------------------------------------------",
        "1 - Imprimir la lista de nombres junto con sus iniciales","2 -Imprimir la lista de nombres y el código del mismo",
        "3 - Normalizar datos","4 - Imprimir índice de nombres", "5 - Navegar fichas","\n6.Salir"]



def imprimir_menu(menu:list):
    """
    Brief: Imprime un menú dado como una lista.

    Param:
    menu (list): Una lista que contiene las opciones del menú a imprimir.

    Returns:
    None: No devuelve ningún valor explícito.
    """
    for opcion in menu:
        print(opcion)

def validar_entero(numero:str):
    """
    Brief: Valida si una cadena representa un número entero.

    Param:
    numero (str): La cadena que se desea validar.

    Returns:
    bool: Devuelve True si la cadena representa un número entero, False en caso contrario.
    """
    return numero.isdigit()

def stark_menu_principal(lista:list):
    """
    Brief: Muestra un menú basado en una lista y solicita al usuario que ingrese una opción.

    Param:
    lista (list): Una lista que contiene las opciones del menú.

    Returns:
    int or bool: Devuelve un entero si la respuesta del usuario es un número válido según el menú.
    Si la respuesta no es un número entero, devuelve False.
    """
    imprimir_menu(lista)
    respuesta = (input("\nIngrese una opcion: "))
    if validar_entero(respuesta):
        return int(respuesta)
    else:
        return False