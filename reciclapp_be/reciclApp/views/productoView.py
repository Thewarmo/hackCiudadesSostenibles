from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from rest_framework.serializers import Serializer
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
    
class ListarTodoProductoView (generics.ListAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self,*args,**kwargs):
        querySet = Producto.objects.all()
        return (querySet)

class ModificarProductoView (generics.UpdateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class ListarProductosNombreView (generics.ListAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self,*args,**kwargs):
        querySet = Producto.objects.filter(nombre__icontains=self.kwargs['nombre'])
        return (querySet)

class ListarProductosOrigenView (generics.ListAPIView):
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all()
    def get_queryset(self,*args,**kwargs):
        token = self.request.META.get ('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['usuario_id'] != self.kwargs ['usuario']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        querySet = Producto.objects.filter(origen=self.kwargs['origen'])
        return (querySet)


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