from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def give_value(gameboard, row, col):
	text = '<span class="%s">%s</span>'%('yell' if gameboard[row][col]=='O' else 'red', gameboard[row][col])
	return mark_safe(text)
