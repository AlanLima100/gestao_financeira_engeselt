from django.shortcuts import render

# View para visualizar a home
def home(request):
    return render (request, 'home.html')


# View para criar uma nova receita
def criar_receita(request):

    return render(request, 'criar_receita.html')


# View para criar uma nova despesa
def criar_despesa(request):

    return render(request, 'criar_despesa.html')


# View para listar todas as receitas
def lista_receitas(request):
    
    return render(request, 'lista_receitas.html')


# View para listar todas as despesas
def lista_despesas(request):
    
    return render(request, 'lista_despesas.html')


# View para editar uma receita existente
def editar_receita(request):

    return render(request, 'editar_receita.html')


# View para editar uma despesa existente
def editar_despesa(request, pk):

    return render(request, 'editar_despesa.html')



# View para excluir uma receita existente
def excluir_receita(request, pk):
    receita = Receita.objects.get(pk=pk)
    receita.delete()
    return redirect('lista_receitas')



# View para excluir uma despesa existente
def excluir_despesa(request, pk):
    despesa = Despesa.objects.get(pk=pk)
    despesa.delete()
    return redirect('lista_despesas')