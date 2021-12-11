from reciclApp.models.reciclador import Reciclador
from reciclApp.models.reciclador import Reciclador
from rest_framework import serializers

class RecicladorSerializer (serializers.ModelSerializer):
    class Meta:
        models= '_all_'