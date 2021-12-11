from django.db import models
from .usuario import Usuario

class Producto(models.Model):
    
    id         = models.AutoField(primary_key=True)
    estado     = models.CharField("estado",max_length=20, null=False)
    nombre     = models.CharField("nombre de categoría",max_length=50, null=False)
    imagen     = models.CharField ("URL_imagen", max_length=300, null=False)
    peso       = models.IntegerField("peso", default=0, null=False)
    direccion  = models.CharField ("direccion", max_length=50, null=False)
    origen     = models.ForeignKey(Usuario, related_name="origen_producto", on_delete=models.CASCADE, null=False)
    destino    = models.ForeignKey(Usuario, related_name="destino_producto", on_delete=models.CASCADE, null=True)
    disponible = models.BooleanField (default=True)
    