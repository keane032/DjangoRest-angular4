# Generated by Django 2.2.4 on 2019-08-24 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_pedido_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='procecador',
            new_name='placamae',
        ),
    ]
