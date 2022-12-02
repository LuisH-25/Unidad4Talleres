from django.db import models

# Create your models here.

class Persona(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        abstract = True

    @property                       # Transforma un metodo en un atributo
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name


class Profesor(Persona):
    salario = models.IntegerField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['first_name', 'last_name'], name = 'primary_key_profesor'
            )
        ]
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = [
            'first_name',
        ]
        
    def __str__(self):
        return self.first_name


class Salon(models.Model):
    # id = models.AutoField(primary_key=True)
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()
    idProfesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)      # si Profesor no puede ir arriba, hacer:    'Profesor'
    
    class Meta:
        verbose_name = 'Salon'
        verbose_name_plural = 'Salones'
        ordering = [
            'hora_entrada',
        ]

    def __str__(self):
        return self.aula


class Alumno(Persona):
    idSalon = models.ForeignKey(Salon, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        constraints = [
            models.UniqueConstraint(
                fields = ['first_name', 'last_name'], name = 'primary_key_alumno'
            )
        ]
    def __str__(self):
        return self.first_name


class OrderedAlum(Alumno):
    class Meta:
        ordering = [
            "first_name",
            "-last_name",
            ]
        proxy = True

class Evaluacion(models.Model):
    # id = models.AutoField(primary_key=True)
    hora_fecha = models.DateTimeField()
    curso = models.CharField(max_length=30)
    evaluador = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = 'Evaluaciones'
        abstract = True

    @property
    def full_name(self):
        return self.curso + " " + self.evaluador

    def __str__(self):
        return self.curso


class Examen_Final(Evaluacion):
    duracion_examen = models.IntegerField()   #IntegerField()
    numero_preguntas = models.IntegerField()   #IntegerField()
    puntaje_total = models.IntegerField()   #IntegerField()

    class Meta:
        verbose_name = 'Examen_Final'
        verbose_name_plural = 'Examenes_Finales'

    @property
    def Puntaje_pregunta(self):
         return  str(self.numero_preguntas/self.puntaje_total)

    def __str__(self):
        return str(self.numero_preguntas)


class Proyecto(Evaluacion):
    tema_proyecto = models.CharField(max_length=100)
    numero_grupos = models.IntegerField()

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.tema_proyecto

class OrderedProy(Proyecto):
    class Meta:
        ordering = [
            "tema_proyecto",
            ]
        proxy = True