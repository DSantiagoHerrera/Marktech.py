# Generated by Django 5.0.2 on 2024-03-14 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('producto_id', models.IntegerField()),
                ('venta_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pqrs',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('tipoPqrs', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=1000)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.PositiveSmallIntegerField()),
                ('stock', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_codigo', models.CharField(max_length=50)),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('total_venta', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.venta')),
            ],
        ),
        migrations.AddField(
            model_name='venta',
            name='productos',
            field=models.ManyToManyField(through='home.VentaProducto', to='home.producto'),
        ),
    ]
