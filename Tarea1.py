# Clase base

class Persona:
   def __init__(self, nombre = "X", apellido = "Y", edad = 0 ):
       self.nombre = nombre
       self.apellido = apellido
       self.edad = edad

   def info(self):
       print(f'Su nombre es: {self.nombre}, su apellido es: {self.apellido}, tiene {self.edad} años.')

   def año_de_nac(self):
       if (2022 - self.edad) >= 1903 :
          print("Nació entre:" + str(int(2021 - self.edad)) + " y " + str(int(2022 - self.edad)))
       else: print("Es la persona mas vieja sobre la tierra")

   def lon_nombre(self):
       print(len(self.nombre))

# Estudiante hereda de Persona
class Profesor(Persona):

         def __int__(self):
                super().__int__( nombre = "X", apellido = "Y", edad = 0 , escuela= 'Y', materia='X', horario='Z', num_alumnos=0):
                  self.escuela = escuela
                  self.materia = materia
                  self.horario = horario
                  self.num_alumnos = num_alumnos

         def info(self):
              print(f'El profesor {self.nombre} {self.apellido} de {self.edad} años de edad')

              print(f'Trabaja en: {self.escuela} impartiendo la clase de  {self.materia} a las {self.horario}')

         def ayudante(self):
              if self.num_alumnos >30 :
                 print(f' El profesor {self.nombre} {self.apellido} necesita por lo menos dos ayudantes')
              elif self.num_alumnos > 6 :
                 print(f'El profesor {self.nombre} {self.apellido} necesita un ayudante ')
              else: print(f'El profesor {self.nombre} {self.apellido} no necesita ayudantes')


# Estudiante hereda de Persona

class Estudiante(Persona):

        def __int__(self):
            super().__int__(self, escuela='x', materias='y', horario = 'z', promedio=0):
                self.escuela = escuela
                self.materias = materias
                self.horario = horario
                self.promedio = promedio

        def info(self):
               print(f'El alumno {self.nombre} {self.apellido} toma las materias de {self.materia} y lleva promedio de {self.promedio}')


        def aprobado(self):
            if self.promedio >= 6:
                print(f'El alumno {self.nombre} {self.apellido} tiene promedio aprobatorio')
            else: print(f'El alumno {self.nombre} {self.apellido} no podrá ')


#Ejemplo de Personas
persona1 = Persona("Juan", "Perez", 30)
persona1.info()
persona1.año_de_nac()
persona1.lon_nombre()

persona2 = Persona("Humberto", "Díaz",58)
persona2.info()
persona2.año_de_nac()
persona2.lon_nombre()


#Ejemplo Profesor
profesor1 = Profesor("Humberto", "Díaz",58, 'F.Ciencias', 'Geometria','10:30',30)
profesor1.info()
