import random
class tictactoe():
 
        def __init__(self):
                self.game=[[0,0,0],
                               [0,0,0],
                               [0,0,0]]
                self.check=False
                self.flag=0
                self.player = 2
                self.turn=0
                self.state = 0
                self.score=-1000



        def change_player(self):
                self.player = 1 if self.player == 2 else 2


        def display(self,msg):
                if(msg=="winner"):
                        print("player {} has won!!!!".format(self.player))
                elif(msg=="filled"):
                        print("This is position is occupied!!!!!!!. Try another")
                elif(msg=="Draw"):
                        print("It is a Tie!!!!!")
                        self.score=0
                else:
                        print("Something went wrong",msg)
                


        def win(self, tree=False):
                def all(l):
                        if(l.count(l[0])==len(l) and l[0]!=0):
                                return True
                        else:
                                return False
                # Horizontal
                self.flag = 0
                for row in self.game:
                        #print(row)
                        if all(row):
                                #print("Player",row[0],"is the winner horizontally!")
                                if row[0]=='X':
                                        self.score=10
                                else:
                                        self.score=-10
                                if not tree:
                                        self.display("winner")
                                self.flag=1
                                #return True
                        

                # / Diagonal
                diag=[]
                for x,y in enumerate(reversed(range(len(self.game)))):
                        diag.append(self.game[y][x])
                if all(diag):
                        if diag[0]=='X':
                                self.score=10
                        else:
                                self.score=-10
                        if not tree:
                                self.display("winner")
                                #print("Player",diag[0],"is the winner Diagonally(/)!")
                        self.flag=1
                        #return True

                # \ Diagonal
                diag=[]
                for z in range(len(self.game)):
                        diag.append(self.game[z][z])
                if all(diag):
                        if diag[0]=='X':
                                self.score=10
                        else:
                                self.score=-10
                        if not tree:
                                self.display("winner")
                        self.flag=1
                        #print("Player",diag[0],"is the winner Diagonally(\\)!")
                        #return True
        

                # Vertical
                for col in range(len(self.game)):
                        check=[]

                        for row in self.game:
                                check.append(row[col])
                        if all(check):
                                if check[0]=='X':
                                        self.score=10
                                else:
                                        self.score=-10
                                if not tree:
                                        self.display("winner")
                                self.flag=1
                                #print("Player",check[0],"is the winner Vertically!")  
                                #return True


                print(self.flag, tree)
                if self.flag == 1:
                        if not tree:
                            self.state = self.player
                        return True

                draw = True
                for i in range(0,3):
                        for j in range(0,3):
                                if self.game[i][j]==0:
                                    draw = False

                print('draw ->', draw)
                if draw:
                        if not tree:
                            self.state = 3
                            self.display("Draw")
                        return True
 
                return False




                #if self.flag == 0:
                #self.flag=2
                #for i in range(0,3):
                #        for j in range(0,3):
                #                if self.game[i][j]==0:
                #                        self.flag=0
                #                        break
                #        if self.flag==0:
                #                break

                #print(tree, self.flag)
                #if(self.flag==0):
                #        return False
                #elif self.flag==2:
                #        if not tree:
                #            self.state = 3
                #            self.display("Draw")
                #        return True
                #else:
                #        if not tree:
                #            self.state = self.player
                #        #self.display("Draw")
                #        return True


        def print_gameboard(self):
                print ("   "+"  ".join([str(i) for i in range(len(self.game))]))
                for count,row in enumerate(self.game):

                        print (count,row)

        def ret_board(self):
                return self.game
        def game_board(self,row=0, column=0,display=True):
                try:
                        self.turn=0
                        if self.game[row][column]!=0:
                                self.display("filled")
                                #print("This is position is occupied!!!!!!!. Try another")
                                self.print_gameboard()
                                self.check = False
                                return False
                        #elif display:
                                #self.print_gameboard()
                        self.change_player()
                        if self.player == 1:
                                self.game[row][column]='O'
                                self.turn=1
                                if not display:
                                        self.print_gameboard()
                        elif self.player == 2:
                                self.game[row][column]='X'
                                if not display:
                                        self.print_gameboard()
                                self.turn=1
                        
                        self.check = self.win()
                        if(self.turn==1):
                                return True
                        else:
                                return False
                        #return True
                except Exception as e:
                        self.display(e);
                        self.print_gameboard()
                        self.check = False

        def evaluate(self):
                return self.score

        def chec(self):
                return self.check



class Bot(tictactoe):

        def __init__(self):
                super().__init__()


        def minimax(self,depth,isMax):
                self.score=-1000
                check_winner=self.win(tree=True)
                if check_winner==True:
                        result=self.evaluate()
                        return result
                        

                """if score==10:
                        return score
                if score==-10:
                        return score"""
                if isMax:
                        best=-1000
                        for i in range(0,3):
                                for j in range(0,3):
                                        if self.game[i][j]==0:
                                                self.game[i][j]='X'
                                                #Min turn
                                                best = max( best,self.minimax(depth+1, False) )
                                                self.game[i][j]=0
                        return best
                else:
                        best=1000
                        for i in range(0,3):
                                for j in range(0,3):
                                        if self.game[i][j]==0:
                                                self.game[i][j]='O'
                                                #Max turn
                                                best = min( best,self.minimax(depth+1, True) )
                                                self.game[i][j]=0
                        return best
        

        def FindBestMove(self):
                bestval=-1000
                row_b=-1
                col_b=-1
                for i in range(0,3):
                        for j in range(0,3):
                                if self.game[i][j]==0:
                                        self.game[i][j]='X'
                                        moveval=self.minimax(0,False)
                                        self.game[i][j]=0
                                        if moveval > bestval:
                                        
                                                row_b=i
                                                col_b=j
                                                bestval=moveval
                                        
                return row_b,col_b

        def bot(self):
                # minmax algo
                #r=random.choice([0,1,2])
                #c=random.choice([0,1,2])
                r,c=self.FindBestMove()
                return r,c 

        def play(self, row, col):
                response=True
                bot_res=True
                response=self.game_board(row,col,False)
                if self.chec():
                        return
                if response:
                        print("Bot's Turn")
                        row, col = self.bot()
                        bot_res=self.game_board(row,col,display=False)
                        while(bot_res==False):
                                row, col = self.bot()
                                bot_res=self.game_board(row,col,display=False)
                return
                 

if __name__ == '__main__':
        g=Bot()
        while g.chec()==False:
                #g.print_gameboard()
                row_choice=int(input("Which row do you want to choose?(0,1,2): "))
                column_choice=int(input("Which column do you want to choose?(0,1,2): "))
                g.play(row_choice, column_choice)

