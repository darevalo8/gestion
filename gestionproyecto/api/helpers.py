from users.models import ClienteUser, InversionistaUser, EmpresaUser


def tipo_empresa(user):
    user_empresa = {}
    try:
        empresa_object = EmpresaUser.objects.get(user=user)
        user_empresa['usuario'] = empresa_object.user.username
        user_empresa['tipo_usuario'] = '1'
        return user_empresa
    except EmpresaUser.DoesNotExist:
        return None


def tipo_cliente(user):
    user_cliente = {}
    try:
        cliente_object = ClienteUser.objects.get(user=user)
        user_cliente['usuario'] = cliente_object.user.username
        user_cliente['tipo_usuario'] = '2'
        return user_cliente
    except ClienteUser.DoesNotExist:
        return None


def tipo_inversionista(user):
    user_inversionista = {}
    try:
        inversio_object = InversionistaUser.objects.get(user=user)
        user_inversionista['usuario'] = inversio_object.user.username
        user_inversionista['tipo_usuario'] = '3'
        return user_inversionista
    except InversionistaUser.DoesNotExist:
        return None


