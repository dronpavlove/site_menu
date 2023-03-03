from django import template
from mymenu.models import CategoryMenu
from django.http import HttpResponse

register = template.Library()


@register.inclusion_tag('mymenu/podmenu_list.html')
def get_menu(slug):
    try:
        data = dict()
        data['filter_menu'] = CategoryMenu.objects.filter(slug=slug).select_related(
            'parent').prefetch_related('children').order_by('tree_id')
        filter_menu = data['filter_menu'][0]
        data['title'] = filter_menu.title
        data['categories'] = [i for i in filter_menu.posts.all()]
        data['parent'] = get_objects_menu(filter_menu, punkt_list=[filter_menu])
        return data
    except:
        return HttpResponse('Нет такого пункта в меню', content_type="text/plain", status=400)


def get_objects_menu(obj, punkt_list: list):
    if obj.parent:
        punkt_list.append(obj.parent)
        return get_objects_menu(obj.parent, punkt_list)
    else:
        return punkt_list[::-1]

