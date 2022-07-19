from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Roles(models.Model):
    nombre = models.CharField(max_length=15)

class Usuarios(AbstractUser):
    rol = models.ForeignKey(Roles, to_field='id', on_delete=models.CASCADE)
    nombres = models.CharField(max_length=40)
    paterno = models.CharField(max_length=20)
    materno = models.CharField(max_length=20)
    correo = models.CharField(max_length=40)
    password = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    username = 'None'

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = []

class Tecnologias(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=400)

class Clases(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=5000)
    tecnologia = models.ForeignKey(Tecnologias, to_field='id', on_delete=models.CASCADE)

class Ejercicios(models.Model):
    nombre = models.CharField(max_length=100)
    enunciado = models.CharField(max_length=5000)
    respuesta1 = models.CharField(max_length=50)
    respuesta2 = models.CharField(max_length=50, blank=True, null=True)
    tecnologia = models.ForeignKey(Tecnologias, to_field='id', on_delete=models.CASCADE)

class Usuario_Ejercicio(models.Model):
    usuario = models.ForeignKey(Usuarios, to_field='id', on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicios, to_field='id', on_delete=models.CASCADE)
    tiempo = models.IntegerField(null=True) 
    estado = models.IntegerField()
    respuesta = models.CharField(max_length=50, null=True)

class Usuario_Clase(models.Model):
    usuario = models.ForeignKey(Usuarios, to_field='id', on_delete=models.CASCADE)
    clase = models.ForeignKey(Clases, to_field='id', on_delete=models.CASCADE)
    estado = models.IntegerField()
    tiempo = models.IntegerField(null=True) 