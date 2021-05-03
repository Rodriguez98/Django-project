from django.db import models

# Create your models here.


class Sexo(models.Model):
    sexo = models.CharField(max_length=70)

    def __str__(self):
        return self.sexo


class Area(models.Model):
    area = models.CharField(max_length=70)

    def __str__(self):
        return self.area


class Carrera(models.Model):
    carrera = models.CharField(max_length=70)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.carrera


class Asignatura(models.Model):
    asignatura = models.CharField(max_length=200)

    def __str__(self):
        return self.asignatura


class Modalidad(models.Model):
    modalidad = models.CharField(max_length=70)

    def __str__(self):
        return self.modalidad


class Turno(models.Model):
    turno = models.CharField(max_length=70)

    def __str__(self):
        return self.turno


class Laboratorio(models.Model):
    laboratorio = models.CharField(max_length=70)

    def __str__(self):
        return self.laboratorio
