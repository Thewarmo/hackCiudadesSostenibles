from reciclApp.models.solicitud import Solicitud
from rest_framework             import serializers

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id', 'estado', 'fecha', 'reciclador','usuario', 'centro_de_acopio']