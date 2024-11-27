from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tasks = Task.objects.all()
    params = {'tasks': tasks}
    return render(request, 'tasks/index.html', params)

@login_required
def create(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskCreationForm()
    params = {'form': form}
    return render(request, 'tasks/create.html', params)

@login_required
def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    params = {'task': task}
    return render(request, 'tasks/detail.html', params)

@login_required
def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskCreationForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:detail', task_id=task.id)
    else:
        form = TaskCreationForm(instance=task)
    params = {'task': task, 'form': form}
    return render(request, 'tasks/edit.html', params)

@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    params = {'task': task}
    return render(request, 'tasks/delete.html', params)
