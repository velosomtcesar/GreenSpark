from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password

PRODUTOS = {
    1: {'nome': 'Painel Solar', 'preco': 20000},
    2: {'nome': 'Turbina Eólica', 'preco': 50000},
    3: {'nome': 'Energia Geotérmica', 'preco': 70000},
}

def home(request):
    if request.method == 'POST':
        nome = request.POST.get('username')
        senha = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(nome=nome)
            if check_password(senha, usuario.senha):
                # Login successful, set session
                request.session['usuario_id'] = usuario.id_usuario
                return redirect('sucesso')
            else:
                messages.error(request, 'Senha incorreta')
        except Usuario.DoesNotExist:
            messages.error(request, 'Nome de usuário não encontrado')

    return render(request, 'usuarios/home.html')

def sucesso(request):
    if 'usuario_id' not in request.session:
        return redirect('home')  # Not logged in, redirect to login page

    produtos = PRODUTOS
    carrinho = request.session.get('carrinho', [])
    return render(request, 'usuarios/sucesso.html', {'produtos': produtos, 'carrinho': carrinho})

def adicionar_ao_carrinho(request, produto_id):
    if 'usuario_id' not in request.session:
        return redirect('home')  # Not logged in, redirect to login page

    produto = PRODUTOS.get(produto_id)
    carrinho = request.session.get('carrinho', [])

    carrinho.append({
        'id': produto_id,
        'nome': produto['nome'],
        'preco': produto['preco'],
    })

    request.session['carrinho'] = carrinho
    return redirect('sucesso')

def remover_do_carrinho(request, produto_id):
    if 'usuario_id' not in request.session:
        return redirect('home')  # Not logged in, redirect to login page

    carrinho = request.session.get('carrinho', [])
    carrinho = [item for item in carrinho if item['id'] != produto_id]

    request.session['carrinho'] = carrinho
    return redirect('sucesso')

def signup(request):
    # Your existing signup logic...
    # No changes needed here
    pass

def usuarios(request):
    # Your existing usuarios logic...
    # No changes needed here
    pass
