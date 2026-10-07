class Vehiculo:                                                             #Crear clase "Vehiculo"
    def __init__(self, marca, modelo, año, precio):                         #Inicializar las variables que contengan la marca, modelo, año y precio del vehiculo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def descripcion_comercial(self):                                        #Crear metodo "descripcion_comercial" que devuelva las variables del vehiculo
        return f"{self.marca} {self.modelo} {self.año} - {self.precio}"

auto1 = Vehiculo("Toyota", "Camry", 2008, 45000000)                         #Crear dos variables "auto" que utilizen la clase "Vehiculo". Ambos con valores distintos
auto2 = Vehiculo("Ford", "F350", 2005, 85000000)

print(f"Vehiculos:"                                                         #Imprimir el valor devuelto por el metodo "descripcion_comercial"
      f"\n{auto1.descripcion_comercial()}"
      f"\n{auto2.descripcion_comercial()}")