from django import forms
from django.core.mail.message import EmailMessage
from .models import Despesa, Receita

# Formulário para criação/edição de uma receita
class ReceitaForm(forms.Form):
    valor = forms.DecimalField(label='Valor:', max_digits=8, decimal_places=2)
    data = forms.DateField(label='Data:')
    categoria = forms.ChoiceField(label='Categoria:', choices=[('investimento', 'Investimento'), ('presente', 'Presente'), ('premio', 'Prêmio'), ('salario', 'Salário'), ('outros', 'Outros')])
    descricao = forms.CharField(label='Descrição:',  widget=forms.Textarea())


   

# # Formulário para criação/edição de uma despesa
class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = '__all__'

    def save(self, commit=True):
        despesa = super(DespesaForm, self).save(commit=False)
        if commit:
            despesa.save()
        return despesa



