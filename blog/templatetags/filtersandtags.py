from django import template

register = template.Library()


@register.filter(name='cur')
def currency(value, name='руб.'):
    return f'{value} {name}'


@register.simple_tag
def lst(sep, *args):
    return sep.join(args) + f' итого: {len(args)}'



