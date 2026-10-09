class Item:                                                 #Reutilizar la clase "Producto" del ejercicio 2

    def __init__(self, nombre, precio_unitario, cant_stock):
            self.nombre = nombre
            self.precio_unitario = precio_unitario
            self.cant_stock = cant_stock
    
    def total(self):
        return self.precio_unitario * self.cant_stock
    
    def __str__(self):
        return f"Producto: {self.nombre}\nPrecio: {self.precio_unitario}\nCantidad en stock: {self.cant_stock}\nPrecio total: {self.total()}"

class Carrito:                                              #Crear Clase "Carrito"

    def __init__(self):                                     #Inicializar el atributo "self"
        self.lista_items = []                               #Crear lista "lista_items"

    def agregar_item(self, item):                           #Crear metodo "agregar_item" con parametro "item"
        self.lista_items.append(item)                       #Agregar un item a la lista
        return f"Item agregado: {item.nombre}\n"            #Devolver el item recien agregado

    def precio_total(self):                                 #Crear metodo "precio_total"
        total = 0                                           #Crear variable "total"
        for item in self.lista_items:                       #Recorrer por cada item dentro de la lista con bucle for
            total += item.total()                           #Sumar el total con el precio total (cantidad * precio unitario) del item actual
        return f"El total a pagar es: {total}"              #Devolver el total

    def mostrar_productos(self):                            #Crear metodo "mostrar_productos"
        if(len(self.lista_items)<= 0):                      #Revisar si la cantidad de items en la lista es menor o igual a 0
            print("No hay items. Porfavor agregue uno.\n")  #Si lo es, imprimir el sgte. mensaje y terminar el metodo
            return
        print("Los items son:")
        for item in self.lista_items:                       #Sino, recorrer por cada item dentro de la lista con bucle for
            print(f"{item}\n")                              #Imprimir el item actual
        print(self.precio_total())                          #Imprimir el precio total al terminar el bucle

item1 = Item("Cereza", 6000, 10)                            #Crear 3 items que utilicen la clase "item" cada uno con sus propios atributos
item2 = Item("Pan", 10000, 4)
item3 = Item("Leche", 8000, 5)

carrito = Carrito()                                         #Crear variable "carrito" que utilice la clase con el mismo nombre

carrito.mostrar_productos()                                 #Realizar distintas operaciones (mostrar productos, agregar productos, etc.)
print(carrito.agregar_item(item1))
carrito.mostrar_productos()
print(carrito.agregar_item(item2))
print(carrito.agregar_item(item3))
carrito.mostrar_productos