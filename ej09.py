class Turno:                                                                                                            #Crear clase "Turno"

    def __init__(self, paciente, hora, estado):                                                                         #Inicializar atributos que contengan el paciente, la hora, y el estado del turno
        self.paciente = paciente
        self.hora = hora
        self.estado = estado

    def atender_turno(self):                                                                                            #Crear metodo "atender_turno"
        self.estado = True                                                                                              #Convertir el estado del turno a "True" o "Atendido"
        return f"{self.paciente} fue atendido.\n"

    def __str__(self):                                                                                                  #Devolver los atributos de la clase mediante metodo "__str__"
        estado_paciente = ""                                                                                            #Crear variable "estado_paciente" que este vacío
        if(self.estado == True):                                                                                        #Revisar si el estado es "True" o "False"
            estado_paciente = "Atendido"                                                                                #Si es True, definir el estado del paciente como "Atendido"
        elif(self.estado == False):
            estado_paciente = "Pendiente"                                                                               #Si es False, definirlo como "Pendiente"

        return f"Nombre del Paciente: {self.paciente}\nHora de atención: {self.hora}\nEstado: {estado_paciente}"

class Agenda:                                                                                                           #Crear clase "Agenda"

    def __init__(self):                                                                                                 #Inicializar el atributo "self"
        self.lista_turnos = []                                                                                          #Crear atributo "lista_turnos" que contenga la lista de todos los turnos

    def agregar_turno(self, turno):                                                                                     #Crear metodo "agregar_turno" con parametro "turno"
        self.lista_turnos.append(turno)                                                                                 #Añadir un turno a la lista de turnos
        return f"Turno agregado: {turno.paciente} a la hora {turno.hora}\n"                                             #Devolver el nombre del paciente y la hora del turno recien añadido

    def listar_pendientes(self):                                                                                        #Crear metodo "listar_pendientes"
        if(len(self.lista_turnos) <= 0):                                                                                #Revisar si la cantidad de turnos es menor o igual a 0
            print("No hay pacientes en la agenda. Por favor agregue uno.\n")                                            #Si lo es, imprimir el sgte. mensaje y terminar el metodo.
            return
        print("Pacientes que falta atender:")                                                                           #Sino, imprimir el sgte. mensaje
        hay_pendiente = False                                                                                           #Crear variable "hay_pendiente" con valor "False"
        for turno in self.lista_turnos:                                                                                 #Recorrer por cada turno dentro de la lista
            if(turno.estado == False):                                                                                  #Revisar si el estado del turno actual es False/Pendiente
                print(f"{turno}\n")                                                                                     #Si lo es, imprimir el turno actual
                hay_pendiente = True                                                                                    #Definir "hay_pendiente" como True
        if(hay_pendiente == False):                                                                                     #Revisar si "hay_pendiente" sigue siendo False
            print("No hay ningún paciente pendiente.")                                                                  #Si lo es, imprimi el sgte. mensaje

            

turno1 = Turno("Ana", "15:30", False)                                                                                   #Crear varios turnos que utilicen la clase "Turno", cada uno con sus propios atributos
turno2 = Turno("David", "8:45", False)
turno3 = Turno("Maria", "9:30", False)
turno4 = Turno("Eduardo", "12:50", False)

agenda_pacientes = Agenda()                                                                                             #Crear una agenda que utilice la clase "Agenda"

agenda_pacientes.listar_pendientes()                                                                                    #Imprimir una simulación de jornada, es decir, que se imprima los pacientes pendientes, agregar pacientes, atender turnos, etc.
print(agenda_pacientes.agregar_turno(turno1))
agenda_pacientes.listar_pendientes()
print(agenda_pacientes.agregar_turno(turno2))
print(agenda_pacientes.agregar_turno(turno3))
print(agenda_pacientes.agregar_turno(turno4))
agenda_pacientes.listar_pendientes()
print(turno1.atender_turno())
print(turno2.atender_turno())
agenda_pacientes.listar_pendientes()