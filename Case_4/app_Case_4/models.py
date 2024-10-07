from django.db import models
from django.http import JsonResponse
import json

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

class Projeto(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    preco = models.IntegerField()
    dias = models.IntegerField()
    coordenadores = models.JSONField(default=list)# precisa são 
    projetistas = models.JSONField(default=list)

class Trainee(models.Model):
    id_trainee = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.TextField(max_length=255)
    curso = models.TextField(max_length=255)
    semestre = models.TextField(max_length=255)

class Membro(models.Model):
    id_membro = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    cargo = models.TextField(max_length=255)
    projetos = models.JSONField(default=list) # Mudar
    
class Meta(models.Model):
    id_meta = models.AutoField(primary_key=True)
    meta = models.TextField(max_length=255)


def cadastrar_projeto(request):
    novo_projeto = Projeto()
    novo_projeto.nome = request.POST.get('nome')
    novo_projeto.preco = request.POST.get('preco')
    novo_projeto.dias = request.POST.get('dias')
    
    coordenadores = request.POST.get('coordenadores')
    projetistas = request.POST.get('projetistas')
    
    if coordenadores:
            novo_projeto.coordenadores = json.loads(coordenadores)
        
    if projetistas:
        novo_projeto.projetistas = json.loads(projetistas)
    
    novo_projeto.save()
    return  JsonResponse({
                'status': 'success',
                'nome': novo_projeto.nome,
                'preco': novo_projeto.preco,
                'dias': novo_projeto.dias,
                'coordenadores': novo_projeto.coordenadores,
                'projetistas': novo_projeto.projetistas
            })
        
def cadastrar_trainee(request):
    novo_trainee = Trainee()
    novo_trainee.nome = request.POST.get('nome')
    novo_trainee.idade = request.POST.get('idade')
    novo_trainee.curso = request.POST.get('curso')
    novo_trainee.semestre = request.POST.get('semestre')
    novo_trainee.save()
    return JsonResponse({
                'status': 'success',
                'nome': novo_trainee.nome,
                'idade': novo_trainee.idade,
                'curso': novo_trainee.curso,
                'semestre': novo_trainee.semestre
            })
    
def cadastrar_membro(request):
    novo_membro = Membro()
    novo_membro.nome = request.POST.get('nome')
    novo_membro.cargo = request.POST.get('cargo')
    novo_membro.projetos = []
    novo_membro.save()
    return JsonResponse({
                'status': 'success',
                'nome': novo_membro.nome,
                'cargo': novo_membro.cargo,
                'projetos': novo_membro.projetos
            })
    
def cadastrar_meta(request):
    nova_meta = Meta()
    nova_meta.meta = request.POST.get('meta')
    nova_meta.save()
    return JsonResponse({
                'status': 'success',
                'meta': nova_meta.meta,
            })