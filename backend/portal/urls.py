from django.urls import path 
from .views import *




urlpatterns = [
  path("listar_regiones/", regionListView.as_view(), name="region_list"),
  path("crear_region/", RegionCreateView.as_view(), name="region_create"),
  path("actualizar_region/<int:pk>/", RegionUpdateView.as_view(), name="actualizar_region"),
  path("borrar_region/<int:pk>/", RegionDelete.as_view(), name="borrar_region"),
  ###########################################################################################
  path("listar_comunas/", ComunaListView.as_view(), name="comuna_list"),
  path("crear_comuna/", ComunaCreateView.as_view(), name="comuna_create"),
  path("actualizar_comuna/<int:pk>", ComunaUpdateView.as_view(), name="comuna_update"),
  path("borrar_comuna/<int:pk>", ComunaDeleteView.as_view(), name="comuna_delete"),
  ###########################################################################################
  path("listar_inmuebles/", InmueblesListView.as_view(), name="inmueble_list"),
  path("crear_inmueble/", InmuebleCreateView.as_view(), name="inmueble_create"),
  path("actualizar_inmueble/<int:pk>", InmuebleUpdateView.as_view(), name="inmueble_update"),
  path("borrar_inmueble/<int:pk>", InmuebleDeleteView.as_view(), name="inmueble_delete"),
  ###########################################################################################
  path("listar_solicitudes/", SolicitudArriendoListView.as_view(), name="solicitud_list"),
  path("crear_solicitud/", SolicitudArriendoCreateView.as_view(), name="solicitud_create"),
  path("actualizar_solicitud/<int:pk>",SolicitudArriendoUpdateView.as_view(), name="solicitud_update"),
  path("borrar_solicitud/<int:pk>",SolicitudArriendoDeleteView.as_view(), name="solicitud_delete"),
  ###########################################################################################
  path("actualizar_perfil/<int:pk>",PerfilUserUpdateView.as_view(), name="perfil_update"),
]