class CuentaBancaria:                                               #Crear clase "CuentaBancaria"
    def __init__(self, saldo):                                      #Inicializar la variable que contenga el saldo de la cuenta
        self.saldo = saldo

    def acreditar(self, monto):                                     #Crear metodo "acreditar" con variable "monto"
        if monto > 0:                                               #Revisar si el monto ingresado es mayor a 0
            self.saldo += monto                                     #Si es mayor, sumar el monto que sea ingresado con el saldo y devolver el monto agregado
            return f"Saldo acreditado: {monto}"
        else:
            return "Error. Por favor ingrese un monto mayor a 0."   #Sino, devolver un mensaje de error

    def registrar_consumo(self, consumo):                           #Crear metodo "registrar_insumo" con variable "consumo"
        if consumo <= self.saldo:                                   #Revisar si el consumo ingresado no exceda el saldo actual
            self.saldo -= consumo                                   #Si no se excede, restar el saldo con el consumo y devolver la cantidad extraída
            return f"Saldo extraído: {consumo}"
        return "Error. Saldo Insuficiente."                         #Si se excede, devolver un mensaje de error.

    def __str__(self):                                              #Devolver el saldo actual de la cuenta mediante metodo "__str__"
        return f"Saldo actual: {self.saldo}"

cuenta = CuentaBancaria(500000)                                     #Crear variable "cuenta" que use la clase "CuentaBancaria" y tenga un saldo de 500000

print(cuenta)                                                       #Imprimir una serie de operaciones realizadas con la cuenta (acreditación, consumo, y consumo si el saldo es insufiente) e imprimir el saldo total de la cuenta despues de cada operación
print(cuenta.acreditar(50000))
print(cuenta)
print(cuenta.registrar_consumo(400000))
print(cuenta)
print(cuenta.registrar_consumo(250000))
print(cuenta)