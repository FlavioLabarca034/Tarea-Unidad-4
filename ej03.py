aguinaldo = True                                                                                        #Definir variable "Aguinaldo"

while(True):                                                                                            #Crear while loop que se repita hasta que se confirme si se considera el aguinaldo o no dentro de la empresa
    respuesta = input("Considerar aguinaldo? S/N?\n")                                                   #Crear condicional if que confirme si se considera o no el aguinaldo. Repetir si se da un valor incorrecto                                              
    if(respuesta.lower() == "s" or respuesta.lower() == "si"):
        aguinaldo = True
        break
    elif(respuesta.lower() == "n" or respuesta.lower() == "no"):
        aguinaldo = False
        break
    else:
        print("Valor incorrecto, por favor ingrese otro valor.")


class empleado:                                                                                         #Crear clase "empleado"
    def __init__(self, nombre, cargo, salario_mensual):                                                 #Inicializar el nombre, cargo, y salario mensual del empleado
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def salario_anual(self):                                                                            #Definir metodo que devuelva el salario anual
        if(aguinaldo):                                                                                  #Revisar si se considera el aguinaldo o no
            return f"Salario Anual: {self.salario_mensual * 13}"                                        #Multiplicar por 13 (12 meses del año + aguinaldo) si se considera
        return f"Salario Anual: {self.salario_mensual * 12}"                                            #Multiplicar por 12 sino

    def __str__(self):                                                                                  #Devolver las variables de la clase
        return f"Empleado: {self.nombre}\nCargo: {self.cargo}\nSalario Mensual: {self.salario_mensual}"

datos_empleado = empleado("Carlos", "Marketing", 2800000)                                               #Crear variable "datos_empleado" que utilice la clase "empleado"                                          

print(datos_empleado)                                                                                   #Imprimir los datos del empleado como también el salario anual
print(datos_empleado.salario_anual())
