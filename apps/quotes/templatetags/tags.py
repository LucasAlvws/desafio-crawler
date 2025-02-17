from django import template

register = template.Library()

@register.filter(name="dataf")
def dataf(value):
    return value.strftime('%d/%m/%Y - %H:%M:%S') 

@register.filter(name="str")
def str(value):
    return str(value) 