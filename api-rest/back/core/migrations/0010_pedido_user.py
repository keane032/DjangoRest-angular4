# Generated by Django 2.2.4 on 2019-08-24 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190824_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='core.Cliente'),
            preserve_default=False,
        ),
    ]
