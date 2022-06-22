from django.urls import path
from rest_cliente.views import getAllClientes, getClienteById

urlpatterns = [
    path('', getAllClientes, name='getAllClientes'),
    path('<id>', getClienteById, name='getClienteById'),
]
