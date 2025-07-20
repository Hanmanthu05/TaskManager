from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    tasks = []
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user = request.user) 
    return render(request,'index.html',{'tasks':tasks})

@login_required
def add_task(request):
    added_ = None
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                added_ = task
                messages.success(request, f'Task "{task.title}" added successfully!')
                return redirect('addTask')
    
    else:
        form = TaskForm() 
    return render(request,'add_task.html',{'form':form,
                                           'added':added_})   


def task_list(request):
    tasks = []
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-added_date') 
    return render(request,'task_list.html',{'tasks':tasks})


def completed(request):
     tasks = []
     if request.user.is_authenticated:
        tasks = Task.objects.filter(completed=True,user=request.user)
     return render(request,'completed.html',{'tasks':tasks})
     


@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id,user = request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('listTask')
       
    return render(request,'delete.html',{'task':task})


@login_required
def update_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id,user = request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task "{task.title}" is edited successfully.')
            return redirect('updateTask',task_id)
    else:
        form = TaskForm(instance=task)
    return render(request,'edit_task.html',{'form':form })


def pending(request):
    tasks = []
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user,completed=False)
    return render(request,'pending_task.html',{'tasks':tasks})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('Home')
            
    else:
        form = UserRegistrationForm()

    return render(request,'registration/register.html',{'form':form})



@login_required
def profile(request):
    user = request.user
    return render(request,'profile.html',{'user':user})
