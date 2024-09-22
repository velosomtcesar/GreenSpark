from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
# Create your views here.

def home(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(nome=nome)  # Busca o usuário pelo nome
            if check_password(senha, usuario.senha):  # Verifica a senha hash
                # Se o nome de usuário e a senha forem válidos, redireciona para a página de sucesso
                return redirect('sucesso')
            else:
                messages.error(request, 'Senha incorreta')
        except Usuario.DoesNotExist:
            # Se o nome de usuário não for encontrado, exibe uma mensagem de erro
            messages.error(request, 'Nome de usuário não encontrado')

    return render(request, 'usuarios/home.html')

def signup(request):
    if request.method == 'POST':
        nome = request.POST.get('username')
        senha1 = request.POST.get('password1')
        senha2 = request.POST.get('password2')

        if senha1 != senha2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'usuarios/signup.html')

        senha_hash = make_password(senha1)  # Criptografa a senha
        novo_usuario = Usuario(nome=nome, senha=senha_hash)
        novo_usuario.save()

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('home')
    return render(request, 'usuarios/signup.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request,'usuarios/usuarios.html',usuarios)