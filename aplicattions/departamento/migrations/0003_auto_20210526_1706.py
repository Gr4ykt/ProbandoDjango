# Generated by Django 3.2.2 on 2021-05-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_auto_20210526_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre Departamento'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(max_length=20, verbose_name='Nombre Corto'),
        ),
    ]
