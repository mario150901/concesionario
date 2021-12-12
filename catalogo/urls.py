from django.urls import path
from catalogo.views import CochesListView, EliminarCoche, EliminarFabricante, FabricantesListView, ModificarCoche, ModificarFabricante, SearchResultsListView, \
    crear_coche, CrearFabricante ,\
    subir_archivo

urlpatterns = [
    path('', views.index, name='index'),
    path('coches/', CochesListView.as_view(), 
        name='listado_coches'),
    path('buscarcoches/', SearchResultsListView.as_view(),
        name="buscacoches" ),
    path('fabricantes/', FabricantesListView.as_view(), 
        name='listado_fabricantes'),
    path('coche/crear', crear_coche, name='crear_coche'),
    path('coche/modificar/<int:pk>', ModificarCoche.as_view(), name='modificar_coche'),
    path('coche/eliminar/<int:pk>', EliminarCoche.as_view(), name='eliminar_coche'),
    path('fabricante/crear', CrearFabricante.as_view(), name='crear_fabricante'),
    path('fabricante/modificar/<int:pk>', ModificarFabricante.as_view(), name='modificar_fabricante'),
    path('fabricante/eliminar/<int:pk>', EliminarFabricante.as_view(), name='eliminar_fabricante'),
    path('subir-archivo', subir_archivo, name='subir-archivo')
]