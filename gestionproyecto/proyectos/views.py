from django.shortcuts import render, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (View, ListView, DetailView,
                                  UpdateView, DeleteView, CreateView)
from django.urls import reverse_lazy
from .models import Proyecto, FaseProyecto
from .forms import ProyectoForm, FaseProyectoForm


class ProyectoList(LoginRequiredMixin, ListView):
    model = Proyecto
    context_object_name = 'objects'
    template_name = 'proyectos/proyecto_list.html'


class CrearProyectoView(LoginRequiredMixin, CreateView):
    form_class = ProyectoForm
    model = Proyecto
    success_url = reverse_lazy('proyecto:proyecto_list')


class ProyectoDetalle(LoginRequiredMixin, View):
    # model = Proyecto
    # context_object_name = 'objects'
    # template_name = 'proyectos/proyecto_list.html'
    def get_object(self, pk):
        try:
            return Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        context = {}
        proyecto = self.get_object(pk)
        context['proyecto'] = proyecto
        fases = FaseProyecto.objects.filter(proyecto=proyecto)
        context['fases'] = fases
        return render(request, 'proyectos/proyecto_detalle.html', context)


class ProyectoUpdate(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm

class ProyectoDelete(LoginRequiredMixin, DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyecto:proyecto_list')
    template_name = 'proyectos/object_confirm_delete.html'


class FaseProyectoAdd(LoginRequiredMixin, CreateView):
    model = FaseProyecto
    form_class = FaseProyectoForm
    success_url = reverse_lazy('proyecto:proyecto_list')


class FaseProyectoDetail(LoginRequiredMixin, DetailView):
    model = FaseProyecto
    context_object_name = 'objects'
    template_name = 'proyectos/fase_detalle.html'


class FaseProyectoUpdate(LoginRequiredMixin, UpdateView):
    model = FaseProyecto
    form_class = FaseProyectoForm


class FaseProyectoDelete(LoginRequiredMixin, DeleteView):
    model = FaseProyecto
    success_url = reverse_lazy('proyecto:proyecto_list')
    template_name = 'proyectos/object_confirm_delete.html'


