<<<<<<< HEAD
from django.db.models import fields
from reciclApp.models.solicitud import Solicitud
from reciclApp.models.solicitud import Solicitud
from rest_framework import serializers


class SolicitudSerializer (serializers.ModelSerializer):
    class Meta:
        model= Solicitud
        fields= '_all_'
=======
from reciclApp.models.solicitud import Solicitud
from rest_framework             import serializers

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ['id', 'estado', 'fecha', 'reciclador','usuario', 'centro_de_acopio']
>>>>>>> a8d9f05544a6cb6516e7ce84553a8297e318e70d
