from django.views.generic import ListView
from django.shortcuts import render
from .models import CategoryMenu


class CategoryMenuListView(ListView):
    model = CategoryMenu
    template_name = "mymenu/menu_list.html"


def get_objects_menu(request, **kwargs):
    data = {}
    if request.method == 'GET':
        data['filter_menu'] = CategoryMenu.objects.filter(slug=kwargs['slug']).select_related('parent').prefetch_related('children').order_by('tree_id')
        filter_menu = data['filter_menu'][0]
        data['title'] = filter_menu.title
        data['categories'] = [i for i in filter_menu.posts.all()]
        data['parent'] = get_menu(filter_menu, punkt_list=[filter_menu])
        return render(request, 'mymenu/podmenu_list.html', context=data)


def get_menu(obj, punkt_list: list):
    if obj.parent:
        punkt_list.append(obj.parent)
        return get_menu(obj.parent, punkt_list)
    else:
        return punkt_list[::-1]


def get_my_menu(request, **kwargs):
    return render(request, 'mymenu/menu.html', {'slug': kwargs['slug']})
