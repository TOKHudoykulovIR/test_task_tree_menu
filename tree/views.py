from django.shortcuts import render, get_object_or_404
from .models import Menu

# Create your views here.


def display_menu(request, id):
    menu = get_object_or_404(Menu, pk=id)
    context = {
        'menu_name': menu.name
    }
    return render(request, 'tree/display.html', context=context)


def list_menu(request):
    menu_list = Menu.objects.all()
    return render(request, 'tree/list_menu.html', {'menu_list': menu_list})