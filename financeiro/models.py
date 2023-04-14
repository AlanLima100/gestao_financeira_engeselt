from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals # estamos criando modelos de dados, exitem um processamento antes de salvar o modelo e depois, isso signifca que podemos aplicar um sinal "antes de voce inserir esses dados em um banco faz algo pra mim com ele" ou depois...usamos o sgno
from django.template.defaultfilters import slugify # já o slug cria caminho, exe: image-amor-primeira


class Base(models.Model):
    criado =models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True # ela é uma classe abstrata, ou seja, não é criada dentro do banco de dados, serve apenas de rascunho para outras classes


from django.db import models

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

class Receita(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data = models.DateField()
    descricao = models.CharField(max_length=200, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_RECEITA)
    comprovante = models.FileField(upload_to='comprovantes/')
    
    def __str__(self) -> str:
        return self.categoria


def receita_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.categoria)

signals.pre_save.connect(receita_pre_save, sender=Receita)# antes de salvar, execute a função 'receita_pre_sauve' quando Receita submeter um sinal *signal*, ou seja, quando Receita for salvo esse metodo vai ser executado