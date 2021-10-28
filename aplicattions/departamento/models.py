from django.db import models

# Create your models here.

class departamento(models.Model):
    name = models.CharField('Nombre Departamento', max_length=50, unique=True)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)
    
    class Meta:
        verbose_name = "Mi Departamento"
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['id']
        unique_together = ('name', 'short_name')

    def __str__(self):
        return str(self.id) + " " + self.name