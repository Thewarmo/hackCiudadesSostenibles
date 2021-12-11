from django.db import models

class Categoria(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("nombre_de_categoría",max_length=50, null=False)
