class Habitacion:

    def __init__(self, numero, tarifa, estado):
        self.numero = numero
        self.tarifa = tarifa
        self.estado = estado

    def ocupar_habitacion(self):
        if(self.estado == True):
            self.estado = False
            return "La habitación ahora está ocupada."
        elif(self.estado == False):
            return "La habitación ya estaba ocupada."

    def liberar_habitacion(self):
        if(self.estado == False):
            self.estado = True
            return "La habitación ahora está liberada."
        elif(self.estado == True):
            return "La habitación ya estaba liberada."

    def calcular_tarifa(self, noches):
        return f"La tarifa total es: {self.tarifa * noches}"

    def __str__(self):
        estado_habitacion = ""
        if(self.estado == True):
            estado_habitacion = "Libre"
        elif(self.estado == False):
            estado_habitacion = "Ocupado"

        return f"Habitación N°{self.numero}\nTarifa por Noche: {self.tarifa}Gs\nEstado: {estado_habitacion}"

habitacion_hotel = Habitacion(81, 150000, False)

print(habitacion_hotel)
print(habitacion_hotel.ocupar_habitacion())
print(habitacion_hotel.liberar_habitacion())
print(habitacion_hotel.ocupar_habitacion())
print(habitacion_hotel.calcular_tarifa(5))
print(habitacion_hotel.liberar_habitacion())