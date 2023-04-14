from django.shortcuts import render
from .forms import ReceitaForm, DespesaForm
from django.contrib import messages

# View para visualizar a home
def home(request):
    return render (request, 'home.html')


# View para criar uma nova receita
def criar_receita(request):
    form = ReceitaForm(request.POST or None) # pdoe conter dados quando o usuário clicar "POST" no botão enviar ou um form vazio quando "GET" assim que abre a pagina 'criar_receita'
    if str(request.method) == 'POST': #ou seja o usuário clicou e enviou dados
        if form.is_valid(): # e só tudo foi preenchido certinho e tá valido, se o formulário n tem erros return true
            valor = form.cleaned_data['valor'] # pegue esses dados ...
            data = form.cleaned_data['data']
            categoria = form.cleaned_data['categoria']
            descricao = form.cleaned_data['descricao']

            print('Dados registrados')
            print(f'Valor: {valor}')
            print(f'Data: {data}')
            print(f'Categoria: {categoria}')
            print(f'Valor: {descricao}')

            messages.success(request, 'Dados da  receita cadastrado com sucesso!')#adicionando mensagens que vai aparecerla no html quando clicar em enviarque chamei no bootstrap_messages
            form = ReceitaForm() # limpando o formulario
        else: # caso não for um formulário
            messages.error(request, 'Erro ao cadastrar dados na receita')    
    context = {
        'form': form
    }
    return render(request, 'criar_receita.html', context)


# View para criar uma nova despesa
def criar_despesa(request):
    form = DespesaForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            valor = form.cleaned_data['valor'] # pegue esses dados ...
            data = form.cleaned_data['data']
            categoria = form.cleaned_data['categoria']
            descricao = form.cleaned_data['descricao']

            print('Dados registrados')
            print(f'Valor: {valor}')
            print(f'Data: {data}')
            print(f'Categoria: {categoria}')
            print(f'Valor: {descricao}')

            messages.success(request, 'Dados da Despesa cadastrado com sucesso!')

            form = DespesaForm()
        else:
            messages.error(request= 'Erro ao cadastrar dos dados das Despesas')
    context = {
            'form': form
    }

    return render(request, 'criar_despesa.html', context)


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