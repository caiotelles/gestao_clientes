from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pessoas
from .forms import PessoaForm

# Create your views here.

@login_required
def pessoa_lista(request):
    pessoa = Pessoas.objects.all()
    return render(request, 'person.html', {'pessoas': pessoa})

@login_required
def pessoa_nova(request):
    form = PessoaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('pessoa_lista')
    return render(request, 'person_form.html', {'form': form})

@login_required
def pessoa_atualizar(request, id):
    pessoa = get_object_or_404(Pessoas, pk=id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('pessoa_lista')

    return render(request, 'person_form.html', {'form': form})

@login_required
def pessoa_deletar(request, id):
    pessoa = get_object_or_404(Pessoas, pk=id)
    form = PessoaForm(request.POST or None, request.FILES or None, instance=pessoa)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoa_lista')

    return render(request, 'pessoa_delete_confirm.html', {'form': form})

