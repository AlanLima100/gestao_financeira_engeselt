from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReceitaForm, DespesaForm
from .models import Receita, Despesa
import itertools




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
            return redirect('lista_receitas_despesas')
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
            return redirect('lista_receitas_despesas')
    else:
        form = DespesaForm()
    context = {
        'form': form
    }    
    return render(request, 'criar_despesa.html', context)



def lista_receitas_despesas(request):
    receitas = Receita.objects.all()
    despesas = Despesa.objects.all()
    lista = sorted(itertools.chain(receitas, despesas), key=lambda obj: obj.data, reverse=True)
    return render(request, 'lista_receitas_despesas.html', {'receitas': receitas, 'despesas': despesas, 'lista': lista})



def editar_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            return redirect('lista_receitas_despesas')
    else:
        form = ReceitaForm(instance=receita)
    return render(request, 'editar_receita.html', {'form': form})


def editar_despesa(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk)
    if request.method == 'POST':
        form = DespesaForm(request.POST or None, instance=despesa, initial={'data': despesa.data})
        if form.is_valid():
            form.save()
            return redirect('lista_receitas_despesas')
    else:
        form = DespesaForm(instance=despesa, initial={'data': despesa.data})

    return render(request, 'editar_despesa.html', {'form': form, 'despesa': despesa})



# View para excluir uma receita existente
def deletar_despesa(request, pk):
    despesa = get_object_or_404(Despesa, pk=pk)

    if request.method == 'POST':
        despesa.delete()
        return redirect('lista_receitas_despesas')

    context = {
        'despesa': despesa,
    }
    return render(request, 'deletar_despesa.html', context)


# View para excluir uma despesa existente
def deletar_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)

    if request.method == 'POST':
        receita.delete()
        return redirect('lista_receitas_despesas')

    return render(request, 'deletar_despesa.html', {'receita': receita})