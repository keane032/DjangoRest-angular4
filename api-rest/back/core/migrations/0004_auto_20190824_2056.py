# Generated by Django 2.2.4 on 2019-08-24 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_cliente_idade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procecador', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='pedidos',
        ),
        migrations.DeleteModel(
            name='Pedidos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='core.Cliente'),
        ),
    ]
