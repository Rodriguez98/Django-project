from django.db import models

# Create your models here.

class Carrera(models.Model):
    carrera = models.CharField(max_length=70)

    def __str__(self):
        return self.carrera

class Asignatura(models.Model):
    asignatura = models.CharField(max_length=70)

    def __str__(self):
        return self.asignatura

class Modalidad(models.Model):
    modalidad = models.CharField(max_length=70)

    def __str__(self):
        return self.modalidad

class Laboratorio(models.Model):
    laboratorio = models.CharField(max_length=70)

    def __str__(self):
        return self.laboratorio

class Docente(models.Model):
    docente = models.CharField(max_length=70)

    def __str__(self):
        return self.docente
class Turno(models.Model):
    turno = models.CharField(max_length=70)

    def __str__(self):
        return self.turno
class Area(models.Model):
    area = models.CharField(max_length=70)
    carrera = models.ForeignKey(Carrera, on_delete = models.CASCADE)

    def __str__(self):
        return self.area

#class Persona(models.Model):
#    email = models.EmailField(unique=True)
#    nombres = models.CharField(max_length=70)
#   apellidos = models.CharField(max_length=70)
#    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
#    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
#    fecha_nacimiento = models.DateField(null=True)

class Reservaciones(models.Model):
    descripcion = models.CharField(max_length=70)
    area = models.ForeignKey(Area, on_delete = models.CASCADE)
    #revisar
    docente = models.ForeignKey(Docente, on_delete = models.CASCADE)
    turno = models.ForeignKey(Turno, on_delete = models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete = models.CASCADE)
    modalidad = models.ForeignKey(Modalidad, on_delete = models.CASCADE)
    fecha = models.DateField(null=True)
    horarioInicio = models.CharField(max_length=70)
    dhorarioFin = models.CharField(max_length=70)
    estado_lab = models.BooleanField(),
    laboratorio = models.ForeignKey(Laboratorio, on_delete = models.CASCADE)

    list_display = ('id', 'descripcion', 'horario')

    def __str__(self):
        return self.descripcion

