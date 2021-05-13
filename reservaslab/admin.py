from django.contrib import admin

from .models import Reservaciones, Area, Carrera, Asignatura, Modalidad, Laboratorio, Docente, Turno

# Register your models here.

admin.site.register(Reservaciones)
admin.site.register(Area)
admin.site.register(Carrera)
admin.site.register(Asignatura)
admin.site.register(Modalidad)
admin.site.register(Laboratorio)
admin.site.register(Docente)
admin.site.register(Turno)
