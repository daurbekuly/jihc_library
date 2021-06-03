from django import template

from ebook.models import *

register = template.Library()


@register.simple_tag
def get_books():
    return Book.objects.all()



