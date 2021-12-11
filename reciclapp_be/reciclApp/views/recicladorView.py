from rest_framework.views import APIView
from rest_framework.decorators import api_view
from reciclApp.models import reciclador 
from reciclApp.serializers import recicladorSerializer

@api_view(['GET','POST'])
def recolector_api_view(request):
    if request.method == 'GET':
        recolector = reciclador.objects.all()
        reciclador_serializer = recicladorSerializer(recolector,many=True)
        return Response(reciclador_serializer.data)

    elif request.method == 'POST':
        reciclador_serializer = recicladorSerializer(data = request.data)
        if reciclador_serializer.is_valid():
            reciclador_serializer.save()
            return Response(reciclador_serializer.data)
        return Response(reciclador_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def recolector_detail_view(request,pk=None):
    try:
        recolector = reciclador.objects.get(pk=pk)
    except reciclador.DoesNotExist:
         return Response('Cliente no encontrado',status=status.HTTP_404_NOT_FOUND)   

    if request.method =='GET':
        reciclador_serializer = recicladorSerializer(recolector)
        return Response(reciclador_serializer.data)
           

    elif request.method == 'PUT':
        reciclador_serializer = recicladorSerializer(recolector,data = request.data)
        if reciclador_serializer.is_valid():
            reciclador_serializer.save()
            return Response(reciclador_serializer.data)
        return Response(reciclador_serializer.errors)

    elif request.method == 'DELETE':
        recolector.delete()
        return Response('Eliminando Recolector...')