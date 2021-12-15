from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título') 
    description = models.TextField(verbose_name='Descripción') 
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') #Se creará la fecha automáticamente  
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición') #Se actualiza cada vez que se ejecuta una instancia 

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'

    def __str__(self):
        return self.title 

    