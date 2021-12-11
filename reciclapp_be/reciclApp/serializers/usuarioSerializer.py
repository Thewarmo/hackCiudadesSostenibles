from django.db.models import fields
from reciclApp.models.usuario import Usuario
from rest_framework import serializers


class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields='_all_'