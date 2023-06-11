from django import template
register = template.Library()


@register.simple_tag
def give_value(gameboard, row, col):
	return gameboard[row][col]
