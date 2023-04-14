from django import forms
from django.core.mail.message import EmailMessage

# Formulário para criação/edição de uma receita
class ReceitaForm(forms.Form):
    valor = forms.DecimalField(label='Valor:', max_digits=8, decimal_places=2)
    data = forms.DateField(label='Data:')
    categoria = forms.ChoiceField(label='Categoria:', choices=[('investimento', 'Investimento'), ('presente', 'Presente'), ('premio', 'Prêmio'), ('salario', 'Salário'), ('outros', 'Outros')])
    descricao = forms.CharField(label='Descrição:',  widget=forms.Textarea())

    def send_mail(self):
        valor = self.cleaned_data['valor']
        data = self.cleaned_data['data']
        categoria = self.cleaned_data['categoria']
        descricao = self.cleaned_data['descrcicao']

        conteudo = f'Valor: {valor} \n Data: {data} \nCategoria: {categoria}\n Descrição: {descricao}'

        mail = EmailMessage(
            subject='E-mail enviado pelo 654545',
            body=conteudo,
            from_email='coontato@seudominio.com.br',
            to=['contato@seudominio.com.br', ],
            headers={'Reaply=-To' : data}
        )
        mail.send()

   

# # Formulário para criação/edição de uma despesa
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



