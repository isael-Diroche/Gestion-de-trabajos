# Generated by Django 4.0.4 on 2022-07-01 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionTrabajosApp', '0006_alter_trabajado_day_alter_trabajado_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajado',
            name='comment',
            field=models.CharField(default='Sin comentario', max_length=100),
        ),
    ]
