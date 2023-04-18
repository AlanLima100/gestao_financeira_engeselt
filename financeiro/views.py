from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReceitaForm, DespesaForm
from .models import Receita, Despesa
from django.db.models import *
from datetime import datetime
from django.db.models import Q

import csv
from django.http import HttpResponse




# View para visualizar a home
def home(request):
    receitas = Receita.objects.all() # Busca todas as receitas do banco de dados
    context = {
        'receitas': receitas
    }
    return render(request, 'home.html', context)


def criar_receita(request):
    if str(request.method) == 'POST':
        form = ReceitaForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            form = ReceitaForm()
            return redirect('lista_receitas')
    else:
        form = ReceitaForm()
    context = {
        'form': form
    }    
    return render(request, 'criar_receita.html', context)



def criar_despesa(request):
    if str(request.method) == 'POST':
        form = DespesaForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            form = DespesaForm()
            return redirect('lista_despesas')
    else:
        form = DespesaForm()
    context = {
        'form': form
    }    
    return render(request, 'criar_despesa.html', context)



# def lista_receitas_despesas(request):
#     receitas = Receita.objects.all()
#     despesas = Despesa.objects.all()
#     lista = sorted(itertools.chain(receitas, despesas), key=lambda obj: obj.data, reverse=True)
#     return render(request, 'lista_receitas_despesas.html', {'receitas': receitas, 'despesas': despesas, 'lista': lista})

def lista_receitas(request):
    receitas = Receita.objects.order_by('-criado_em')
    return render(request, 'lista_receitas.html', {'receitas': receitas})

def lista_despesas(request):
    despesas = Despesa.objects.order_by('-criado_em')
    tem_filtro = False

    # filtro de valor
    min_valor = request.GET.get('min_valor')
    max_valor = request.GET.get('max_valor')
    if min_valor and max_valor:
        despesas = despesas.filter(valor__gte=min_valor, valor__lte=max_valor)
        tem_filtro = True
    elif min_valor:
        despesas = despesas.filter(valor__gte=min_valor)
        tem_filtro = True
    elif max_valor:
        despesas = despesas.filter(valor__lte=max_valor)
        tem_filtro = True

    # filtro de categoria
    categoria = request.GET.get('categoria')
    if categoria:
        despesas = despesas.filter(categoria=categoria)
        tem_filtro = True

    # filtro de período (data inicial e data final)
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    if data_inicial and data_final:
        try:
            data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
        except ValueError:
            data_inicial = None
        try:
            data_final = datetime.strptime(data_final, '%Y-%m-%d')
        except ValueError:
            data_final = None
        if data_inicial and data_final:
            despesas = despesas.filter(data__range=[data_inicial, data_final])
            tem_filtro = True

    # obter todas as categorias para exibição no filtro
    categorias = Despesa.objects.values_list('categoria', flat=True).distinct()

    context = {
        'despesas': despesas,
        'valor_filtro': {'min': min_valor, 'max': max_valor},
        'categoria_filtro': categoria,
        'data_inicial_filtro': data_inicial.strftime('%Y-%m-%d') if isinstance(data_inicial, datetime) else None,
        'data_final_filtro': data_final.strftime('%Y-%m-%d') if isinstance(data_final, datetime) else None,
        'tem_filtro': tem_filtro,
        'categorias': categorias,  # passa as categorias para o template
    }

    # Verifica se existem filtros aplicados
    if not tem_filtro:
        context['mensagem'] = 'Não foram aplicados filtros na busca.'

    return render(request, 'lista_despesas.html', context)


def editar_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    if request.method == 'POST':
        form = ReceitaForm(request.POST or None, instance=receita,
        initial={'data': receita.data})
        if form.is_valid():
            form.save()
            return redirect('lista_receitas')
    else:
        form = ReceitaForm(instance=receita, initial={'data': receita.data})
    return render(request, 'editar_receita.html', {'form': form, 'receita': receita})


def editar_despesa(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk)
    if request.method == 'POST':
        form = DespesaForm(request.POST or None, instance=despesa, initial={'data': despesa.data})
        if form.is_valid():
            form.save()
            return redirect('lista_despesas')
    else:
        form = DespesaForm(instance=despesa, initial={'data': despesa.data})

    return render(request, 'editar_despesa.html', {'form': form, 'despesa': despesa})



# View para excluir uma receita existente
def deletar_despesa(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk)

    if request.method == 'POST':
        despesa.delete()
        return redirect('lista_despesas')

    context = {
        'despesa': despesa,
    }
    return render(request, 'deletar_despesa.html', context)


# View para excluir uma despesa existente
def deletar_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)

    if request.method == 'POST':
        receita.delete()
        return redirect('lista_receitas')

    return render(request, 'deletar_despesa.html', {'receita': receita})

def baixar_receitas(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="receitas.csv"'

    writer = csv.writer(response)
    writer.writerow(['Valor', 'Categoria', 'Data/Hora', 'descricao'])

    
    receitas = Receita.objects.all() # aqui esta pegando todas as receitas, para especificar o periodo da data teria que aplicar um filtro aqui

    for receita in receitas:
        writer.writerow([receita.valor, receita.categoria, receita.data_hora, receita.descricao])

    return response


def baixar_despesas(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="despesas.csv"'

    writer = csv.writer(response)
    writer.writerow(['Valor', 'Categoria', 'Data/Hora'])

    despesas = Despesa.objects.all()

    for despesa in despesas:
        writer.writerow([despesa.valor, despesa.categoria, despesa.data_hora])

    return response


def baixar_despesas_filtradas(request):
    valor = request.GET.get('valor')
    data = request.GET.get('data')
    categoria = request.GET.get('categoria')
    
    despesas = Despesa.objects.filter(valor=valor, data=data, categoria=categoria)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="despesas.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['valor', 'data', 'categoria', 'descricao', 'comprovante'])
    
    for despesa in despesas:
        writer.writerow([despesa.valor, despesa.data, despesa.categoria, despesa.descricao, despesa.comprovante])
    
    return response
    

