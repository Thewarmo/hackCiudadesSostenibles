
from rest_framework import status
from rest_framework.response import Response
from django.db.models.query import QuerySet
from rest_framework                      import request, status, views, generics
from reciclApp.models.reciclador import Reciclador 
from reciclApp.serializers.recicladorSerializer import RecicladorSerializer, RecicladorUsuarioSerializer


class ListarTodoRecicladorView (generics.ListAPIView):
    serializer_class = RecicladorUsuarioSerializer
    def get_queryset(self,*args,**kwargs):
        querySet = Reciclador.objects.all()
        return (querySet)

class ListarRecicladorZonaView (generics.ListAPIView):
    serializer_class = RecicladorUsuarioSerializer
    def get_queryset(self,*args,**kwargs):
        querySet = Reciclador.objects.filter(zona=self.kwargs['zona'])
        return (querySet)

class ListarRecicladorMaterialView (generics.ListAPIView):
    serializer_class = RecicladorUsuarioSerializer
    def get_queryset(self,*args,**kwargs):
        querySet = Reciclador.objects.filter(categoria=self.kwargs['categoria'])
        return (querySet)

