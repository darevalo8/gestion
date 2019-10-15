from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from dashboard.models import Cliente
from users.models import ClienteUser
from .serializers import ClienteSerializer, UserSerializer


class ClienteList(APIView):
    permission_classes = (IsAuthenticated,)

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


