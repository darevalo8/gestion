from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import ClienteForm, UserForm
from users.models import ClienteUser

@login_required()
def index(request):
    nombre = request.user.username
    print(request.user.has_perm('users.add_empresauser'))
    return render(request, 'dashboard/dashboard.html', {'nombre': nombre})


class CrearCliente(LoginRequiredMixin, View):

    def get(self, request):
        form_cliente = ClienteForm()
        form_user = UserForm()
        context = {'form_user': form_user, 'form_cli': form_cliente}
        return render(request, 'dashboard/cliente_form.html', context)

    @staticmethod
    def post(request):
        form_cliente = ClienteForm(request.POST)
        form_user = UserForm(request.POST)
        if form_cliente.is_valid() and form_user.is_valid():
            cliente = form_cliente.save()
            user = form_user.save(commit=False)
            user.set_password(user.password)
            user.save()
            ClienteUser.objects.create(user=user, cliente=cliente)
            return redirect('dashboard:inicio')

