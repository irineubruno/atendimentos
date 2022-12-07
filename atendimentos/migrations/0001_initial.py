# Generated by Django 3.2.14 on 2022-12-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=250, verbose_name='Slug')),
                ('cnpj', models.CharField(max_length=20, unique=True, verbose_name='CNPJ')),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['nome'],
            },
        ),
    ]
