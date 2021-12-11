from reciclApp.models.producto               import Producto
from reciclApp.models.usuario                import Usuario
from reciclApp.serializers.usuarioSerializer import Usuario
from rest_framework                          import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'estado', 'imagen','peso', 'direccion','origen', 'destino', 'disponible']
    
    def to_representation(self, obj):
        
        producto = Producto.objects.get(id=obj.id)
        origen   = Usuario.objects.get(id=obj.origen_id)
        
        try:     
            destino  = Usuario.objects.get(id=obj.destino_id)
        
            return {
                'id': producto.id,
                'nombre': producto.nombre,
                'estado': producto.estado,
                'imagen': producto.imagen,
                'peso': producto.peso,
                'direccion': producto.direccion,
                'disponible': producto.disponible,
                'origen': {
                    'nombre':origen.nombre,
                    'telefono': origen.telefono,
                },
                'destino': destino.username
            }
        except:
                   
            return {
                'id': producto.id,
                'nombre': producto.nombre,
                'estado': producto.estado,
                'imagen': producto.imagen,
                'peso': producto.peso,
                'direccion': producto.direccion,
                'disponible': producto.disponible,
                'origen': {
                    'nombre':origen.nombre,
                    'telefono': origen.telefono,
                },
                'destino': None
            }
