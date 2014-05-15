'''
AUTOR: Vinicius Fernandes Peixoto
USER GitHub: vfpeixoto
EMAIL: vfernandespeixoto@gmail.com
'''

from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime, date
from caixas.models import Conta
from pessoas.models import Pessoa

def fluxoListar(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'fluxos/fluxoListar.html', {'pessoas': pessoas})

def fluxoPesquisar(request):
    if request.method == 'POST':
        pessoaBusca = request.POST.get('pessoaBusca')
        dataBuscaInicio = request.POST.get('dataBuscaInicio', '')
        dataBuscaFim = request.POST.get('dataBuscaFinal', '')
        
        pessoas = Pessoa.objects.all().order_by('nome')

        split1 = dataBuscaInicio[0:10].split('/') 
        split2 = dataBuscaFim[0:10].split('/')
       
        if int(pessoaBusca) == 0:
            contas = Conta.objects.filter(data__gte=date( int(split1[2]), int(split1[1]), int(split1[0]) ) 
                                        , data__lte=date( int(split2[2]), int(split2[1]), int(split2[0]) ))
        else:
            contas = Conta.objects.filter(pessoa_id = pessoaBusca, data__gte=date( int(split1[2]), int(split1[1]), int(split1[0]) ) 
                                        , data__lte=date( int(split2[2]), int(split2[1]), int(split2[0]) ))        
        
        totalreceber = 0
        totalpagar = 0

        try:           
            for item in contas:
                if item.tipo == 'E':
                    totalreceber = totalreceber + item.valor
                else:
                    totalpagar = totalpagar + item.valor
        except:
            contas = []

        return render(request, 'fluxos/fluxoListar.html', {'contas': contas, 'pessoas': pessoas, 'totalreceber': totalreceber, 'totalpagar': totalpagar})
