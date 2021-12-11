from reciclApp.models.reciclador import Reciclador

from rest_framework             import serializers

class RecicladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciclador
        fields = ['id', 'zona', 'usuario', 'categoria']