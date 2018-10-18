# Generated by Django 2.1.2 on 2018-10-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_venda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(blank=True, to='clientes.Produto'),
        ),
    ]
