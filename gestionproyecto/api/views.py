from django.shortcuts import render, Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from dashboard.models import Cliente, Inversionista
from users.models import ClienteUser, InversionistaUser
from proyectos.models import Proyecto
from .serializers import (ClienteSerializer,
                          UserSerializer,
                          InversionistaSerializer, ProyectoSerializer)


class ClienteList(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        print(request.user)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = {
            'nombre_cliente': request.data['nombre'],
            'nit_cliente' : request.data['nit'],
            'tel_cliente': request.data['telefono'],
            'direc_cliente': request.data['direccion']
        }
        data_user = {
            'username': request.data['username'],
            'password': request.data['password'],
            'email': request.data['email']
        }
        cliente_serializer = ClienteSerializer(data=data)
        user_serializer = UserSerializer(data=data_user)
        if cliente_serializer.is_valid() and user_serializer.is_valid():
            user = user_serializer.save()
            user.set_password(user.password)
            user.save()
            cliente = cliente_serializer.save()
            ClienteUser.objects.create(user=user, cliente=cliente)
            return Response(cliente_serializer.data, status=status.HTTP_201_CREATED)
        return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        data = {
            'nombre_cliente': request.data['nombre'],
            'nit_cliente': request.data['nit'],
            'tel_cliente': request.data['telefono'],
            'direc_cliente': request.data['direccion']
        }
        cliente_serializer = ClienteSerializer(cliente, data=data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InversionistaList(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Inversionista.objects.get(pk=pk)
        except Inversionista.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        inversionista = Inversionista.objects.all()
        serializer = InversionistaSerializer(inversionista, many=True)
        print(request.user)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = {
            'nombre': request.data['nombre'],
            'nit': request.data['nit'],
            'telefono': request.data['telefono'],
            'direccion': request.data['direccion'],
            'tipo_inver': request.data['tipo_inver']
        }
        data_user = {
            'username': request.data['username'],
            'password': request.data['password'],
            'email': request.data['email']
        }
        inversionista_seriali = InversionistaSerializer(data=data)
        user_serializer = UserSerializer(data=data_user)
        if inversionista_seriali.is_valid() and user_serializer.is_valid():
            user = user_serializer.save()
            user.set_password(user.password)
            user.save()
            inversionista = inversionista_seriali.save()
            InversionistaUser.objects.create(user=user, inversionista=inversionista)
            return Response(inversionista_seriali.data, status=status.HTTP_201_CREATED)
        return Response(inversionista_seriali.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        inversionista = self.get_object(pk)
        data = {
            'nombre': request.data['nombre'],
            'nit': request.data['nit'],
            'telefono': request.data['telefono'],
            'direccion': request.data['direccion'],
            'tipo_inver': request.data['tipo_inver']
        }
        serializer_inver = InversionistaSerializer(inversionista, data=data)
        if serializer_inver.is_valid():
            serializer_inver.save()
            return Response(serializer_inver.data)
        return Response(serializer_inver.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        inversionista = self.get_object(pk)
        inversionista.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProyectoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        proeyecto = Proyecto.objects.all()
        serializer = ProyectoSerializer(proeyecto, many=True)
        return Response(serializer.data)

