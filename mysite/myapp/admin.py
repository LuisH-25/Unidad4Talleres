from django.contrib import admin
from .models import Salon, Alumno, Profesor, Examen_Final, Proyecto

# Register your models here.

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'aula',
        'hora_entrada',
        'idProfesor',
        )

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'idSalon',
        )


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'salario',
        'full_name',
        )

@admin.register(Examen_Final)
class ExamenFinalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'hora_fecha',
        'curso',
        'evaluador',
        'duracion_examen',
        'numero_preguntas',
        'puntaje_total',
        'Puntaje_pregunta',
        )

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'hora_fecha',
        'curso',
        'evaluador',
        'tema_proyecto',
        'numero_grupos',
        )
    ordering=(
        'tema_proyecto',
        )

