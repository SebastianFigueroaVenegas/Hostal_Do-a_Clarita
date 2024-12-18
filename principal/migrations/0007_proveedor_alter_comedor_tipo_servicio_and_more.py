# Generated by Django 5.1 on 2024-11-30 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_comedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('rut_proveedor', models.CharField(max_length=12, unique=True)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('rubro', models.CharField(choices=[('Carniceria', 'Carniceria'), ('Verduleria', 'Verduleria'), ('Pescaderia', 'Pescaderia'), ('Tecnologia', 'Tecnologia'), ('Ferreteria', 'Ferreteria'), ('Articulos de Aseo', 'Articulos de Aseo')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='comedor',
            name='tipo_servicio',
            field=models.CharField(choices=[('Ejecutivo', 'Ejecutivo'), ('Especial', 'Especial'), ('General', 'General')], max_length=50),
        ),
        migrations.AlterField(
            model_name='habitacion',
            name='tipo_cama',
            field=models.CharField(choices=[('King', 'King'), ('Queen', 'Queen'), ('2 plazas', '2 plazas'), ('1 plaza', '1 plaza')], max_length=50),
        ),
    ]
