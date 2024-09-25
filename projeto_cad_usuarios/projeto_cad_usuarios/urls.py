"""projeto_cad_usuarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),  # Login page
    path('signup/', views.signup, name='signup'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('sucesso/', views.sucesso, name='sucesso'),  # Success page after login
    path('adicionar-ao-carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover-do-carrinho/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]