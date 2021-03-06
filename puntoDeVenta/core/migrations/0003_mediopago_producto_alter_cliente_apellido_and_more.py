# Generated by Django 4.0.5 on 2022-06-19 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cliente_idcliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedioPago',
            fields=[
                ('idMedioPago', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificador del medio de pago')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre del medio de pago')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificador del producto')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descipcion del producto')),
                ('precio', models.IntegerField(verbose_name='Precio del producto')),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=150, verbose_name='Apellido del cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.CharField(max_length=200, verbose_name='Correo del cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=200, verbose_name='Direccion del cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idCliente',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre del cliente'),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Venta')),
                ('monto', models.IntegerField(verbose_name='Monto Venta')),
                ('fecha', models.CharField(max_length=10, verbose_name='Fecha de la venta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente', verbose_name='Identificador del Cliente')),
                ('medioPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mediopago', verbose_name='Medio Pago Venta')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('idDetalleVenta', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificador del detalle de venta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto', verbose_name='Identificador del producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta', verbose_name='Identificador de la venta')),
            ],
        ),
    ]
