# Generated by Django 2.2.4 on 2019-08-28 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20190828_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='memorias',
            field=models.ManyToManyField(to='core.Memoria'),
        ),
    ]