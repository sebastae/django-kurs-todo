from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from list.forms import TodoItemForm
from list.models import TodoItem


def show(request):
    items = TodoItem.objects.all()
    d = {
        'head': "Head text",
        'body': "Moar text"
    }
    return render(request, 'list/all.html', {'items': items, 'dict':d})

def add(request):
    form = TodoItemForm()
    if request.method == "POST":
        form = TodoItemForm(request.POST)

        if form.is_valid():
            item = TodoItem(description=form.cleaned_data["description"])
            item.save()
            return HttpResponseRedirect(reverse('list:show'))


    context = {
        'form': form
    }

    return render(request, 'list/add.html', context)

def toggle_done(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.done = not item.done
    item.save()
    return HttpResponseRedirect(reverse('list:show'))

