# Generated by Django 4.0.4 on 2022-07-02 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionTrabajosApp', '0007_trabajado_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajado',
            name='day',
            field=models.IntegerField(default=2),
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.CharField(default='2', max_length=10)),
                ('weekday', models.CharField(default='sábado', max_length=10)),
                ('mes', models.CharField(default='7', max_length=15)),
                ('year', models.CharField(default='2022', max_length=15)),
                ('monto', models.IntegerField()),
                ('total', models.IntegerField()),
                ('Servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionTrabajosApp.servicio')),
            ],
            options={
                'verbose_name': 'Salida',
                'verbose_name_plural': 'Salidas',
            },
        ),
    ]