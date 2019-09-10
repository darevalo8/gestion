from django.urls import path
from .views import index
app_name = 'dashboard'
urlpatterns = [
    #path('register', register, name='register'),
    path('', index, name='inicio')
]
