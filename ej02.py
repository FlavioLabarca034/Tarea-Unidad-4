class Producto:                                                                                                     #Crear clase "Producto"
    def __init__(self, nombre, precio_unitario, cant_stock):                                                        #Inicializar el nombre, precio unitario, y la cantidad de stock de la clase
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cant_stock = cant_stock

    def total(self):                                                                                                #Crear metodo "total" que devuelva el valor total del producto (precio * cantidad)
        return f"Valor en total: {self.precio_unitario * self.cant_stock}"

    def __str__(self):                                                                                              #Imprimir las variables de la clase
        return f"Producto: {self.nombre}\nPrecio: {self.precio_unitario}\nCantidad en stock: {self.cant_stock}"

tomate = Producto("Tomate", 5000, 10)                                                                               #Definir 3 distintos productos que utilizen la clase "Productos"
zanahoria = Producto("Zanahoria", 7500, 20)
lechuga = Producto("Lechuga", 6000, 15)

print(f"Producto 1:\n{tomate}\n{tomate.total()}"                                                                    #Imprimir los 3 productos, como también su valor total
      f"\n\nProducto 2:\n{zanahoria}\n{zanahoria.total()}"
      f"\n\nProducto 3:\n{lechuga}\n{lechuga.total()}")