from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  
db = client["Tienda_Musica"]


albumes = db['albumes']
albumes.insert_many([
    {"titulo": "AM", "artista": "Arctic Monkeys", "anio": 2013},
    {"titulo": "Thriller", "artista": "Michael Jackson", "anio": 1982},
    {"titulo": "Genesis", "artista": "Peso Pluma", "anio": 2023}
])


artistas = db['artistas']
artistas.insert_many([
    {"nombre": "Alex Turner", "genero": "alternativa", "pais": "Reino Unido"},
    {"nombre": "Michael Jackson", "genero": "Pop", "pais": "EE.UU."},
    {"nombre": "Peso Pluma", "genero": "Corridos", "pais": "México"}
])


canciones = db['canciones']
canciones.insert_many([
    {"titulo": "Arabella", "album": "AM", "duracion": 3.27, "precio": 1.99},
    {"titulo": "Billie Jean", "album": "Thriller", "duracion": 4.54, "precio": 2.99},
    {"titulo": "Rubicon", "album": "Genesis", "duracion": 3.58, "precio": 1.49}
])

def agregar_cancion():
    titulo = input("Ingrese el título de la canción: ")
    album = input("Ingrese el álbum de la canción: ")
    duracion = float(input("Ingrese la duración de la canción (en minutos): "))
    precio = float(input("Ingrese el precio de la canción: "))
    
    cancion = {
        "titulo": titulo,
        "album": album,
        "duracion": duracion,
        "precio": precio
    }
    
    canciones.insert_one(cancion)
    print("Canción agregada con éxito.")

def eliminar_cancion():
    titulo = input("Ingrese el título de la canción a eliminar: ")
    result = canciones.delete_one({"titulo": titulo})
    
    if result.deleted_count > 0:
        print("Canción eliminada con éxito.")
    else:
        print("Canción no encontrada.")

def actualizar_cancion():
    titulo = input("Ingrese el título de la canción a actualizar: ")
    campo = input("Ingrese el campo a actualizar (titulo, album, duracion, precio): ")
    nuevo_valor = input("Ingrese el nuevo valor: ")
    
    if campo == "duracion" or campo == "precio":
        nuevo_valor = float(nuevo_valor)
    
    result = canciones.update_one({"titulo": titulo}, {"$set": {campo: nuevo_valor}})
    
    if result.matched_count > 0:
        print("Canción actualizada con éxito.")
    else:
        print("Canción no encontrada.")

def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Agregar una canción")
        print("2. Eliminar una canción")
        print("3. Actualizar una canción")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_cancion()
        elif opcion == '2':
            eliminar_cancion()
        elif opcion == '3':
            actualizar_cancion()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 4.")

mostrar_menu()