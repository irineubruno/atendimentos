# Generated by Django 3.2.14 on 2022-12-07 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0008_alter_solicitacao_situacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='solicitacao',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='solicitacao',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='solicitacao',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='solicitacao',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='solicitacao',
            name='tecnico',
        ),
        migrations.DeleteModel(
            name='Categoria_servico',
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.DeleteModel(
            name='Solicitacao',
        ),
    ]
