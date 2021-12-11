from django.db  import models
from .usuario   import Usuario
from .categoria import Categoria

class Reciclador(models.Model):
    
    id = models.AutoField(primary_key=True)
    zona      = models.CharField('Zona', max_length = 50, null=False)
    usuario   = models.ForeignKey(Usuario, related_name='reciclador', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name="reciclador_categoria", on_delete=models.CASCADE, null=False)