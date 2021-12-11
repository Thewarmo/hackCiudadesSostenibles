from django.contrib.auth.hashers import UNUSABLE_PASSWORD_SUFFIX_LENGTH
from django.db      import models
from .usuario       import Usuario
from .reciclador    import Reciclador
from .centro_acopio import CentroDeAcopio

class Solicitud(models.Model):
    
    id = models.AutoField(primary_key=True)
    estado     = models.CharField('Estado', max_length = 50, null=False)
    fecha      = models.DateTimeField('Fecha', max_length = 50, auto_now_add=True)
    reciclador = models.ForeignKey (Reciclador, related_name='reciclador_solicitud', null=False, on_delete=models.CASCADE)
    usuario    = models.ForeignKey(Usuario, related_name='usuario_solicitud', null=False, on_delete=models.CASCADE)
    centro_de_acopio = models.ForeignKey(CentroDeAcopio, related_name='centro_acopio_solicitud', null=True, on_delete=models.CASCADE)