from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    return HttpResponse('Bienvenido {0}'.format(request.user.empresauser.nombre_empresa))

