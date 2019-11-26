from django import forms
from .models import Proyecto, FaseProyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre_proyecto', 'fecha_inicio',
                  'fecha_fin', 'cliente', 'descripcion')


class FaseProyectoForm(forms.ModelForm):
    class Meta:
        model = FaseProyecto
        fields = (
            'nombre_fase',
            'fecha_inicio',
            'fecha_fin',
            'descripcion',
            'proyecto'
        )
