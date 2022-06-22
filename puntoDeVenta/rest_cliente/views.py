from curses.ascii import HT
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Cliente
from .serializers import ClienteSerializer
from .utils import verifyEmail

@csrf_exempt
@api_view(['GET', 'POST'])
def getAllClientes(request: HttpRequest):
    if request.method == 'GET':
        cliente = Cliente.objects.all();
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    else:
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            if verifyEmail(serializer.validated_data.get('correo')):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(data={"message": "Correo existente"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def getClienteById(request: HttpRequest, id):
    try:
        cliente = Cliente.objects.get(idCliente=id);
    except Cliente.DoesNotExist:
        return Response({'message': 'Id cliente no existe', 'error': True} ,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ClienteSerializer(cliente, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(cliente,data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)