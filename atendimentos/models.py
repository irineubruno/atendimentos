from django.db import models

class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=250)
    slug = models.SlugField('Slug', max_length=250)
    cnpj = models.CharField('CNPJ', max_length=20, unique=True)
    endereco = models.CharField('Endereço', max_length=50)
    telefone = models.CharField('Telefone', max_length=50)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome']

    def __str__(self):
        return self.nome



class Cliente(models.Model):
    TIPO_CLIENTE = (
        ("cnpj", "Pessoa Jurídica"),
        ("cpf", "Pessoa Física")
    )
    tipo = models.CharField('Tipo de Pessoa', max_length=4, choices=TIPO_CLIENTE, blank=False, null=False)
    nome = models.CharField('Nome', max_length=250)
    slug = models.SlugField('Slug', max_length=250)
    identificador = models.CharField('CNPJ/CPF', max_length=20, unique=True)
    endereco = models.CharField('Endereço', max_length=50)
    telefone = models.CharField('Telefone' ,max_length=50)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Tecnico(models.Model):
    TEC_SEXO = (
        ("F", "Feminino"),
        ("M", "Masculino")
    )
    nome = models.CharField('Nome', max_length=250)
    slug = models.SlugField('Slug', max_length=250)
    sexo = models.CharField('Sexo', max_length=1, choices=TEC_SEXO, blank=False, null=False)
    cpf = models.CharField('CPF', max_length=20, unique=True)
    telefone = models.CharField('Telefone', max_length=50)

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Tipo_atendimento(models.Model):
    nome = models.CharField('nome', max_length=250)

    class Meta:
        verbose_name = 'Tipo de Atendimento'
        verbose_name_plural = 'Tipo de Atendimentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Tipo_departamento(models.Model):
    nome = models.CharField('nome', max_length=250)

    class Meta:
        verbose_name = 'Tipo de Departamentos'
        verbose_name_plural = 'Tipo de Departamentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class ordem_servico(models.Model):
    OS_TIPO = (
        ("pendente", "Pendente"),
        ("aguardando", "Aguardando"),
        ("finalizado", "Finalizado")
    )
    data = models.DateTimeField('Data')
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, blank=True, null=True)
    tipo_atendimento = models.ForeignKey(Tipo_atendimento, on_delete=models.SET_NULL, blank=True, null=True)
    tipo_departamento = models.ForeignKey(Tipo_departamento, on_delete=models.SET_NULL, blank=True, null=True)
    descricao = models.TextField('Descrição do Defeito')
    resolucao = models.TextField('Resolução do Defeito')
    tipo = models.CharField('Tipo', max_length=20, choices=OS_TIPO, blank=False, null=False)

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordem de Serviços'
        ordering = ['tipo_departamento']
