# Generated by Django 2.2.4 on 2019-08-26 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20190825_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('qtd', models.IntegerField()),
                ('tamanho', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='pedido',
            name='memoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memorias', to='core.Memoria'),
        ),
    ]
