from django.shortcuts import render
from .models import Todo
# Create your views here.



def home(request):
    tasks=Todo.objects.all
    a=len(Todo.objects.filter(Completed=False))
    return render(request,'home.html',{'tasks':tasks,'active1':"active",'a':a})

def Active(request):
    tasks=Todo.objects.filter(Completed=False)
    a=len(Todo.objects.filter(Completed=False))
    return render(request,'home.html',{'tasks':tasks,'active2':"active",'a':a})

def Completed(request):
    tasks=Todo.objects.filter(Completed=True)
    a=len(Todo.objects.filter(Completed=False))
    return render(request,'home.html',{'tasks':tasks,'active3':"active",'a':a})

def add(request):
    try:
        new=request.POST['task']
        t = Todo(task=new,Completed=False)
        t.save()
        a=len(Todo.objects.filter(Completed=False))
        tasks=Todo.objects.all
        return render(request,'home.html',{'tasks':tasks,'active1':"active",'a':a})
    except:
        tasks=Todo.objects.all
        a=len(Todo.objects.filter(Completed=False))
        return render(request,'home.html',{'tasks':tasks,'active1':"active",'a':a})

