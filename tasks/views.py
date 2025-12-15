from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    item_list = Todo.objects.filter(user=request.user).order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Task added successfully!")
            return redirect('todo')
    else:
        form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/home.html', page)

@login_required
def remove(request, item_id):
    item = get_object_or_404(Todo, id=item_id, user=request.user)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect('todo')
