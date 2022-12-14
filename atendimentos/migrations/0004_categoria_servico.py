# Generated by Django 3.2.14 on 2022-12-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0003_tecnico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slug')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
            },
        ),
    ]
