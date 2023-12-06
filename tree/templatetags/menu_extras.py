from django import template
from ..models import MenuItem, Menu

register = template.Library()


@register.inclusion_tag("tree/menu_template.html")
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_items = menu.items.filter(parent__isnull=True)
    return {'menu_items': menu_items, 'menu_name': menu_name}


@register.inclusion_tag("tree/menu_template.html")
def draw_menu_recursive(parent):
    child_items = parent.children.all()
    return {'menu_items': child_items}
