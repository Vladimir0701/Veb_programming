

from django import template
from blog.models import Category

register = template.Library()

# Это декаратор функции показа меню
# Чтобы связать эту функцию с тегом используется декоратор доступный через переменную register

@register.inclusion_tag('blog/menu_tpl.html')

def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}