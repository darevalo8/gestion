from django.contrib import admin
from .models import (EmpresaUser,
                     ClienteUser,
                     InversionistaUser)
admin.site.register(EmpresaUser)
admin.site.register(ClienteUser)
admin.site.register(InversionistaUser)
