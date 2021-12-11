from reciclApp.models.producto import Producto

from rest_framework             import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'estado', 'imagen','peso', 'direccion','origen', 'destino', 'disponible']