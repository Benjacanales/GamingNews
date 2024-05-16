from django.db import models

# Create your models here.
class Genero(models.Model):
    descripcion = models.CharField(max_length=10)

    def __str__(self): 
        return self.descripcion
    
class TipoUsuario(models.Model):
    descripcion = models.CharField(max_length=20)
    
    def __str__(self): 
        return self.descripcion

class Usuario(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField(default=0)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self): 
        return self.rut