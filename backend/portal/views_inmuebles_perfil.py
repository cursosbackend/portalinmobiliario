from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Inmueble
from .form import InmuebleForm

@method_decorator(login_required, name="dispatch")
class PerfilInmuebleListView(ListView):
    model = Inmueble
    template_name = "perfil/inmueble_list.html"
    context_object_name = "inmuebles"
    paginate_by = 10
    def get_queryset(self): return Inmueble.objects.filter(propietario=self.request.user).order_by("-creado")

class PerfilInmuebleCreateView(LoginRequiredMixin, CreateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = "perfil/inmueble_form.html"
    success_url = reverse_lazy("perfil_inmueble_list")

    def form_valid(self, form):
        # ✅ Asigna ANTES del super para que quede persistido
        form.instance.propietario = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class PerfilInmuebleUpdateView(UpdateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = "perfil/inmueble_form.html"
    success_url = reverse_lazy("perfil_inmueble_list")
    def get_queryset(self): return Inmueble.objects.filter(propietario=self.request.user)

@method_decorator(login_required, name="dispatch")
class PerfilInmuebleDeleteView(DeleteView):
    model = Inmueble
    template_name = "perfil/inmueble_confirm_delete.html"
    success_url = reverse_lazy("perfil_inmueble_list")
    def get_queryset(self): return Inmueble.objects.filter(propietario=self.request.user)
