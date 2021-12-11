from django.db.models import fields
from reciclApp.models.centro_acopio import CentroDeAcopio
from rest_framework import serializers

class CentroAcopioSerializer (serializers.ModelSerializer):
    class Meta:
        model = CentroDeAcopio
        fields = '_all_'
