from reciclApp.models.reciclador import Reciclador
<<<<<<< HEAD
from reciclApp.models.reciclador import Reciclador
from rest_framework import serializers

class RecicladorSerializer (serializers.ModelSerializer):
    class Meta:
        models= '_all_'
=======
from reciclApp.models.usuario    import Usuario
from reciclApp.models.categoria  import Categoria


from rest_framework             import serializers

class RecicladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciclador
        fields = ['zona', 'categoria']

class RecicladorUsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reciclador
        fields = ['zona', 'categoria', 'usuario']

    def to_representation(self, obj):
    
        reciclador = Reciclador.objects.get(id=obj.id)
        usuario    = Usuario.objects.get(id=obj.usuario_id)
        categoria  = Categoria.objects.get(id=obj.categoria_id)
        return {
            'nombre': usuario.nombre,
            'telefono': usuario.telefono,            
            'zona': reciclador.zona,
            'categoria':categoria.nombre,

        }
>>>>>>> a8d9f05544a6cb6516e7ce84553a8297e318e70d
