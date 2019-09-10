from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    #path('register', register, name='register'),
    path('', auth_views.LoginView.as_view(), name='login')
]
