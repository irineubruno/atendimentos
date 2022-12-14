# Generated by Django 3.2.14 on 2022-12-07 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0013_ordem_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem_servico',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atendimentos.cliente'),
        ),
        migrations.AlterField(
            model_name='ordem_servico',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atendimentos.empresa'),
        ),
        migrations.AlterField(
            model_name='ordem_servico',
            name='tecnico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atendimentos.tecnico'),
        ),
        migrations.AlterField(
            model_name='ordem_servico',
            name='tipo_atendimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atendimentos.tipo_atendimento'),
        ),
        migrations.AlterField(
            model_name='ordem_servico',
            name='tipo_departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atendimentos.tipo_departamento'),
        ),
    ]
