# Generated by Django 2.2.4 on 2019-08-24 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_pedido_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='memoria',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='placadevideo',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='placamae',
        ),
    ]
