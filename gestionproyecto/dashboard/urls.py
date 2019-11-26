from django.urls import path
from .views import (index,
                    CrearCliente,
                    CrearInversionista,
                    InversionistaList,
                    ClienteList, ClienteDetail,
                    InversionistaDetail, InversionistaUpdate,
                    ClienteUpdate, InversionistaDelete,
                    ClienteDelete)
app_name = 'dashboard'
urlpatterns = [
    #path('register', register, name='register'),
    path('', index, name='inicio'),
    path('cliente-add/', CrearCliente.as_view(), name='cliente_add'),
    path('cliente-list', ClienteList.as_view(), name='cliente_list'),
    path('cliente/<int:pk>/', ClienteDetail.as_view(), name='cliente_detail'),
    path('edit/cliente/<int:pk>/', ClienteUpdate.as_view(), name='cliente_update'),
    path('delete/cliente/<int:pk>/', ClienteDelete.as_view(), name='cliente_delete'),
    path('inversionista-add', CrearInversionista.as_view(), name='inver_add'),
    path('inversionista-list', InversionistaList.as_view(), name='inver_list'),
    path('inver/<int:pk>/', InversionistaDetail.as_view(), name='inver_detail'),
    path('delete/inver/<int:pk>/', InversionistaDelete.as_view(), name='inver_delete'),
    path('edit/inver/<int:pk>/', InversionistaUpdate.as_view(), name='inver_update'),
]
