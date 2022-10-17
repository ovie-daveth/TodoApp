from django.shortcuts import render,redirect
from tasks.forms import taskform
from .models import tasks


def task(request):
    form = taskform()
    if request.method == 'POST':
        form = taskform(request.POST)
        if form.is_valid():
            form.save();
            return redirect('/')
    context = {'form': form}
    return render(request, "task.html", context)

def home(request):
    task = tasks.objects.all()
    context = {'task': task}
    return render(request, "home.html", context)

def view(request, pk):
    task = tasks.objects.get(id=pk)
    context = {'task': task}
    return render (request, 'view.html', context)

def update(request, pk):
    task = tasks.objects.get(id=pk)
    form = taskform(instance=task)
    if request.method == 'POST':
        form = taskform(request.POST, instance=task)
        if form.is_valid():
            form.save();
            return redirect('/')
    context = {'form':form}
    return render(request, 'task.html', context)


def delete(request, pk):
    task = tasks.objects.get(id=pk)
    task.delete
    return redirect('/')

