from reciclApp.models.centro_acopio import CentroDeAcopio

from rest_framework             import serializers

class CentroAcopioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroDeAcopio
        fields = ['id', 'nombre', 'zona', 'dirección','telefono', 'encargado']