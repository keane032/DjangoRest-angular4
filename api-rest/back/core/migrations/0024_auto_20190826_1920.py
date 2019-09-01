# Generated by Django 2.2.4 on 2019-08-26 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20190826_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='memoria',
        ),
        migrations.CreateModel(
            name='MemoriaPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd', models.IntegerField()),
                ('memoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mecoriaPedido', to='core.Memoria')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='memorias',
            field=models.ManyToManyField(related_name='memorias', to='core.MemoriaPedido'),
        ),
    ]