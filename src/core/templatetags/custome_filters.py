from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter(name='striphtml')
def strip_html_tags(value):
    return strip_tags(value)