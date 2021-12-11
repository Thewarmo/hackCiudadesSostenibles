from django.db import models
from .usuario  import Usuario

class CentroDeAcopio(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre    = models.CharField("Nombre_del_centro_de_acopio",max_length=50, null=False)
    zona      = models.CharField('Zona', max_length = 50, null=False)
    direccion = models.CharField('Direccion', max_length = 50, null=False)
    telefono  = models.CharField('Encargado', max_length = 50, null=False)
    encargado = models.ForeignKey(Usuario, related_name='encargado', null=False)