from django.contrib import admin
from .models import Receita



@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'data', 'categoria', 'descricao', 'slug', 'criado', 'modificado', 'ativo')

    list_filter = ['categoria']
    search_fields = ['descricao']

