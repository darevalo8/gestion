from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from .forms import ClienteForm, UserForm, InversionistaForm
from .models import Inversionista, Cliente
from users.models import ClienteUser, InversionistaUser

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


class CrearInversionista(LoginRequiredMixin, View):

    def get(self, request):
        form_inversion = InversionistaForm()
        form_user = UserForm()
        context = {'form_user': form_user, 'form_inver': form_inversion}
        return render(request, 'dashboard/iversionista_form.html', context)

    @staticmethod
    def post(request):
        form_inversion = InversionistaForm(request.POST)
        form_user = UserForm(request.POST)
        if form_inversion.is_valid() and form_user.is_valid():
            inversionista = form_inversion.save()
            user = form_user.save(commit=False)
            user.set_password(user.password)
            user.save()
            InversionistaUser.objects.create(user=user, inversionista=inversionista)
            return redirect('dashboard:inicio')


class InversionistaList(LoginRequiredMixin, ListView):
    model = Inversionista
    template_name = 'dashboard/list_inver.html'
    context_object_name = 'objects'


class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'dashboard/list_cliente.html'
    context_object_name = 'objects'
