from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views for creating, updating, deleting and listing tasks


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_task')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


def list_task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list_task.html', {'tasks': tasks})


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_task')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/update_task.html', {'form': form, 'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('list_task')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_task')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
