""" custom template filter """
from django import template

# register custom filter filter
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    This function takes as parameters a bag item's price and a quantity and
    returns it's total
    """
    return price * quantity
