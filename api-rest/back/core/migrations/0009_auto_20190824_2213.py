# Generated by Django 2.2.4 on 2019-08-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_pedido_placamae'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='memoria',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='placadevideo',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
