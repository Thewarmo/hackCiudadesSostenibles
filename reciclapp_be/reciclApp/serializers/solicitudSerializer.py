from django.db.models import fields
from reciclApp.models.solicitud import Solicitud
from reciclApp.models.solicitud import Solicitud
from rest_framework import serializers


class SolicitudSerializer (serializers.ModelSerializer):
    class Meta:
        model= Solicitud
        fields= '_all_'