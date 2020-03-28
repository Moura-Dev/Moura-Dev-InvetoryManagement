from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'index.html')



def display_notebook(request):
    items = Notebook.objects.all()
    context = {
        'items' : items,
        'header' : "Notebooks"

    }
    return render(request, 'index.html', context)


def display_computador(request):
    items = Computador.objects.all()
    context = {
        'items' : items,
        'header': "Computadores"

    }
    return render(request, 'index.html', context)



def display_celular(request):
    items = Celular.objects.all()
    context = {
        'items' : items,
        'header': "Celulares"

    }
    return render(request, 'index.html', context)



def add_dispositivo(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_notebook(request):
    return add_dispositivo(request, NotebookForm)


def add_computador(request):
    return add_dispositivo(request, ComputadorForm)

def add_celular(request):
     return add_dispositivo(request, CelularForm)


def edit_dispositivo(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)


    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})



def edit_notebook(request, pk):
    return edit_dispositivo(request, pk, Notebook, NotebookForm)

def edit_computador(request, pk):
    return edit_dispositivo(request, pk, Computador, ComputadorForm)


def edit_celular(request, pk):
    return edit_dispositivo(request, pk, Celular, CelularForm)




def delete_notebook(request, pk):

    Notebook.objects.filter(id=pk).delete()

    items = Notebook.objects.all()

    context = {
        'items': items
    }

    return render (request, 'index.html', context)



def delete_computador(request, pk):

    Computador.objects.filter(id=pk).delete()

    items = Computador.objects.all()

    context = {
        'items': items
    }

    return render (request, 'index.html', context)



def delete_celular(request, pk):

    Celular.objects.filter(id=pk).delete()

    items = Celular.objects.all()

    context = {
        'items': items
    }

    return render (request, 'index.html', context)