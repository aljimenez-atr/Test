from django.db import models

# Create your models here.

#Modelo para categoria

        
class arriendoCleta(models.Model):
    idbicicleta = models.AutoField(primary_key=True, verbose_name="id bicicleta")
    modelo = models.CharField(max_length=50,verbose_name="Modelo bicicleta")
    porte = models.CharField(max_length=30, verbose_name="porte bicicleta")
    aro = models.IntegerField(verbose_name="aro de rueda")



