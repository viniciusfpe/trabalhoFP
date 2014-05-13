'''
AUTOR: Vinicius Fernandes Peixoto
USER GitHub: vfpeixoto
EMAIL: vfernandespeixoto@gmail.com
'''

from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from caixas.models import Conta
from pessoas.models import Pessoa

def fluxoListar(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'fluxos/fluxoListar.html', {'pessoas': pessoas})

def fluxoPesquisar(request):
    if request.method == 'POST':
        pessoaBusca = request.POST.get('pessoaBusca')
        dataBuscaInicio = datetime.strptime(request.POST.get('dataBuscaInicio', ''), '%d/%m/%Y %H:%M:%S')
        dataBuscaFim = datetime.strptime(request.POST.get('dataBuscaFinal', ''), '%d/%m/%Y %H:%M:%S')
        
        pessoas = Pessoa.objects.all().order_by('nome')

        totalreceber = 0
        totalpagar = 0
       
        if int(pessoaBusca) == 0:
            sql = "select cc.* from caixas_conta cc where cc.data >= '%s' and  cc.data <= '%s'" % (dataBuscaInicio, dataBuscaFim)
        else:
            sql = "select cc.* from caixas_conta cc inner join pessoas_pessoa pp on pp.id = cc.pessoa_id where cc.pessoa_id like %s  and cc.data >= '%s' and  cc.data <= '%s' order by cc.data" % (pessoaBusca, dataBuscaInicio, dataBuscaFim)
        try:            
            contas = Conta.objects.raw(sql)

            for item in contas:
                if item.tipo == 'E':
                    totalreceber = totalreceber + item.valor
                else:
                    totalpagar = totalpagar + item.valor
        except:
            contas = []

        return render(request, 'fluxos/fluxoListar.html', {'contas': contas, 'pessoas': pessoas, 'totalreceber': totalreceber, 'totalpagar': totalpagar})


