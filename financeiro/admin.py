from django.contrib import admin
from .models import Receita, Despesa




class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'data', 'categoria', 'descricao')
    list_filter = ['categoria', 'valor', 'data']
    search_fields = ['descricao']

admin.site.register(Receita, ReceitaAdmin)



class DespesaAdmin(admin.ModelAdmin):
    list_display =('valor', 'data', 'categoria', 'descricao')
    list_filter = ['categoria', 'valor', 'data']
    search_fields = ['descricao']

admin.site.register(Despesa, DespesaAdmin)