from django.db import models

# Create your models here.

class Editorial(models.Model):
    CodEditorial=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=15)

    def __str__(self):
        self.Nombre


        
class Libros(models.Model):
    Codigo_Libro=models.AutoField(primary_key=True)
    Titulo=models.TextField(max_length=15)
    Cantidad=models.IntegerField()
    Precio=models.FloatField()
    CodEditorial=models.IntegerField()

    def __str__(self):
        self.Titulo

