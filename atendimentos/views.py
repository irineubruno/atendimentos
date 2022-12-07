from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

from .models import Empresa, Cliente, Tecnico, Tipo_departamento, Tipo_atendimento, ordem_servico

class IndexView(TemplateView):
    template_name = 'index.html'
