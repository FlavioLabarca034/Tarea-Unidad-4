class Libro:                                                                            #Crear clase "Libro" mediante metodo "__init__"
    def __init__(self, nombre, autor, estado = True):                                   #Inicializar las variables que contienen el nombre, autor, y estado del libro
        self.nombre = nombre
        self.autor = autor
        self.estado = estado

    def __str__(self):                                                                  #Imprimir las variables mediante metodo "__str__"
        libro_estado = ""                                                               #Crear variable "libro_estado"
        if(self.estado):                                                                #Revisar el estado del libro, e definir "libro_estado" como "Disponible" o "Prestado" dependiendo del estado
            libro_estado = "Disponible"
        else:
            libro_estado = "Prestado"

        return f"Título: {self.nombre}\nAutor: {self.autor}\nEstado: {libro_estado}"    #Devolver el nombre, autor, y estado del libro

libro1 = Libro("Blancanieves", "Hermanos Grimm", True)                                  #Usar la clase creada para definir 2 libros, cada uno con diferentes datos
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", False)

print(f"Libros:\n{libro1}\n"                                                            #Imprimir los dos libros
      f"\n{libro2}")