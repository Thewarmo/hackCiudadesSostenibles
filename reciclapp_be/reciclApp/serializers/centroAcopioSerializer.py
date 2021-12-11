<<<<<<< HEAD
from django.db.models import fields
from reciclApp.models.centro_acopio import CentroDeAcopio
from rest_framework import serializers

class CentroAcopioSerializer (serializers.ModelSerializer):
    class Meta:
        model = CentroDeAcopio
        fields = '_all_'
=======
from reciclApp.models.centro_acopio          import CentroDeAcopio

from reciclApp.models.usuario                import Usuario


from rest_framework             import serializers

class CentroAcopioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroDeAcopio
        fields = ['nombre', 'zona', 'direccion','telefono']


class CentroAcopioEncargadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CentroDeAcopio
        fields = ['nombre', 'zona', 'direccion','telefono', 'encargado']

    def to_representation(self, obj):
    
        centro = CentroDeAcopio.objects.get(id=obj.id)
        encargado = Usuario.objects.get(id=obj.encargado_id)
        return {

            'nombre': centro.nombre,
            'zona': centro.zona,
            'direccion':centro.direccion,
            'telefono': centro.telefono,
            'encargado': {
                'nombre': encargado.nombre,
                'telefono': encargado.telefono,
            }
        }
>>>>>>> a8d9f05544a6cb6516e7ce84553a8297e318e70d
