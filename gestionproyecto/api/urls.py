from django.urls import path
from .views import ClienteList
app_name = 'api'
urlpatterns = [
    path('clientes', ClienteList.as_view()),
]
