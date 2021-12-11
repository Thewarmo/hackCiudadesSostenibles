<<<<<<< HEAD
from django.db.models import fields
from reciclApp.models.producto import Producto
from rest_framework import serializers

=======
from reciclApp.models.producto               import Producto
from reciclApp.models.usuario                import Usuario
from reciclApp.serializers.usuarioSerializer import Usuario
from rest_framework                          import serializers
>>>>>>> a8d9f05544a6cb6516e7ce84553a8297e318e70d

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
<<<<<<< HEAD
        fields= '_all_'
=======
        fields = ['id', 'nombre', 'estado', 'imagen','peso', 'direccion','origen', 'destino', 'disponible']
    
    def to_representation(self, obj):
        
        producto = Producto.objects.get(id=obj.id)
        origen   = Usuario.objects.get(id=obj.origen)
        destino  = Usuario.objects.get(id=obj.destino)
        
        return {
            'id': producto.id,
            'nombre': producto.nombre,
            'estado': producto.estado,
            'imagen': producto.imagen,
            'peso': producto.peso,
            'direccion': producto.direccion,
            'disponible': producto.disponible,
            'origen': {
                'nomrbe':origen.nombre,
                'telefono': origen.telefono,
            },
            'destino': destino.username
        }

>>>>>>> a8d9f05544a6cb6516e7ce84553a8297e318e70d
