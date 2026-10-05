#EJERCICIO 1: FICHA DE CLIENTE
class Cliente():                                                                                #Crear clase cliente
    def __init__(self, nombre, cedula, telefono):                                               #Crear constructor "__init__" para inicializar los atributos "nombre", "cedula" y "telefono"
        self.nombre = nombre                                                                    #Inicializar el nombre, CI y Teléfono del Cliente, mediante el parametro "self"
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):                                                                          #Crear constructor "__str__" el cual devuelve una cadena
        return f"Nombre: {self.nombre}\nCédula: {self.cedula}\nTeléfono: {self.telefono}"       #Devolver la ficha del cliente


datos_cliente = Cliente("Eduardo", 502191, 981223817)                                           #Crear variable "datos cliente" que utilize la clase "Cliente"

print(datos_cliente)                                                                            #Imprimir la variable