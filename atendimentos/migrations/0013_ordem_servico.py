# Generated by Django 3.2.14 on 2022-12-07 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0012_tipo_departamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordem_servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('descricao', models.TextField(verbose_name='Descição Defeito')),
                ('resolucao', models.TextField(verbose_name='Resolucao Defeito')),
                ('tipo', models.CharField(choices=[('pendente', 'Pendente'), ('aguardando', 'Aguardando'), ('finalizado', 'Finalizado')], max_length=20, verbose_name='Tipo')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimentos.cliente')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimentos.empresa')),
                ('tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimentos.tecnico')),
                ('tipo_atendimento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimentos.tipo_atendimento')),
                ('tipo_departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimentos.tipo_departamento')),
            ],
            options={
                'verbose_name': 'Ordem de Serviço',
                'verbose_name_plural': 'Ordem de Serviços',
                'ordering': ['data'],
            },
        ),
    ]
