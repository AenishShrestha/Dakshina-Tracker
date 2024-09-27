from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Dakshina
from .forms import DakshinaForm

@login_required
def dashboard(request):
    today = timezone.now().date()
    user_dakshinas = Dakshina.objects.filter(user=request.user).order_by('-date')
    leaderboard = Dakshina.objects.filter(date=today).order_by('-amount')
    
    context = {
        'user_dakshinas': user_dakshinas,
        'leaderboard': leaderboard,
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_dakshina(request):
    if request.method == 'POST':
        form = DakshinaForm(request.POST)
        if form.is_valid():
            dakshina = form.save(commit=False)
            dakshina.user = request.user
            dakshina.save()
            return redirect('dashboard')
    else:
        form = DakshinaForm()
    return render(request, 'tracker/add_dakshina.html', {'form': form})

@login_required
def edit_dakshina(request, pk):
    dakshina = get_object_or_404(Dakshina, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DakshinaForm(request.POST, instance=dakshina)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DakshinaForm(instance=dakshina)
    return render(request, 'tracker/edit_dakshina.html', {'form': form})

@login_required
def delete_dakshina(request, pk):
    dakshina = get_object_or_404(Dakshina, pk=pk, user=request.user)
    if request.method == 'POST':
        dakshina.delete()
        return redirect('dashboard')
    return render(request, 'tracker/delete_dakshina.html', {'dakshina': dakshina})