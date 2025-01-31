# Generated by Django 2.1.7 on 2019-02-24 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('napi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prontuario_de_atendimento_integral_pai',
            name='Endereco',
            field=models.CharField(max_length=32, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='prontuario_de_atendimento_integral_pai',
            name='Estado_Civil',
            field=models.CharField(max_length=32, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='prontuario_de_atendimento_integral_pai',
            name='Idade',
            field=models.CharField(max_length=2, verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='prontuario_de_atendimento_integral_pai',
            name='Naturalidade',
            field=models.TextField(max_length=32, verbose_name='Naturalidade'),
        ),
        migrations.AlterField(
            model_name='prontuario_de_atendimento_integral_pai',
            name='Nome_da_Mae',
            field=models.CharField(max_length=64, verbose_name='Nome da Mãe'),
        ),
        migrations.AlterField(
            model_name='prontuario_de_atendimento_integral_pai',
            name='Nome_do_Pai',
            field=models.TextField(max_length=64, verbose_name='Nome do Pai'),
        ),
        migrations.AlterField(
            model_name='prontuario_de_atendimento_integral_pai',
            name='Profissao',
            field=models.TextField(max_length=32, verbose_name='Profissão'),
        ),
        migrations.AlterField(
            model_name='prontuario_de_atendimento_integral_pai',
            name='data_de_registro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='prontuario_de_atendimento_integral_pai',
            name='nome',
            field=models.CharField(max_length=64, verbose_name='Nome'),
        ),
    ]
