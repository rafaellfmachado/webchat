# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-24 08:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado')),
                ('deleted', models.BooleanField(default=False, verbose_name='Removido')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ('-updated',),
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
                'permissions': (('supervisor_chat', 'Supervisor CHAT'),),
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var', models.CharField(max_length=100, verbose_name='Vari\xe1vel')),
                ('desc', models.CharField(max_length=100, verbose_name='Descri\xe7\xe3o')),
                ('value', models.TextField(verbose_name='Valor')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Configura\xe7\xe3o',
                'verbose_name_plural': 'Configura\xe7\xf5es',
                'permissions': (('vnc_config', 'Acesso VNC'),),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactid', models.CharField(db_index=True, max_length=200)),
                ('contactname', models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='Nome Profile')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('profile_pic', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notas')),
                ('ctype', models.CharField(choices=[(b'whatsapp', b'Whatsapp'), (b'facebook', b'Facebook')], default=b'whatsapp', max_length=100, verbose_name='Tipo de Contato')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado')),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Lista Contato',
                'verbose_name_plural': 'Listas de Contato',
            },
        ),
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invalid_count', models.IntegerField(default=0)),
                ('data', models.TextField(blank=True, null=True, verbose_name='Dados')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('userstart', models.DateTimeField(blank=True, null=True, verbose_name='Inicio Atendimento')),
                ('userstop', models.DateTimeField(blank=True, null=True, verbose_name='Fim Atendimento')),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Aberto'), (2, 'Encerrado')], default=1, null=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.Chat')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Descri\xe7\xe3o')),
                ('filter_match', models.CharField(choices=[(b'exact', 'Igual'), (b'iexact', 'Igual(ignorando maisculo/min\xfasculo)'), (b'startswith', 'Come\xe7ar com'), (b'endswith', 'Finalizar com')], default=b'iexact', max_length=50)),
                ('check', models.TextField(verbose_name='Verificar Mensagem')),
                ('reply', models.TextField(blank=True, null=True, verbose_name='Resposta')),
                ('replygroup', models.BooleanField(default=True, help_text='Se desmarcar e mensagem vier do grupo, ser\xe1 respondido no privado', verbose_name='Responder para Grupo ?')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('contacts', models.ManyToManyField(blank=True, to='chatapp.Contact', verbose_name='Contatos')),
                ('contactslist', models.ManyToManyField(blank=True, to='chatapp.ContactList', verbose_name='Listas de Contato')),
            ],
            options={
                'ordering': ('check',),
                'verbose_name': 'Filtro',
                'verbose_name_plural': 'Filtros',
            },
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descri\xe7\xe3o')),
                ('start_date', models.TimeField(verbose_name=b'Data Inicial')),
                ('end_date', models.TimeField(verbose_name=b'Data Final')),
                ('message', models.TextField(blank=True, null=True, verbose_name=b'Mensagem')),
                ('status', models.BooleanField(default=True, verbose_name=b'Ativo')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group')),
            ],
            options={
                'verbose_name': 'Intervalo de Atendimento',
                'verbose_name_plural': 'Intervalos de Atendimento',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Descri\xe7\xe3o')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('retry', models.IntegerField(blank=True, default=10, null=True, verbose_name='Tentativas Item Menu')),
                ('invalid_option_message', models.TextField(blank=True, null=True, verbose_name='Mensagem Op\xe7\xe3o Inv\xe1lida')),
                ('default', models.BooleanField(verbose_name='Menu Padrao')),
            ],
            options={
                'ordering': ('description',),
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.IntegerField(default=1, verbose_name='Sequ\xeancia')),
                ('option', models.CharField(max_length=255, verbose_name='C\xf3digo/Op\xe7\xe3o')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Mensagem')),
                ('input_data', models.BooleanField(default=False, verbose_name='Entrada de Dados ?')),
                ('leave_group', models.BooleanField(help_text='Definir apenas quando cliente acessar menu e quiser voltar para menu anterior de outro setor', verbose_name='Sair do Grupo atual')),
                ('group_chat', models.BooleanField(verbose_name='Falar com atendente')),
                ('leave_chat', models.BooleanField(default=False, verbose_name='Encerrar atendimento')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.Menu', verbose_name='Menu')),
                ('option_menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_menu', to='chatapp.Menu', verbose_name='Pr\xf3ximo Menu')),
            ],
            options={
                'ordering': ('menu__id', 'seq', 'option'),
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Itens',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.TextField(blank=True, null=True)),
                ('reply_message_id', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True, verbose_name='Conte\xfado')),
                ('caption', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=b'media/chatapp')),
                ('mtype', models.CharField(blank=True, db_column=b'type', default=b'chat', max_length=100, null=True, verbose_name='Tipo')),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('mime', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrada')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Aguardando Envio'), (1, 'Enviando Mensagem'), (2, 'Enviada'), (3, 'Recebida'), (99, 'Erro no Envio')], null=True, verbose_name='Status')),
                ('error', models.TextField(blank=True, null=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.Chat')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatapp.Contact', verbose_name='Contato')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usu\xe1rio')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='Descri\xe7\xe3o')),
                ('script_file', models.FileField(upload_to=b'scripts', verbose_name='Script')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'ordering': ('description',),
                'verbose_name': 'Script',
                'verbose_name_plural': 'Scripts',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctype', models.CharField(choices=[(b'whatsapp', b'Whatsapp'), (b'facebook', b'Facebook')], max_length=200, verbose_name='Tipo')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('username', models.CharField(blank=True, max_length=200, null=True, verbose_name='Usu\xe1rio')),
                ('password', models.CharField(blank=True, max_length=200, null=True, verbose_name='Senha')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Canal Atendimento',
                'verbose_name_plural': 'Canais de Atendimento',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descri\xe7\xe3o')),
                ('token', models.CharField(max_length=255, unique=True, verbose_name='Token')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Mapear Usu\xe1rio')),
            ],
            options={
                'ordering': ('description',),
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
            },
        ),
        migrations.AddField(
            model_name='menuitem',
            name='script',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemscript', to='chatapp.Script'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='updategroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Definir Grupo'),
        ),
        migrations.AddField(
            model_name='filter',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatapp.Menu', verbose_name='Enviar Menu'),
        ),
        migrations.AddField(
            model_name='filter',
            name='script',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatapp.Script', verbose_name='Script'),
        ),
        migrations.AddField(
            model_name='filter',
            name='sources',
            field=models.ManyToManyField(blank=True, help_text='Preenche apenas se desejar aplicar o filtro em determinado canal', to='chatapp.Source', verbose_name='Canais de atendimento'),
        ),
        migrations.AddField(
            model_name='customerservice',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatapp.Menu'),
        ),
        migrations.AddField(
            model_name='customerservice',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Respons\xe1vel'),
        ),
        migrations.AddField(
            model_name='contact',
            name='groups',
            field=models.ManyToManyField(blank=True, to='chatapp.ContactList', verbose_name='Grupos'),
        ),
        migrations.AddField(
            model_name='chat',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatapp.Contact', verbose_name='Contato'),
        ),
        migrations.AddField(
            model_name='chat',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='Grupo'),
        ),
        migrations.AddField(
            model_name='chat',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Respons\xe1vel'),
        ),
        migrations.AddField(
            model_name='chat',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatapp.Source', verbose_name='Canal de Atendimento'),
        ),
    ]