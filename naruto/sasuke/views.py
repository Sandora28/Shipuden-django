# ninja/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ninja
from .forms import NinjaForm
from django.contrib.auth.decorators import login_required

import templates
def ninja_list(request):
    ninjas = Ninja.objects.all()
    return render(request, 'ninja_list.html', {'ninjas': ninjas})

def ninja_detail(request, pk):
    ninja = get_object_or_404(Ninja, pk=pk)
    return render(request, 'ninja_detail.html', {'ninja': ninja})

@login_required
def ninja_create(request):
    if request.method == 'POST':
        form = NinjaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ninja_list')
    else:
        form = NinjaForm()
    return render(request, 'ninja_form.html', {'form': form})

def ninja_update(request, pk):
    ninja = get_object_or_404(Ninja, pk=pk)
    form = NinjaForm(request.POST or None, instance=ninja)
    if form.is_valid():
        form.save()
        return redirect('ninja_detail', pk=pk)
    return render(request, 'ninja_form.html', {'form': form})

def ninja_delete(request, pk):
    ninja = get_object_or_404(Ninja, pk=pk)
    if request.method == 'POST':
        ninja.delete()
        return redirect('ninja_list')
    return render(request, 'ninja_confirm_delete.html', {'ninja': ninja})
