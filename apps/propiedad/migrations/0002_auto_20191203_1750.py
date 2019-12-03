# Generated by Django 2.2.7 on 2019-12-03 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='calle',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='codigo_postal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='comuna',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='propiedad.Comuna'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='detalle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='numero',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='provincia',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='propiedad.Provincia'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='region',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='propiedad.Region'),
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
    ]