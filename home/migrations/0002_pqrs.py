# Generated by Django 4.2.6 on 2024-02-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pqrs',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('tipoPqrs', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=50)),
            ],
        ),
    ]