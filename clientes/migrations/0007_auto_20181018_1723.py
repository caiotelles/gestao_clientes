# Generated by Django 2.1.2 on 2018-10-18 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20181018_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoas',
            name='doc',
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
    ]
