from django.utils import timezone
from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals # estamos criando modelos de dados, exitem um processamento antes de salvar o modelo e depois, isso signifca que podemos aplicar um sinal "antes de voce inserir esses dados em um banco faz algo pra mim com ele" ou depois...usamos o sgno
from django.template.defaultfilters import slugify # já o slug cria caminho, exe: image-amor-primeira


class Base(models.Model):
    criado =models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    criado_em = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True # ela é uma classe abstrata, ou seja, não é criada dentro do banco de dados, serve apenas de rascunho para outras classes


CATEGORIAS_RECEITA = (
    ('INVESTIMENTO', 'Investimento'),
    ('PRESENT', 'Presente'),
    ('PREMIO', 'Prêmio'),
    ('SALARIO', 'Salário'),
    ('OUTROS', 'Outros'),
)

CATEGORIAS_DESPESA = (
    ('CASA', 'Casa'),
    ('EDUCACAO', 'Educação'),
    ('ELETRONICOS', 'Eletrônicos'),
    ('LAZER', 'Lazer'),
    ('SAUDE', 'Saúde'),
    ('SUPERMERCADO', 'Supermercado'),
    ('TRANSPORTE', 'Transporte'),
    ('OUTROS', 'Outros'),
)

class Receita(Base):
    valor = models.DecimalField('Valor:', max_digits=8, decimal_places=2)

    data = models.DateField('Data:')
    categoria = models.CharField('Categoria:', choices=CATEGORIAS_RECEITA , max_length=200, blank=True)


    descricao = models.CharField('Descrição:', max_length=200, blank=True)

    comprovante = models.FileField(upload_to='comprovantes/')
    
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.categoria} - {self.valor}'





class Despesa(Base):
    valor = models.DecimalField('Valor:', max_digits=8, decimal_places=2)
    data = models.DateField('Data:')

    categoria = models.CharField('Categoria:',choices=CATEGORIAS_DESPESA, max_length=200, blank=True )

    descricao = models.CharField('Descrição:', max_length=200, blank=True)

    comprovante = models.FileField(upload_to='comprovantes/')

    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.categoria} - {self.valor}'
    
