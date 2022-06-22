import email
from xmlrpc.client import boolean
from core.models import Cliente
from .serializers import ClienteSerializer

def verifyEmail(email):
    cliente = Cliente.objects.filter(correo=email)
    if cliente.count() > 0:
        return False
    return True