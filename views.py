from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        Item.objects.create(name=name, description=description)
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('/')

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('/')
    return render(request, 'edit.html', {'item': item})
