
from rest_framework                               import serializers
from reciclApp.models.usuario                     import Usuario
from reciclApp.models.centro_acopio               import CentroDeAcopio
from reciclApp.models.reciclador                  import Reciclador
from reciclApp.models.categoria                   import Categoria
from reciclApp.serializers.centroAcopioSerializer import CentroAcopioSerializer
from reciclApp.serializers.recicladorSerializer   import RecicladorSerializer
from reciclApp.serializers.categoriaSerializer    import CategoriaSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'nombre', 'correo', 'identificacion', 'telefono']
        
        
class UsuarioCentroSerializer(serializers.ModelSerializer):
    centro = CentroAcopioSerializer()
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'nombre', 'correo', 'identificacion', 'telefono', 'centro']
        
    def create(self, validated_data):

        centroData = validated_data.pop('centro')
        usuarioInstance = Usuario.objects.create(**validated_data)
        CentroDeAcopio.objects.create(encargado=usuarioInstance, **centroData)
        return usuarioInstance
    
    def to_representation(self, obj):

        usuario = Usuario.objects.get(id=obj.id)
        centro = CentroDeAcopio.objects.get(encargado=obj.id)
        return {
            'id': usuario.id,
            'username': usuario.username,
            'nombre': usuario.nombre,
            'correo': usuario.correo,
            'identificacion':usuario.identificacion,
            'telefono': usuario.telefono,
            'centro_acopio': {
                'id': centro.id,
                'nombre': centro.nombre,
                'zona': centro.zona,
                'direccion': centro.direccion,
                'telefono': centro.telefono,
            }
        }

class UsuarioRecicladorSerializer(serializers.ModelSerializer):
    reciclador = RecicladorSerializer()
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'nombre', 'correo', 'identificacion', 'telefono', 'reciclador']
        
    def create(self, validated_data):

        recicladorData = validated_data.pop('reciclador')
        usuarioInstance = Usuario.objects.create(**validated_data)
        Reciclador.objects.create(usuario=usuarioInstance, **recicladorData)
        return usuarioInstance
    
    def to_representation(self, obj):

        usuario = Usuario.objects.get(id=obj.id)
        reciclador = Reciclador.objects.get(usuario=obj.id)
        categoria= Categoria.objects.get(reciclador.categoria)
        return {
            'id': usuario.id,
            'username': usuario.username,
            'nombre': usuario.nombre,
            'correo': usuario.correo,
            'identificacion':usuario.identificacion,
            'telefono': usuario.telefono,
            'reciclador': {
                'id': reciclador.id,
                'zona': reciclador.zona,
                'categoria': categoria.name,
            }
        }

