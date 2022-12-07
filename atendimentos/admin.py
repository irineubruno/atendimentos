from django.contrib import admin
from atendimentos.models import Empresa, Cliente, Tecnico, Tipo_atendimento, Tipo_departamento, ordem_servico

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'cnpj', 'endereco', 'telefone']
    prepopulated_fields = {'slug': ('nome', 'cnpj',)}

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'nome', 'slug', 'identificador', 'endereco', 'telefone']
    prepopulated_fields = {'slug': ('nome', 'identificador',)}

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'sexo', 'cpf', 'telefone']
    prepopulated_fields = {'slug': ('nome', 'cpf',)}

@admin.register(Tipo_atendimento)
class Tipo_atendimentoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Tipo_departamento)
class Tipo_departamentoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(ordem_servico)
class Ordem_servicoAdmin(admin.ModelAdmin):
    #list_display = ['tipo_departamento', 'tipo','data', 'descricao', 'resolucao', ]
    list_display = ['data', 'empresa', 'cliente', 'tecnico', 'tipo_atendimento', 'tipo_departamento', 'descricao', 'resolucao', 'tipo']
