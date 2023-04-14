from django.urls import path
from .views import home,criar_receita, criar_despesa, lista_receitas, lista_despesas, editar_receita, editar_despesa, excluir_receita, excluir_despesa

urlpatterns = [
    path('', home, name='home'),
    path('criar-receita/', criar_receita, name='criar_receita'),
    path('criar-despesa/', criar_despesa, name='criar_despesa'),
    path('lista-receitas/', lista_receitas, name='lista_receitas'),
    path('lista-despesas/', lista_despesas, name='lista_despesas'),
    path('editar-receita/', editar_receita, name='editar_receita'),
    path('editar-despesa/', editar_despesa, name='editar_despesa'),
    path('excluir-receita/', excluir_receita, name='excluir_receita'),
    path('excluir-despesa/', excluir_despesa, name='excluir_despesa'),
]