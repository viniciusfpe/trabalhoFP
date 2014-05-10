from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from django.db.models import Q 
from caixas.models import Conta
from pessoas.models import Pessoa

def fluxoListar(request):
    fluxo = Conta
    return render(request, 'fluxos/fluxoListar.html', {'fluxo': fluxo})