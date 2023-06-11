from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=20, default ="Python")
    camada = models.IntegerField(default = "00000")
    
    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(default ="")
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(default ="")
    profesion = models.CharField(max_length=40)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"

    
class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField(default ="")
    entregado = models.BooleanField(default = False)