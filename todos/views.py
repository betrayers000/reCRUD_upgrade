from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')

def create(request):
    author = request.POST.get("author")
    title = request.POST.get("title")
    content = request.POST.get("content")
    due_date = request.POST.get("due-date")
    
    todo = Todo.objects.create(
        author=author, 
        title=title, 
        content=content, 
        due_date=due_date
        )
    return redirect('todos:index')


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todos:index')
    
def add(request):
    if request.method == "POST":
        author = request.POST.get("author")
        title = request.POST.get("title")
        content = request.POST.get("content")
        due_date = request.POST.get("due-date")
    
        todo = Todo.objects.create(
            author=author, 
            title=title, 
            content=content, 
            due_date=due_date
            )
        return redirect('todos:index')
    else:
        return render(request, 'add.html')
