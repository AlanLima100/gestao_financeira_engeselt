from django.urls import path
from .views import home, criar_receita, criar_despesa, lista_receitas, lista_despesas, editar_receita, editar_despesa, deletar_despesa, deletar_receita

urlpatterns = [
    path('', home, name='home'),

    path('criar-receita/', criar_receita, name='criar_receita'),

    path('criar-despesa/', criar_despesa, name='criar_despesa'),


    path('lista-receitas/', lista_receitas, name='lista_receitas'),

    path('lista-despesas/', lista_despesas, name='lista_despesas'),


    path('editar-despesa/<int:pk>/', editar_despesa, name='editar_despesa'),

    path('deletar-despesa/<int:pk>/',deletar_despesa, name='deletar_despesa'),

    path('editar-receita/<int:pk>/', editar_receita, name='editar_receita'),
    
    path('deletar-receita/<int:pk>/', deletar_receita, name='deletar_receita'),
]
