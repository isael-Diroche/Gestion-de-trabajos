# Generated by Django 4.0.4 on 2022-07-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionTrabajosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]