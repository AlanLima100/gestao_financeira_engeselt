# Generated by Django 4.2 on 2023-04-21 01:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('criado_em', models.DateTimeField(default=django.utils.timezone.now)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor:')),
                ('data', models.DateField(verbose_name='Data:')),
                ('categoria', models.CharField(blank=True, choices=[('CASA', 'Casa'), ('EDUCACAO', 'Educação'), ('ELETRONICOS', 'Eletrônicos'), ('LAZER', 'Lazer'), ('SAUDE', 'Saúde'), ('SUPERMERCADO', 'Supermercado'), ('TRANSPORTE', 'Transporte'), ('OUTROS', 'Outros')], max_length=200, verbose_name='Categoria:')),
                ('descricao', models.CharField(blank=True, max_length=200, verbose_name='Descrição:')),
                ('comprovante', models.FileField(upload_to='comprovantes/')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('criado_em', models.DateTimeField(default=django.utils.timezone.now)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor:')),
                ('data', models.DateField(verbose_name='Data:')),
                ('categoria', models.CharField(blank=True, choices=[('INVESTIMENTO', 'Investimento'), ('PRESENT', 'Presente'), ('PREMIO', 'Prêmio'), ('SALARIO', 'Salário'), ('OUTROS', 'Outros')], max_length=200, verbose_name='Categoria:')),
                ('descricao', models.CharField(blank=True, max_length=200, verbose_name='Descrição:')),
                ('comprovante', models.FileField(upload_to='comprovantes/')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
