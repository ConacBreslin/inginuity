"""File to calculate sub total"""
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """calculate subtotal of order"""
    return price * quantity
