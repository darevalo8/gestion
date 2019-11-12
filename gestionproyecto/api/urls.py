from django.urls import path
from .views import ClienteList, InversionistaList
app_name = 'api'
urlpatterns = [
    path('clientes', ClienteList.as_view()),
    path('inversionistas', InversionistaList.as_view()),
]
