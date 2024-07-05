from os import system
from random import randint
import json

def limpiar_pantalla():
    """Limpia la pantalla
    """
    system("cls")
#-------------------------------------------------------------------------------------------------------------------------------------
def pausar():
    """Pausa la animacion entre operaciones
    """
    system("pause")
#-------------------------------------------------------------------------------------------------------------------------------------
def menu()-> str:
    """Menu de opciones

    Returns:
        str: opcion elegida
    """
    limpiar_pantalla()
    print("Menu de opciones")
    print("1 - Cargar Datos")
    print("2 - Imprimir Lista")
    print("3 - Asignar Estadistica")
    print("4 - Mejores Posts")
    print("5 - Haters")
    print("6 - Promedio Followers")
    print("7 - Ordenar Datos por Nombre Ascendente")
    print("8 - Mas popular")
    print("9 - Salir")
    opcion = input("Ingrese opcion: ")
    return opcion
#-------------------------------------------------------------------------------------------------------------------------------------
def get_acutal_path(nombre_archivo:str)->str:
    """Obtiene la ruta completa del archivo

    Args:
        nombre_archivo (str): Nombre del archivo

    Returns:
        str: Ruta del archivo
    """
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)
#-------------------------------------------------------------------------------------------------------------------------------------
def cargar_datos(nombre_archivo:str)-> list:
    """Carga los datos de un archivo CSV y los almacena en una lista de diccionarios.

    Returns:
        list: Lista de diccionarios con los datos del archivo CSV
    """
    with open(get_acutal_path(nombre_archivo), "r", encoding="utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")
        for linea in archivo.readlines():
            post = {}
            linea = linea.strip("\n").split(",")
            
            id, user, likes, dislikes, followers = linea
            post["id"] = int(id)
            post["user"] = user
            post["likes"] = int(likes)
            post["dislikes"] = int(dislikes)
            post["followers"] = int(followers)
            lista.append(post)
    return lista
#-------------------------------------------------------------------------------------------------------------------------------------
def imprimir_pantalla(lista: list):
    """Muestra la lista que se le pase

    Args:
        lista (list): lista que se muestra en pantalla
    """
    for dato in lista:
        print(f"{dato['id']}, {dato['user']}, {dato['likes']}, {dato['dislikes']}, {dato['followers']}")
#-------------------------------------------------------------------------------------------------------------------------------------
def asignar_likes(lista:list)->list:
    """Asigna likes aleatorios

    Args:
        lista (list): Le paso la lista con los likes en 0

    Returns:
        list: Le devuelvo la lista con valores aleatorios entre 500 y 3000
    """
    for elem in lista:
        tiempo = randint(500,3000)
        elem["likes"] = tiempo
    return lista
#-------------------------------------------------------------------------------------------------------------------------------------
def asignar_dislikes(lista:list)->list:
    """Asigna dislikes aleatorios

    Args:
        lista (list): Le paso la lista con los dislikes en 0

    Returns:
        list: Le devuelvo la lista con valores aleatorios entre 300 y 3500
    """
    for elem in lista:
        tiempo = randint(300,3500)
        elem["dislikes"] = tiempo
    return lista
#-------------------------------------------------------------------------------------------------------------------------------------
def asignar_followers(lista:list)->list:
    """Asigna followers aleatorios

    Args:
        lista (list): Le paso la lista con los followers en 0

    Returns:
        list: Le devuelvo la lista con valores aleatorios entre 10000 y 20000
    """
    for elem in lista:
        tiempo = randint(10000,20000)
        elem["followers"] = tiempo
    return lista
#-------------------------------------------------------------------------------------------------------------------------------------
def asignar_valores(lista:list)->list:
    """Asigna likes, dislikes y followers aleatorios

    Args:
        lista (list): lista de diccionarios con valores 0

    Returns:
        list: Lista con valores agregados
    """
    likes = asignar_likes(lista)
    dislikes = asignar_dislikes(lista)
    followers = asignar_followers(lista)
    return likes, dislikes, followers
#-------------------------------------------------------------------------------------------------------------------------------------
def guardar_archivo_csv(lista:list,nombre_archivo_csv)->any:
    """guardar_archivo_csv

    Args:
        lista (list): paso una lista
        nombre_archivo_csv (_type_): el nombre del archivo que quiero ponerle 

    Returns:
        any: no devuelve nada
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    with open(get_acutal_path(nombre_archivo_csv), "w", encoding="utf-8") as archivo: #hace lo mismo que el anterior pero aca pasa el nombre a mayusculas
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for persona in lista:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)

            linea = ",".join(l) + "\n"
            archivo.write(linea)
#-------------------------------------------------------------------------------------------------------------------------------------
def mejores_posts(lista:list)->list:
    """Deuvelve lista con posts de mas de 2000 likes

    Args:
        lista (list): lista de diccionarios con info de posts

    Returns:
        list: lista de posts con mas de 2000 likes
    """
    lista_retorno = []
    for el in lista:
        if el["likes"] > 2000:
            lista_retorno.append(el)
    return lista_retorno
#-------------------------------------------------------------------------------------------------------------------------------------
def mejores_posts_csv(lista:list):
    """Guarda los mejores posts en un archivo CSV

    Args:
        lista (list): lista de diccionarios con info de posts

    Returns:
        _type_: None
    """
    mej_posts = mejores_posts(lista)
    mej_posts_csv = guardar_archivo_csv(mej_posts, "mejores_posts.csv")
    return mej_posts_csv
#-------------------------------------------------------------------------------------------------------------------------------------
def haters(lista:list)->list:
    """Devuelve lista de posts con mas dislikes que likes

    Args:
        lista (list): lista de diccionarios con info de posts

    Returns:
        list: lista de posts con mas dislikes que likes
    """
    lista_retorno = []
    for el in lista:
        if el["likes"] < el["dislikes"]:
            lista_retorno.append(el)
    return lista_retorno
#-------------------------------------------------------------------------------------------------------------------------------------
#punto 5
def haters_csv(lista:list):
    """Guarda haters en un archivo CSV

    Args:
        lista (list): lista de diccionarios con info de posts

    Returns:
        _type_: none
    """
    lista_haters = haters(lista)
    hate_csv = guardar_archivo_csv(lista_haters, "haters.csv")
    return hate_csv
#-------------------------------------------------------------------------------------------------------------------------------------
def mapear_followers(lista:list)->list:
    """Mapea followers de la lista de diccionarios a una lista de enteros

    Args:
        lista (list): lista de diccionarios con info de posts

    Returns:
        list: _description_
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el["followers"]))
    return lista_retorno

#-------------------------------------------------------------------------------------------------------------------------------------
def totalizar_listas(lista:list)->int:
    """Suma todos los elementos de una lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        int: La suma de todos los números en la lista.
    """
    total = 0
    for numero in lista:
        total += numero
    return total
#-------------------------------------------------------------------------------------------------------------------------------------
def calcular_promedio_3(lista:list)->float:
    """Calcula el promedio de una lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        float: El promedio de los números en la lista.

    Raises:
        ValueError: Si la lista está vacía.
    """
    cant = len(lista)
    if cant == 0:
        raise ValueError("No esta definido el promedio de una lista vacia")
    return totalizar_listas(lista) / cant
#-------------------------------------------------------------------------------------------------------------------------------------
def promedio_followers(lista:list)->str:
    """Calcula promedio de followers de una lista de posts

    Args:
        lista (list): lista de diccionarios con info de posts

    Returns:
        str: Mensaje con el promedio de followers
    """
    followers = mapear_followers(lista)
    promedio = calcular_promedio_3(followers)
    mensaje = f"El promedio de followers es de: {promedio:.0f}"
    return mensaje
#-------------------------------------------------------------------------------------------------------------------------------------
def ordenar_ascendente_por_users(lista)->list:
    """Ordena una lista de posts en orden ascendente segun usuario.

    Args:
        lista (list): Lista de diccionarios con información de posts.

    Returns:
        list: Lista ordenada en orden ascendente segun usuario.

    Raises:
        TypeError: Si el primer parámetro no es una lista.
    """
    if not isinstance(lista, list): raise TypeError ("primer parametro debe ser una lista")
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j]['user'] < lista[min_idx]['user']:
                min_idx = j
        # Intercambiar elementos
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista
#-------------------------------------------------------------------------------------------------------------------------------------
def guardar_archivo_json(archivo_json, posts)->None:
    """Guarda una lista de posts en un archivo JSON.

    Args:
        archivo_json (str): El nombre del archivo JSON.
        posts (list): Lista de diccionarios con información de posts.

    Returns:
        None
    """
    with open(get_acutal_path(archivo_json), "w", encoding="utf-8") as archivo_json:
        return json.dump(posts, archivo_json, indent = 4)
#-------------------------------------------------------------------------------------------------------------------------------------
def guardar_ascendente_user_json(lista: list)->None:
    """Ordena una lista de posts en orden ascendente por usuario y guarda los resultados en un archivo JSON.

    Args:
        lista (list): Lista de diccionarios con información de posts.

    Returns:
        None
    """
    orden_ascendente_users = ordenar_ascendente_por_users(lista)
    archivo_json = guardar_archivo_json("ord_asc_user.json", orden_ascendente_users)
    return archivo_json
#-------------------------------------------------------------------------------------------------------------------------------------
def calcular_mayor(lista:list)->int:
    """Calcula el numero mas grande de una lista

    Args:
        lista (list): Lista de numeros

    Raises:
        ValueError: Si la lista esta vacia lanza este error

    Returns:
        int: El numero mas grande de la lista
    """
    if not lista:
        raise ValueError("No esta definido el mayor de una lista vacia")
    
    flag = False
    for numero in lista:
        if flag == False or numero > num_mayor:
            num_mayor = numero
            flag = True
    return num_mayor
#-------------------------------------------------------------------------------------------------------------------------------------
def mapear_likes_users(lista:list)->list:
    """Mapea lista de diccionarios a lista de tuplas con likes y usuarios

    Args:
        lista (list): lista de diccionarios con claves "likes" y "user"

    Returns:
        _type_: Lista de tuplas en la que cada tupla tiene likes y usuario
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append((el["likes"], el["user"]))
    return lista_retorno
#-------------------------------------------------------------------------------------------------------------------------------------
def posteo_mas_likeado(lista:list)->str:
    """Indica posteo mas likeado de una lista de posts

    Args:
        lista (list): lista de diccionarios con info de posts

    Returns:
        None: Imprime el usuario y los likes del post con mas likes
    """
    likes_user = mapear_likes_users(lista)
    posteo_mas_likes = calcular_mayor(likes_user)
    mensaje = f"El posteo mas likeado es el de {posteo_mas_likes[1]} con {posteo_mas_likes[0]} likes"
    return mensaje
#-------------------------------------------------------------------------------------------------------------------------------------
