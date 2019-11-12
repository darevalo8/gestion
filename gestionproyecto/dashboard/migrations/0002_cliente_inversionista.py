# Generated by Django 2.2.4 on 2019-10-14 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('nit_cliente', models.CharField(max_length=50)),
                ('tel_cliente', models.CharField(max_length=11)),
                ('direc_cliente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inversionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
                ('tipo_inver', models.IntegerField(choices=[(1, 'Inversionista'), (2, 'Banco')], default=1)),
            ],
        ),
    ]