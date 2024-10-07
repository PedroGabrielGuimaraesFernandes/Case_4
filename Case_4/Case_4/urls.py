"""
URL configuration for Case_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_Case_4 import views
from app_Case_4 import models

urlpatterns = [
    # path('admin/', admin.site.urls),
    #Case4.com
    path('', views.home, name="home"),
    #Case4.com/usuarios
    path('usuarios/', views.usuarios, name = 'listagem_usuarios'),
    
    path('trainees/', views.trainees, name = 'listagem_trainees'),
    
    path('membros/', views.membros, name = 'listagem_membros'),
    
    path('metas/', views.metas, name = 'listagem_metas'),
    
    path('projetos/', views.projetos, name = 'listagem_projetos'),
    
    path('add/', models.cadastrar_membro, name = 'cadastrar_membro'),
    
    path('cadastrar_trainee/', views.cadastro_trainee, name = 'cadastro_trainee'),

    path('add_trainee/', models.cadastrar_trainee, name = 'cadastrar_trainee'),

    path('cadastrar_projeto/', views.cadastro_Projeto, name = 'cadastro_projeto'),

    path('add_projeto/', models.cadastrar_projeto, name = 'cadastrar_projeto'),
    
    path('cadastrar_membro/', views.cadastro_membro, name = 'cadastro_membro'),

    path('add_membro/', models.cadastrar_membro, name = 'cadastrar_membro'),

    path('informacoes_gerais/', views.informacoes_gerais, name = 'informacoes_gerais'),

    path('cadastrar_metas/', views.cadastro_metas, name='cadastro_metas'),
    
    path('add_meta/', models.cadastrar_meta, name = 'cadastrar_meta'),

    path('sair_do_sistema/', views.sair_do_sistema, name='sair_do_sistema'),

    path('dados_setor/', views.dados_setor, name='dados_setor'),
    ]
