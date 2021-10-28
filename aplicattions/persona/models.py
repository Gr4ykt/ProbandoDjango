from django.db import models
from django.db.models.fields import CharField
from aplicattions.departamento.models import departamento

# Create your models here.

class habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    def __str__(self):
        return str(self.id) + " " + self.habilidad


class empleado(models.Model):
    job_choices = (
        ('0', 'Informatico'),
        ('1', 'Comunicaciones'),
        ('2', 'Contador'),
        ('3', 'Administrador')
    )

    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Apellido', max_length=50)
    avatar = models.ImageField(upload_to='media', blank=True, null=True)
    full_name = models.CharField(
        'nombre completo',
        max_length=120,
        blank=True
    )

    job = CharField('Trabajo', choices=job_choices, max_length=70)
    #FOREINGKEY
    Departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)

    #MANYTOMANYFIELD
    habilidad = models.ManyToManyField(habilidades)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados contratados'
        ordering = ['id', 'name']

    def __str__(self):
        return str(self.id) + " " + self.short_name + ' ' + self.name + ' ' + self.job