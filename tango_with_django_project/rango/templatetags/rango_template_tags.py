from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
# is a decorator, passes the next function through register
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
            'act_cat': cat}
