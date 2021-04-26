from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def criar_produto(request):
    form = ProdutoForm(request.POST or None)    
    
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
        
    return render(request, 'produtos-form.html', {'form': form})
    
def update_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    
    return render(request, 'produtos-form.html', {'form': form, 'produto': produto})

def delete_produto(request, id):
    produto = Produto.objects.get(id=id)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    
    
    return render(request, 'prod-delete-confirm.html', { 'produto': produto})
    
    
    