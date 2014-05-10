from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from django.db.models import Q 
from caixas.models import Conta
from pessoas.models import Pessoa

def fluxoListar(request):
    fluxo = Conta
    pessoas = Pessoa.objects.all().order_by('nome')

    return render(request, 'fluxos/fluxoListar.html', {'fluxo': fluxo, 'pessoas': pessoas})

