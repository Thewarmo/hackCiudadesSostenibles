from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from reciclApp.models.solicitud import Solicitud 
from reciclApp.serializers.solicitudSerializer import SolicitudSerializer


class CrearSolicitudView(APIView):
    
    def post(self, request, *args, **kwargs):
        
        serializer = SolicitudSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response("Solicitud Creada", status=status.HTTP_201_CREATED)

class ModificarSolicitudView (generics.UpdateAPIView):
    serializer_class = SolicitudSerializer
    queryset = Solicitud.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)