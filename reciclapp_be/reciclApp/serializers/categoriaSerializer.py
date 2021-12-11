from reciclApp.models.categoria import Categoria

from rest_framework             import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']