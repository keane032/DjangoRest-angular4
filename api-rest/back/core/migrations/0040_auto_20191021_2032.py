# Generated by Django 2.2.4 on 2019-10-21 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20191021_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placamae',
            old_name='total_memorias',
            new_name='total_memoria',
        ),
    ]
