from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from reciclApp.models.producto import Producto 
from reciclApp.serializers.productoSerializer import ProductoSerializer



class CrearProductoView(APIView):
    
    def post(self, request, *args, **kwargs):
        
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response("Producto Creado", status=status.HTTP_201_CREATED)
    

@api_view(['GET','POST'])
def producto_api_view(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        producto_serializer = productoSerializer(producto,many=True)
        return Response(producto_serializer.data)

    elif request.method == 'POST':
        producto_serializer = productoSerializer(data = request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data)
        return Response(producto_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def producto_detail_view(request,pk=None):
    try:
        producto = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
         return Response('Cliente no encontrado',status=status.HTTP_404_NOT_FOUND)   

    if request.method =='GET':
        producto_serializer = productoSerializer(producto)
        return Response(producto_serializer.data)
           

    elif request.method == 'PUT':
        producto_serializer = productoSerializer(producto,data = request.data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data)
        return Response(producto_serializer.errors)

    elif request.method == 'DELETE':
        producto.delete()
        return Response('Eliminando Producto...')