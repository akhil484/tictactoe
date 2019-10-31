import itertools
from flask import *
app=Flask(__name__)
@app.route('/')
def tictactoe():

	def win(current_game):
		def all(l):
			if(l.count(l[0])==len(l) and l[0]!=0):
				return True
			else:
				return False
		# Horizontal
		for row in game:
			print(row)
			if all(row):
				print("Player",row[0],"is the winner horizontally!")
				return True

		# / Diagonal
		diag=[]
		for x,y in enumerate(reversed(range(len(game)))):
			diag.append(game[y][x])
		if all(diag):
				print("Player",diag[0],"is the winner Diagonally(/)!")
				return True

		# \ Diagonal
		diag=[]
		for z in range(len(game)):
			diag.append(game[z][z])
		if all(diag):
				print("Player",diag[0],"is the winner Diagonally(\\)!")
				return True

		# Vertical
		for col in range(len(game)):
			check=[]

			for row in game:
				check.append(row[col])
			if all(check):
				print("Player",check[0],"is the winner Vertically!")  
				return True 


	def game_board(game_map,player=0, row=0, column=0,just_display=False):
		try:
			if game_map[row][column]!=0:
					print("This is position is occupied!!!!!!!. Try another")
					return game_map,False
			print ("   "+"  ".join([str(i) for i in range(len(game_map))]))
			if not just_display:
				game_map[row][column]=player
			for count,row in enumerate(game_map):
				print (count,row)
			return game_map,True
		except Exception as e:
			print("Something went wrong",e)
			return game_map,False
		except IndexError as e:
			print("You might have entered position other than 0 1 or 2", e)
			return game_map,False  

	play=True
	players=[1,2]

	while play:
		game_size=int(input("What size of tic tac toe do you want? "))
		game=[[0 for i in range(game_size)] for i in range(game_size)]
		game_won=False
		game,_=game_board(game,just_display=True)
		players_choice=itertools.cycle([1,2])


		while not game_won:
			current_player=next(players_choice)
			print("Current Player",current_player)
			played=False

			while not played:
				row_choice=int(input("Which row do you want to choose?(0,1,2): "))
				column_choice=int(input("Which column do you want to choose?(0,1,2): "))
				game,played=game_board(game,current_player,row_choice,column_choice)
			if win(game):
				game_won=True
				again=input("Do you want to play again: (y/n)?")
				if again.lower()=="y":
					print("restarting")
				else:
					print("Bye")
					play=False




