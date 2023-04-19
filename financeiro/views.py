from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReceitaForm, DespesaForm
from .models import Receita, Despesa
from django.db.models import *
from datetime import datetime
import csv
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages





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
            # Verifica se já existe uma despesa com os mesmos valores
            valor = form.cleaned_data['valor']
            data = form.cleaned_data['data']
            categoria = form.cleaned_data['categoria']
            receitas = Receita.objects.filter(valor=valor, data=data, categoria=categoria)
            if receitas.exists():
                messages.error(request, 'Já existe uma receita com esses valores.')
                return redirect('criar_receita')
            # Salva a nova despesa
            form.save()
            messages.success(request, 'Receita cadastrada com sucesso.')
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
            # Verifica se já existe uma despesa com os mesmos valores
            valor = form.cleaned_data['valor']
            data = form.cleaned_data['data']
            categoria = form.cleaned_data['categoria']
            despesas = Despesa.objects.filter(valor=valor, data=data, categoria=categoria)
            if despesas.exists():
                messages.error(request, 'Já existe uma despesa com esses valores.')
                return redirect('criar_despesa')
            # Salva a nova despesa
            form.save()
            messages.success(request, 'Despesa cadastrada com sucesso.')
            form = DespesaForm()
            return redirect('lista_despesas')
    else:
        form = DespesaForm()
    context = {
        'form': form
    }    
    return render(request, 'criar_despesa.html', context)



def lista_receitas(request):
    receitas = Receita.objects.order_by('-criado_em')
    tem_filtro = False

    # filtro de valor
    min_valor = request.GET.get('min_valor')
    max_valor = request.GET.get('max_valor')
    if min_valor and max_valor:
        receitas = receitas.filter(valor__gte=min_valor, valor__lte=max_valor)
        tem_filtro = True
    elif min_valor:
        receitas = receitas.filter(valor__gte=min_valor)
        tem_filtro = True
    elif max_valor:
        receitas = receitas.filter(valor__lte=max_valor)
        tem_filtro = True

    # filtro de categoria
    categoria = request.GET.get('categoria')
    if categoria:
        receitas = receitas.filter(categoria=categoria)
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
            receitas = receitas.filter(data__range=[data_inicial, data_final])
            tem_filtro = True

    # obter todas as categorias para exibição no filtro
    categorias = Receita.objects.values_list('categoria', flat=True).distinct()

    context = {
        'receitas': receitas,
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

    return render(request, 'lista_receitas.html', context)

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
    valor = request.GET.get('min_valor')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    categoria = request.GET.get('categoria')

    despesas = Despesa.objects.all()
    if valor:
        despesas = despesas.filter(valor__gte=valor)
    if data_inicial:
        despesas = despesas.filter(data__gte=data_inicial)
    if data_final:
        despesas = despesas.filter(data__lte=data_final)
    if categoria:
        despesas = despesas.filter(categoria__icontains=categoria)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="despesas.csv"'

    writer = csv.writer(response)
    writer.writerow(['valor', 'data', 'categoria', 'descricao', 'comprovante'])

    for despesa in despesas:
        writer.writerow([despesa.valor, despesa.data, despesa.categoria, despesa.descricao, despesa.comprovante])

    return response


def baixar_receitas_filtradas(request):
    valor = request.GET.get('min_valor')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    categoria = request.GET.get('categoria')

    despesas = Receita.objects.all()
    if valor:
        despesas = despesas.filter(valor__gte=valor)
    if data_inicial:
        despesas = despesas.filter(data__gte=data_inicial)
    if data_final:
        despesas = despesas.filter(data__lte=data_final)
    if categoria:
        despesas = despesas.filter(categoria__icontains=categoria)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="despesas.csv"'

    writer = csv.writer(response)
    writer.writerow(['valor', 'data', 'categoria', 'descricao', 'comprovante'])

    for despesa in despesas:
        writer.writerow([despesa.valor, despesa.data, despesa.categoria, despesa.descricao, despesa.comprovante])

    return response
