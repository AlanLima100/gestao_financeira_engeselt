from django import forms
from .models import Despesa, Receita

# Formulário para criação/edição de uma receita
class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'
    
    def save(self, commit=True):
        receita = super(ReceitaForm, self).save(commit=False)
        if commit:
            receita.save()
        return receita

   

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



