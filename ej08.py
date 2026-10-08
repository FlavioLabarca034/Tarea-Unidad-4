class Cancion:                                                                                          #Crear clase "Cancion"
    def __init__(self, titulo, artista, duracion):                                                      #Inicializar las variables que contengan el titulo, artista, y duracion de la canción
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):                                                                                  #Devolver todas las variables mediante el metodo "__str__"
        return f"Título: {self.titulo}\nArtista: {self.artista}\nDuración: {self.duracion} minutos"

class ListaReproduccion:                                                                                #Crear clase "ListaReproduccion"
    def __init__(self, nombre_lista):                                                                   #Inicializar la variable que contenga el nombre de la lista
        self.nombre_lista = nombre_lista
        self.lista_canciones = []                                                                       #Crear variable "lista_canciones" en donde se guarden las canciones

    def agregar_cancion(self, cancion):                                                                 #Crear metodo "agregar_cancion"
        self.lista_canciones.append(cancion)                                                            #Añadir una canción a la lista "lista_canciones"

        return f"Canción agregada: {cancion.titulo}"                                                    #Devolver el titulo de la canción recien añadida

    def duracion_total(self):                                                                           #Crear metodo "duracion_total"
        total = 0                                                                                       #Crear variable "total"
        for cancion in self.lista_canciones:                                                            #Recorrer por cada canción dentro de la lista "lista_canciones"
            total += cancion.duracion                                                                   #Sumar el total con la duración de la canción actual

        return f"Duración total de la lista: {total} minutos."                                          #Devolver la duración total

    def imprimir_lista(self):                                                                           #Crear metodo "imprimir_lista"
        print(f"Nombre de lista: {self.nombre_lista}\n"                                                 #Imprimir el nombre actual de la lista
              f"Canciones:\n")
        if(len(self.lista_canciones) > 0):                                                              #Revisar si la cantidad de canciones dentro de la lista es mayor a 0
            for cancion in self.lista_canciones:                                                        #Si se cumple, recorrer por cada canción dentro de la lista e imprimirla
                print(f"{cancion}\n")
            
            print(self.duracion_total())                                                                #Al terminar el búcle for, imprimir la duración total de la lista
        else:
            print("No hay canciones en la lista. Por favor agregue una.")                               #Si no se cumple, imprimir el siguiente mensaje



cancion1 = Cancion("Bohemian Rhapsody", "Queen", 5)                                                     #Crear 3 canciones que utilicen la clase "Cancion", cada una con sus propios atributos
cancion2 = Cancion("We are the Champions", "Queen", 3)
cancion3 = Cancion("Another one Bites the Dust", "Queen", 3)

lista_musica = ListaReproduccion("Musica Queen")                                                        #Crear una lista de musica que utilice la clase "ListaReproduccion"

lista_musica.imprimir_lista()                                                                           #Imprimir la lista de música. Como no hay ningúna musica todavia, va a imprimir un mensaje de error.
print(lista_musica.agregar_cancion(cancion1))                                                           #Agregar una musica mediante el metodo "agregar_musica" e imprimir el valor que devuelve
lista_musica.imprimir_lista()                                                                           #Imprimir de nuevo la lista. Ahora que hay una canción, se imprime sin problemas
print(lista_musica.agregar_cancion(cancion2))                                                           #Agregar dos canciones más
print(lista_musica.agregar_cancion(cancion3))
lista_musica.imprimir_lista()                                                                           #Imprimir una vez más la lista, esta vez con 3 canciones.
