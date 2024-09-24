from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


def home(request):
    if request.method == 'POST':
        nome = request.POST.get('username')  
        senha = request.POST.get('password')

        try:
           
            usuario = Usuario.objects.get(nome=nome)
            
            if check_password(senha, usuario.senha):
                
                return redirect('sucesso')
            else:
                messages.error(request, 'Senha incorreta')
        except Usuario.DoesNotExist:
            
            messages.error(request, 'Nome de usuário não encontrado')

    
    return render(request, 'usuarios/home.html')

def signup(request):
    if request.method == 'POST':
        
        nome = request.POST.get('nome') 
        senha1 = request.POST.get('password1')
        senha2 = request.POST.get('password2')

        
        if senha1 != senha2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'usuarios/signup.html')

        
        senha_hash = make_password(senha1)

        
        novo_usuario = Usuario(nome=nome, senha=senha_hash)
        novo_usuario.save()

        
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('home')  

    
    return render(request, 'usuarios/signup.html')

def usuarios(request):
    if request.method == 'POST':
        
        nome = request.POST.get('nome')

        if nome: 
            novo_usuario = Usuario(nome=nome)
            novo_usuario.save()
        else:
           
            return render(request, 'usuarios/usuarios.html', {'error': 'O campo nome é obrigatório.'})

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)

def sucesso(request):
    return render(request, 'usuarios/sucesso.html')
