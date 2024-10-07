from django.shortcuts import render
from .models import Usuario
from .models import Membro
from .models import Projeto
from .models import Trainee
from .models import Meta

# Create your views here.
def home(request):
    return render(request, "usuarios/home.html")

def usuarios(request):
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    usuarios = {
    'usuarios': Usuario.objects.all()
    }
    # Retorna os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)

def trainees(request):
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    trainees = {
    'trainees': Trainee.objects.all()
    }
    # Retorna os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/trainees.html', trainees)

def membros(request):
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    membros = {
    'membros': Membro.objects.all()
    }
    # Retorna os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/membros.html', membros)

def metas(request):
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    metas = {
    'metas': Meta.objects.all()
    }
    # Retorna os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/metas.html', metas)

def projetos(request):
    #Exibir todos os usuarios ja cadastrados em uma nova pagina
    projetos = {
    'projetos': Projeto.objects.all()
    }
    
    # Retorna os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/projetos.html', projetos,)

def cadastro_Projeto(request):
    #fazer select 
    coordenadores = Membro.objects.filter(cargo="Coordenador")
    projetistas = Membro.objects.filter(cargo="Projetista")
    
    # Verificar se os dados estão corretos
   
    
    #colocar resultado em variavel
    #mandar a variavel junto com o render
    return render(request, 'usuarios/cadastro_projeto.html', {'coordenadores': coordenadores, 'projetistas': projetistas })

def cadastro_trainee(request):
    return render(request, 'usuarios/cadastro_trainee.html')

def cadastro_membro(request):
    return render(request, 'usuarios/cadastro_membro.html')

def informacoes_gerais(request):
    return render(request, 'usuarios/informacoes_gerais.html')  

def cadastro_metas(request):
    return render(request, 'usuarios/cadastro_metas.html')

def sair_do_sistema(request):
    return render(request, 'usuarios/sair_do_sistema.html')

def dados_setor(request):
    # Aqui você deve substituir os valores abaixo pelos dados reais que deseja mostrar
    projetos = Projeto.objects.all()
    trainee = Trainee.objects.all()
    membro = Membro.objects.all()
    faturamento = 0
    for projeto in projetos:
        faturamento += projeto.preco
    
    projeto_por_membro = projetos.count()/membro.count()
    
    
    return render(request, 'usuarios/dados_setor.html', {
        'faturamento_total': faturamento,  # Exemplo de faturamento total
        'quantidade_projetos': projetos.count(),     
        'quantidade_trainees': trainee.count(),      # Exemplo de quantidade de trainees
        'quantidade_membros': membro.count(),       # Exemplo de quantidade total de membros
        'quantidade_projetos_por_membro': projeto_por_membro})


