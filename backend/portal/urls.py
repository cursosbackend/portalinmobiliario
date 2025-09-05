from django.urls import path
from .views import (
    HomeInmuebleListView,
    register_view, login_view, logout_view,
    PerfilView, PerfilEditView,
    SolicitudArriendoCreateView,
    solicitud_aceptar, 
    solicitud_rechazar
)
from .views_inmuebles_perfil import (
    PerfilInmuebleListView, PerfilInmuebleCreateView,
    PerfilInmuebleUpdateView, PerfilInmuebleDeleteView,
)

urlpatterns = [
    path("", HomeInmuebleListView.as_view(), name="home"),

    # auth
    path("accounts/register/", register_view, name="register"),
    path("accounts/login/",    login_view,    name="login"),
    path("accounts/logout/",   logout_view,   name="logout"),

    # perfil
    path("perfil/", PerfilView.as_view(), name="perfil"),
    path("perfil/editar/", PerfilEditView.as_view(), name="perfil_editar"),

    # CRUD inmuebles dentro del perfil (arrendador)
    path("perfil/inmuebles/",                 PerfilInmuebleListView.as_view(),  name="perfil_inmueble_list"),
    path("perfil/inmuebles/nuevo/",           PerfilInmuebleCreateView.as_view(), name="perfil_inmueble_create"),
    path("perfil/inmuebles/<int:pk>/editar/", PerfilInmuebleUpdateView.as_view(), name="perfil_inmueble_update"),
    path("perfil/inmuebles/<int:pk>/borrar/", PerfilInmuebleDeleteView.as_view(), name="perfil_inmueble_delete"),

    # solicitudes
    path("solicitudes/nueva/<int:inmueble_pk>/", SolicitudArriendoCreateView.as_view(), name="solicitud_create_for_inmueble"),

    # solicitudes
    path("solicitudes/<int:pk>/aceptar/",  solicitud_aceptar,  name="solicitud_aceptar"),
    path("solicitudes/<int:pk>/rechazar/", solicitud_rechazar, name="solicitud_rechazar"),
]
