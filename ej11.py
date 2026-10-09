class Estudiante:                                                   #Crear clase "Estudiantes"

    def __init__(self, nombre, notas):                              #Inicializar los atributos que contengan el nombre y las notas del Estudiante
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self):                                    #Crear metodo "calcular_promedio"
        promedio = 0                                                #Crear variable "promedio"
        for nota in self.notas:                                     #Recorrer por cada nota mediante bucle for
            promedio += nota                                        #Sumar el promedio con la nota actual
        promedio /= len(self.notas)                                 #Al terminar el bucle, dividi el promedio con la cantidad de notas
        return promedio                                             #Devolver el promedio

    def aprobar(self):                                              #Crear metodo "aprobar"
        print(f"Nota final: {self.calcular_promedio()}")            #Imprimir la nota promedio del alumno
        if(self.calcular_promedio() >= 3):                          #Revisar si la nota promedio es mayor o igual a la nota minima para aprobar (en este caso, 3)
            return "Aprobado"                                       #Si es mayor o igual, aprobar
        else:
            return "Reprobado"                                      #Si es menor, reprobar

    def __str__(self):                                              #Devolver todos los atributos de la clase con metodo "__str__"
        return f"Estudiante: {self.nombre}\nNotas: {self.notas}"

notas1 = [5, 4, 3, 3, 5]                                            #Crear a dos estudiantes que utilicen la clase "Estudiante", cada uno con su propia nota y nombre
estudiante1 = Estudiante("Miguel", notas1)

notas2 = [4, 2, 2, 1, 3]
estudiante2 = Estudiante("Jorge", notas2)

print(estudiante1)                                                  #Imprimir los datos de cada estudiante como también si aprobaron o no
print(estudiante1.aprobar())
print(estudiante2)
print(estudiante2.aprobar())