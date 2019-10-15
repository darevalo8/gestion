from django.contrib import admin
from .models import (Empresa,
                     Cliente,
                     Inversionista)
# Register your models here.
admin.site.register(Empresa)
admin.site.register(Cliente)
admin.site.register(Inversionista)
