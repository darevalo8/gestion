from django.urls import path
from .views import ClienteList, InversionistaList, ProyectoView, TipoUsuario
app_name = 'api'
urlpatterns = [
    path('clientes', ClienteList.as_view()),
    path('clientes/<int:pk>/', ClienteList.as_view()),
    path('inversionistas', InversionistaList.as_view()),
    path('inversionistas/<int:pk>/', InversionistaList.as_view()),
    path('proyectos', ProyectoView.as_view()),
    path('me', TipoUsuario.as_view()),
]
