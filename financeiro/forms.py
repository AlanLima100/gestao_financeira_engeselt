from django import forms


# Formulário para criação/edição de uma receita
class ReceitaForm(forms.Form):
    valor = forms.DecimalField(label='Valor:', max_digits=8, decimal_places=2)
    data = forms.DateField(label='Data:')
    categoria = forms.ChoiceField(label='Categoria:', choices=[('investimento', 'Investimento'), ('presente', 'Presente'), ('premio', 'Prêmio'), ('salario', 'Salário'), ('outros', 'Outros')])
    descricao = forms.CharField(label='Descrição:',  widget=forms.Textarea())

   

# Formulário para criação/edição de uma despesa
class DespesaForm(forms.Form):
    valor = forms.DecimalField(label='Valor:', max_digits=8, decimal_places=2)
    data = forms.DateField(label='Data:')
    categoria = forms.ChoiceField(label='Categoria:', choices=[
        ('casa', 'Casa'),
        ('educacao', 'Educação'),
        ('eletronicos', 'Eletrônicos'),
        ('lazer', 'Lazer'),
        ('saude', 'Saúde'),
        ('supermercado', 'Supermercado'),
        ('transporte', 'Transporte'),
        ('outros', 'Outros')
    ])
    descricao = forms.CharField(label='Descrição:', widget=forms.Textarea()) # texto em area com varias linhas



