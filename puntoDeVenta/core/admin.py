from django.contrib import admin
from core.models import Cliente, Producto, DetalleVenta, Venta, MedioPago
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(DetalleVenta)
admin.site.register(Venta)
admin.site.register(MedioPago)
