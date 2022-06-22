from multiprocessing.connection import Client
from operator import mod
from os import PRIO_USER
from platform import mac_ver
from xml.dom.minidom import Identified
from django.db import models

# Create your models here.

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, verbose_name='Identificador del Cliente')
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre del cliente')
    apellido = models.CharField(max_length=150, null=False, verbose_name='Apellido del cliente')
    correo = models.CharField(max_length=200, null=False, verbose_name='Correo del cliente')
    direccion = models.CharField(max_length=200, verbose_name='Direccion del cliente')
    
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Identificador del producto')
    nombre = models.CharField(max_length=100, null=False, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=250, verbose_name='Descipcion del producto')
    precio = models.IntegerField(null=False, verbose_name='Precio del producto')

class MedioPago(models.Model):
    idMedioPago = models.IntegerField(primary_key=True, verbose_name='Identificador del medio de pago')
    nombre = models.CharField(max_length=25, null=False, verbose_name='Nombre del medio de pago')

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True, verbose_name='Id Venta')
    monto = models.IntegerField(null=False, verbose_name='Monto Venta')
    medioPago = models.ForeignKey(MedioPago, verbose_name='Medio Pago Venta', null=False, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=10, null=False, verbose_name='Fecha de la venta')
    cliente = models.ForeignKey(Cliente, verbose_name='Identificador del Cliente', on_delete=models.CASCADE)
    
class DetalleVenta(models.Model):
    idDetalleVenta = models.IntegerField(primary_key=True, verbose_name='Identificador del detalle de venta')
    producto = models.ForeignKey(Producto, verbose_name='Identificador del producto', on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, verbose_name='Identificador de la venta', on_delete=models.CASCADE)