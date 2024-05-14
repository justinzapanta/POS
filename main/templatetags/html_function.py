from django.template import Library

register = Library()

@register.filter
def modulo(num):
    return num % 2