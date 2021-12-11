
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.db.models.query import QuerySet
from rest_framework                      import request, status, views, generics
from reciclApp.models.centro_acopio import CentroDeAcopio
from reciclApp.serializers import CentroAcopioSerializer, CentroAcopioEncargadoSerializer



class ListarTodoCentrosView (generics.ListAPIView):
    serializer_class = CentroAcopioEncargadoSerializer
    def get_queryset(self,*args,**kwargs):
        querySet = CentroDeAcopio.objects.all()
        return (querySet)

class ListarCentrosZonaView (generics.ListAPIView):
    serializer_class = CentroAcopioEncargadoSerializer
    def get_queryset(self,*args,**kwargs):
        querySet = CentroDeAcopio.objects.filter(zona=self.kwargs['zona'])
        return (querySet)

class ListarCentrosNombreView (generics.ListAPIView):
    serializer_class = CentroAcopioEncargadoSerializer
    def get_queryset(self,*args,**kwargs):
        querySet = CentroDeAcopio.objects.filter(nombre=self.kwargs['nombre'])
        return (querySet)

