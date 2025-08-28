from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    pass

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    pass

@admin.register(SolicitudArriendo)
class SolicitudArriendoAdmin(admin.ModelAdmin):
    pass


@admin.register(PerfilUser)
class PerfilUserAdmin(admin.ModelAdmin):
    pass