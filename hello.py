import itertools
from flask import *
app=Flask(__name__)
@app.route('/')

class tictactoe():
	game=[[0,0,0],
		  [0,0,0],
		  [0,0,0]]

	def win(self):
		def all(l):
			if(l.count(l[0])==len(l) and l[0]!=0):
				return True
			else:
				return False
		# Horizontal
		for row in self.game:
			print(row)
			if all(row):
				print("Player",row[0],"is the winner horizontally!")
				return True

		# / Diagonal
		diag=[]
		for x,y in enumerate(reversed(range(len(self.game)))):
			diag.append(self.game[y][x])
		if all(diag):
				print("Player",diag[0],"is the winner Diagonally(/)!")
				return True

		# \ Diagonal
		diag=[]
		for z in range(len(self.game)):
			diag.append(self.game[z][z])
		if all(diag):
				print("Player",diag[0],"is the winner Diagonally(\\)!")
				return True

		# Vertical
		for col in range(len(self.game)):
			check=[]

			for row in self.game:
				check.append(row[col])
			if all(check):
				print("Player",check[0],"is the winner Vertically!")  
				return True 


	
	def game_board(self,player=0, row=0, column=0,just_display=False):
		try:
			if self.game[row][column]!=0:
				print("This is position is occupied!!!!!!!. Try another")
				return False
			print ("   "+"  ".join([str(i) for i in range(len(self.game))]))
			if not just_display:
				self.game[row][column]=player
			for count,row in enumerate(self.game):
				print (count,row)
			return True
		except Exception as e:
			print("Something went wrong",e)
			return False
		except IndexError as e:
			print("You might have entered position other than 0 1 or 2", e)
			return False  


g=tictactoe()
players_choice=itertools.cycle([1,2])
check=False
while not check:
	played=False
	while not played:
		current_player=next(players_choice)
		row_choice=int(input("Which row do you want to choose?(0,1,2): "))
		column_choice=int(input("Which column do you want to choose?(0,1,2): "))
		played=g.game_board(current_player,row_choice,column_choice)
		check=g.win()






