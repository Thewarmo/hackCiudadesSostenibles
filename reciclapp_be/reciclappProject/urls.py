"""reciclappProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from reciclApp.views.usuarioView   import CrearCentroAcopioView,CrearRecicladorView,CrearUsuarioView
from reciclApp.views.centroAcopiView import ListarTodoCentrosView, ListarCentrosZonaView, ListarCentrosNombreView
from reciclApp.views.recicladorView  import ListarTodoRecicladorView, ListarRecicladorMaterialView, ListarRecicladorZonaView
from reciclApp.views.productoView    import CrearProductoView, ListarTodoProductoView, ModificarProductoView, ListarProductosNombreView, ListarProductosOrigenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('signup/usuario/', CrearUsuarioView.as_view()),
    path('signup/reciclador/', CrearRecicladorView.as_view()),
    path('signup/centroacopio/', CrearCentroAcopioView.as_view()),
    path('centroacopio/list', ListarTodoCentrosView.as_view()),
    path('centroacopio/zona/<str:zona>', ListarCentrosZonaView.as_view()),
    path('centroacopio/nombre/<str:nombre>', ListarCentrosNombreView.as_view()),
    path('reciclador/list', ListarTodoRecicladorView.as_view()),
    path('reciclador/zona/<str:zona>', ListarRecicladorZonaView.as_view()),
    path('reciclador/categoria/<int:categoria>', ListarRecicladorMaterialView.as_view()),
    path('producto/', CrearProductoView.as_view()),
    path('producto/list', ListarTodoProductoView.as_view()),
    path('producto/update/<int:pk>', ModificarProductoView.as_view()),
    path('producto/nombre/<str:nombre>', ListarProductosNombreView.as_view()),
    path('producto/origen/<int:origen>', ListarProductosOrigenView.as_view())
]
