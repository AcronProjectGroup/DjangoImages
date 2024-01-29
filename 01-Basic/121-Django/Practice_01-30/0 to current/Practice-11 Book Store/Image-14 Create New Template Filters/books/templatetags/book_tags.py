from django import template

register = template.Library()

# Create Custom lowercase
@register.filter
def To_lowerCase(value):
    return value.lower()














