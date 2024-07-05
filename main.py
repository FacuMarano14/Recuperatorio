from funciones import *

seguir = True


while seguir:
    match menu():
        case "1":
            lista_posts = cargar_datos("posts.csv")
        case "2":
            imprimir_pantalla(lista_posts)
            pausar()
        case "3":
            asignar_valores(lista_posts)
            imprimir_pantalla(lista_posts)
            pausar()
        case "4":
            mejores_posts_csv(lista_posts)
            pausar()
        case "5":
            haters_csv(lista_posts)
            pausar()
        case "6":
            promedio = promedio_followers(lista_posts)
            print(promedio)
            pausar()
        case "7":
            guardar_ascendente_user_json(lista_posts)
            pausar()
        case "8":
            post_mas_likes = posteo_mas_likeado(lista_posts)
            print(post_mas_likes)
            pausar()
        case "9":
            seguir = False