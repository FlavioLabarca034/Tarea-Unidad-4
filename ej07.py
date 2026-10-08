class Producto:                                                                                                     #Crear clase "Producto" la cual es similar a la del ejercicio 2
    def __init__(self, nombre, precio_unitario, cant_stock, stock_minimo):                                          #Inicializar los mismos datos, solo con la adición de un nuevo dato "stock_minimo"              
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cant_stock = cant_stock
        self.stock_minimo = stock_minimo

    def total(self):                                                                                                #Crear metodo "total" igual al del ejercicio 2
                return f"Valor en total: {self.precio_unitario * self.cant_stock}"

    def ingresar_mercaderia(self, mercaderia):                                                                      #Crear un nuevo metodo "ingresar mercaderia"
        if mercaderia > 0:                                                                                          #Revisar si la mercaderia ingresada es mayor a 0
            self.cant_stock += mercaderia                                                                           #Si lo es, se añade la cantidad ingresada a la mercadería total, y se devuelve tanto el stock añadido como también el stock total
            return f"Stock añadido: {mercaderia}"
        else:
             return "Error. Por favor ingrese una cantidad mayor a 0."                                              #Sino, devolver un mensaje de error

    def registrar_venta(self, venta):                                                                               #Crear nueva función "registrar_venta"
        if venta <= self.cant_stock:                                                                                #Revisar si la venta ingresada no excede la cantidad total de stock
            self.cant_stock -= venta                                                                                #Si no excede, se resta el stock con la venta
            if self.cant_stock < self.stock_minimo:                                                                 #Revisar si la cantidad total de stock es menor al stock minimo
                return f"Stock Vendido: {self.cant_stock}\nCantidad total: {self.cant_stock}\nAdvertencia: la cantidad de {self.nombre}s está por debajo del mínimo."   #Si lo es, devolver el stock vendido/total, y un mensaje de advertencia
            return f"Stock vendido: {venta}\nCantidad total: {self.cant_stock}"                                     #Sino, devolver solamente el stock vendido y total
        return "Error. Stock insuficiente"                                                                          #Si la cantidad de ventas se excede, devolver un mensaje de error

    def __str__(self):                                                                                              #Devolver el nombre, precio, y cantidad total del producto
            return f"Producto: {self.nombre}\nPrecio: {self.precio_unitario}\nCantidad en stock: {self.cant_stock}"

tomate = Producto("Tomate", 6500, 15, 5)                                                                            #Crear un nuevo producto/variable"Tomate" que utilice la clase "Producto"

print(tomate)                                                                                                       #Imprimir los datos del producto como también lo siguiente:
print(tomate.total())                                                                                               #Su valor total
print(tomate.ingresar_mercaderia(3))                                                                                #El stock añadido y total
print(tomate.total())                                                                                               #Su nuevo valor total
print(tomate.registrar_venta(16))                                                                                   #El stock vendido y total
print(tomate.total())                                                                                               #Su nuevo valor total
print(tomate.registrar_venta(5))                                                                                    #El stock vendido, pero como este es mayor al stock total, se devuelve un mensaje de error

           

    