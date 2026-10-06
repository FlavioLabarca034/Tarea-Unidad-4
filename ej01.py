class Cliente():                                                                                #Crear clase cliente
    def __init__(self, nombre, cedula, telefono):                                               #Crear constructor "__init__" para inicializar los atributos "nombre", "cedula" y "telefono"
        self.nombre = nombre                                                                    #Inicializar el nombre, CI y Teléfono del Cliente, mediante el parametro "self"
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):                                                                          #Crear constructor "__str__" el cual devuelve una cadena
        return f"Nombre: {self.nombre}\nCédula: {self.cedula}\nTeléfono: {self.telefono}"       #Devolver la ficha del cliente


cliente1 = Cliente("Eduardo", 502191, 981223817)                                                #Crear variables "cliente1" y "cliente2" que utilizen la clase "Cliente"
cliente2 = Cliente("Ana", 4523022, 994321556)

print(f"CLIENTE 1:\n{cliente1}\n"
      f"CLIENTE 2:\n{cliente2}")                                                                #Imprimir las variable