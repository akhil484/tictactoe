import itertools

class tictactoe():
 
	def __init__(self):
		self.game=[[0,0,0],
			       [0,0,0],
			       [0,0,0]]
		self.check=False
		self.flag=0


	def display(self,msg):
		if(msg=="winner"):
			print("We have a winner!!!!")
		elif(msg=="filled"):
			print("This is position is occupied!!!!!!!. Try another")
		else:
			print("Something went wrong",msg)
		


	def win(self):
		def all(l):
			if(l.count(l[0])==len(l) and l[0]!=0):
				return True
			else:
				return False
		# Horizontal
		for row in self.game:
			#print(row)
			if all(row):
				#print("Player",row[0],"is the winner horizontally!")
				self.display("winner")
				self.flag=1
				return True
			

		# / Diagonal
		diag=[]
		for x,y in enumerate(reversed(range(len(self.game)))):
			diag.append(self.game[y][x])
		if all(diag):
			self.display("winner")
				#print("Player",diag[0],"is the winner Diagonally(/)!")
			self.flag=1
			return True

		# \ Diagonal
		diag=[]
		for z in range(len(self.game)):
			diag.append(self.game[z][z])
		if all(diag):
			self.display("winner")
			self.flag=1
				#print("Player",diag[0],"is the winner Diagonally(\\)!")
			return True
	

		# Vertical
		for col in range(len(self.game)):
			check=[]

			for row in self.game:
				check.append(row[col])
			if all(check):
				self.display("winner")
				self.flag=1
				#print("Player",check[0],"is the winner Vertically!")  
				return True
		if(self.flag==0):
			return False



	def print_gameboard(self):
		print ("   "+"  ".join([str(i) for i in range(len(self.game))]))
		for count,row in enumerate(self.game):

			print (count,row)



	def game_board(self,row=0, column=0,just_display=False):
		try:
			if self.game[row][column]!=0:
				self.display("filled")
				#print("This is position is occupied!!!!!!!. Try another")
				self.check = False
			if not just_display:
				self.game[row][column]=1
			self.print_gameboard()
			#return True
			self.check = self.win()
		except Exception as e:
			self.display(e);
			self.print_gameboard()
			self.check = False


	def chec(self):
		return self.check


g=tictactoe()
while g.chec()==False:
	row_choice=int(input("Which row do you want to choose?(0,1,2): "))
	column_choice=int(input("Which column do you want to choose?(0,1,2): "))
	g.game_board(row_choice,column_choice)



"""class Bot(tictactoe):

	def __init__(self):
		super(self)

	def bot()
		self.game
		self.player_choice
		# bot logic <- random """


