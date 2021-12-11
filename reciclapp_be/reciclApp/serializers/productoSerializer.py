from django.db.models import fields
from reciclApp.models.producto import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields= '_all_'