from django.urls import path
from .views import index, CrearCliente
app_name = 'dashboard'
urlpatterns = [
    #path('register', register, name='register'),
    path('', index, name='inicio'),
    path('cliente-add/', CrearCliente.as_view(), name='cliente_add')
]
