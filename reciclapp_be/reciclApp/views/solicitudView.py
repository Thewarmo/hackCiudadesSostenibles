from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from reciclApp.models import solicitud 
from reciclApp.serializers import solicitudSerializer

@api_view(['GET','POST'])
def producto_api_view(request):
    if request.method == 'GET':
        solic = solicitud.objects.all()
        solicitud_serializer = solicitudSerializer(solic,many=True)
        return Response(solicitud_serializer.data)

    elif request.method == 'POST':
        solicitud_serializer = solicitudSerializer(data = request.data)
        if solicitud_serializer.is_valid():
            solicitud_serializer.save()
            return Response(solicitud_serializer.data)
        return Response(solicitud_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def producto_detail_view(request,pk=None):
    try:
        solic = solicitud.objects.get(pk=pk)
    except solicitud.DoesNotExist:
         return Response('Cliente no encontrado',status=status.HTTP_404_NOT_FOUND)   

    if request.method =='GET':
        solicitud_serializer = solicitudSerializer(solic)
        return Response(solicitud_serializer.data)
           

    elif request.method == 'PUT':
        solicitud_serializer = solicitudSerializer(solic,data = request.data)
        if solicitud_serializer.is_valid():
            solicitud_serializer.save()
            return Response(solicitud_serializer.data)
        return Response(solicitud_serializer.errors)

    elif request.method == 'DELETE':
        solic.delete()
        return Response('Eliminando Recolector...')