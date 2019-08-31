# Generated by Django 2.2.4 on 2019-08-28 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_pedido_memoriapedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='MemoriaPedido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='memoria',
            field=models.ManyToManyField(related_name='mps', to='core.Memoria'),
        ),
        migrations.DeleteModel(
            name='MemoriaPedido',
        ),
    ]
