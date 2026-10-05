#EJERCICIO 1: FICHA DE CLIENTE
class Cliente():
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}\nCédula: {self.cedula}\nTeléfono: {self.telefono}"


datos_cliente = Cliente("Eduardo", 502191, 981223817)

print(datos_cliente)