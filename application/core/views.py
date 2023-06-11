from django.shortcuts import render, redirect

from django.http import HttpResponse
from core.utils import Bot
from django import template
register = template.Library()


def show_board(request):
	if 'game' not in request.session:
		request.session['game'] = Bot().__dict__

	GamePlay = Bot()
	GamePlay.__dict__ = request.session['game']
	row=0
	col=0
	msg = ''
	if GamePlay.state != 0:
		if GamePlay.state == 1:
			msg = 'You won!!!'
		elif GamePlay.state == 3:
			msg = 'Match drawn'
		else:
			msg = 'You lost'

	if request.method=='POST':
		row=int(request.POST.get('row'))
		column=int(request.POST.get('column'))
		
		GamePlay.play(row,column)
		request.session['game'] = GamePlay.__dict__
		return HttpResponse({'board': GamePlay.game})

	return render(request, "core/show_board.html",{"range": range(3),'gameboard':GamePlay.game, 'state':GamePlay.state, 'msg':msg})

def restart(request):
	request.session['game'] = Bot().__dict__
	return redirect('/core/play-game')

@register.filter
def give_value(gameboard,i,j):
	return gameboard[i][j]
