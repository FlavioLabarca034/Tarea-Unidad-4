class linea_cliente:                                                                                        #Crear clase "linea_cliente"

    def __init__(self, cliente, gigabytes):                                                                 #inicializar los atributos que contengan el nombre y los gigabytes del cliente
        self.cliente = cliente
        self.gigabytes = gigabytes

    def consumo_gb(self, consumo):                                                                          #Crear metodo "consumo_gb"
        if(self.gigabytes == 0):                                                                            #Revisar si el cliente ya no tiene gigabytes
            return "Ya se te acabaron los gigabytes. Por favor renueve su plan."                            #Si no tiene, devolver este mensaje de error y terminar el metodo
        if(consumo >= self.gigabytes):                                                                      #Si todavia tiene, revisar si el consumo de gigabytes es mayor o igual que la cantidad de gigabytes del cliente
            self.gigabytes = 0                                                                              #Si lo es, convertir la cantidad de gigabytes a 0 y devolver un mensaje
            return "Se te han acabado los gigabytes. Por favor renueve su plan"
        self.gigabytes -= consumo                                                                           #Si no lo es, restar la cantidad de gigabytes con el consumo
        if(self.gigabytes <= 3):                                                                            #Revisar si la cantidad de gigabytes es menor o igual a 3
            return f"Gigabytes consumidos: {consumo}\nAdvertencia: se te están acabando los gigabytes."     #Si lo es, mostar el consumo total de gigabytes como también un mensaje de advertencia
        return f"Gigabytes consumidos: {consumo}"                                                           #Sino, solamente devolver el consumo total de gigabytes

    def informe(self):                                                                                      #Crear funcion "informe"
        return f"Cliente: {self.cliente}\nGigabytes restantes: {self.gigabytes}"                            #Devolver el nombre del cliente como también los gigabytes restantes del plan

cliente = linea_cliente("Andres", 15)                                                                       #Crear un cliente que utilice la clase de "linea_cliente"

print(cliente.informe())                                                                                    #Realizar distintas operaciones que contengan un informe de gigabytes o su consumo
print(cliente.consumo_gb(8))
print(cliente.informe())
print(cliente.consumo_gb(4))
print(cliente.informe())
print(cliente.consumo_gb(6))