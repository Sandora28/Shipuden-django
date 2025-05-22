# ninja/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ninja,Mission
from .forms import NinjaForm, MissionForm, JutsuForm, TeamForm
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

@login_required
def ninja_update(request, pk):
    ninja = get_object_or_404(Ninja, pk=pk)
    form = NinjaForm(request.POST or None, instance=ninja)
    if form.is_valid():
        form.save()
        return redirect('ninja_detail', pk=pk)
    return render(request, 'ninja_form.html', {'form': form})

@login_required
def ninja_delete(request, pk):
    ninja = get_object_or_404(Ninja, pk=pk)
    if request.method == 'POST':
        ninja.delete()
        return redirect('ninja_list')
    return render(request, 'ninja_confirm_delete.html', {'ninja': ninja})

@login_required
def mission_create(request):
    if request.method == 'POST':
        form=MissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mission_list')
    else:
        form = MissionForm()
    return render(request,'mission_form.html',{'form': form})


def mission_detail(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    return render(request, 'mission_detail.html', {'mission': mission})

def mission_list(request):
    missions = Mission.objects.all()
    return render(request, 'mission_list.html', {'missions': missions})
@login_required
def mission_update(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    form = MissionForm(request.POST or None, instance=mission)
    if form.is_valid():
        form.save()
        return redirect('mission_detail', pk=pk)
    return render(request, 'mission_form.html', {'form': form})
@login_required
def mission_delete(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'POST':
        mission.delete()
        return redirect('mission_list')
    return render(request, 'mission_confirm_delete.html', {'mission': mission})



@login_required
def jutsu_create(request):
    if request.method == 'POST':
        form=JutsuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ninja_list')
    else:
        form = JutsuForm()
    return render(request,'jutsu_form.html',{'form': form})

def team_create(request):
    if request.method == 'POST':
        form=TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ninja_list')
    else:
        form = TeamForm()
    return render(request,'team_form.html',{'form': form})
