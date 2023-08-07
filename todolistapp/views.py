from django.shortcuts import render, redirect
from .models import ToDos
from .forms import ToDosForm


# Create your views here.
def index(request):
    latest_todo_list = ToDos.objects.order_by("id")
    form = ToDosForm()
    if request.method == 'POST':
        form = ToDosForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        "latest_todo_list": latest_todo_list,
        'form': form
    }
    return render(request, 'todos/index.html', context)


def delete(request, id):
    todelete = ToDos.objects.get(id=id)
    todelete.delete()
    return redirect('/')
