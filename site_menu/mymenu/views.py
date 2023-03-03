from django.views.generic import ListView
from django.shortcuts import render
from .models import CategoryMenu


class CategoryMenuListView(ListView):
    model = CategoryMenu
    template_name = "mymenu/menu_list.html"


def get_my_menu(request, **kwargs):
    return render(request, 'mymenu/menu.html', {'slug': kwargs['slug']})
