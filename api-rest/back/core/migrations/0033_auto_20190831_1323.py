# Generated by Django 2.2.4 on 2019-08-31 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_procecador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='placamae',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Placamae', to='core.PlacaMae'),
        ),
    ]
