from django.urls import path
from .views import (index,
                    CrearCliente,
                    CrearInversionista,
                    InversionistaList,
                    ClienteList)
app_name = 'dashboard'
urlpatterns = [
    #path('register', register, name='register'),
    path('', index, name='inicio'),
    path('cliente-add/', CrearCliente.as_view(), name='cliente_add'),
    path('cliente-list', ClienteList.as_view(), name='cliente_list'),
    path('inversionista-add', CrearInversionista.as_view(), name='inver_add'),
    path('inversionista-list', InversionistaList.as_view(), name='inver_list'),
]
