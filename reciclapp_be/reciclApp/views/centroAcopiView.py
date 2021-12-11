from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from reciclApp.models import centro_acopio
from reciclApp.serializers import centroAcopioSerializer

@api_view(['GET','POST'])
def centro_api_view(request):
    if request.method == 'GET':
        centro = centro_acopio.objects.all()
        centro_serializer = centroAcopioSerializer(centro,many=True)
        return Response(centro_serializer.data)

    elif request.method == 'POST':
        centro_serializer = centroAcopioSerializer(data = request.data)
        if centro_serializer.is_valid():
            centro_serializer.save()
            return Response(centro_serializer.data)
        return Response(centro_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def centro_detail_view(request,pk=None):
    try:
        centro = centro_acopio.objects.get(pk=pk)
    except centro_acopio.DoesNotExist:
         return Response('Cliente no encontrado',status=status.HTTP_404_NOT_FOUND)   

    if request.method =='GET':
        centro_serializer = centroAcopioSerializer(centro)
        return Response(centro_serializer.data)
           

    elif request.method == 'PUT':
        centro_serializer = centroAcopioSerializer(centro,data = request.data)
        if centro_serializer.is_valid():
            centro_serializer.save()
            return Response(centro_serializer.data)
        return Response(centro_serializer.errors)

    elif request.method == 'DELETE':
        centro.delete()
        return Response('Eliminando Centro...')       