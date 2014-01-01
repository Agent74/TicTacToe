from __future__ import print_function
from random import shuffle
import os, copy

def drawTable(listXO):
	os.system("clear")	
	for i in range(3):
		for j in range(3):
			if(listXO[i][j]==3):
				print("X",end=" ")
			elif(listXO[i][j]==5):
				print("O",end=" ")
			else:
				print("_",end=" ")
		print()

def markPos(val):
	print("Enter row position(1-3):")
	row=int(raw_input())-1
	print("Enter column position(1-3):")
	col=int(raw_input())-1
	if(listXO[row][col]==2):
		listXO[row][col]=val
		return True
	else:
		print("Position is already filled")
		return False

class tictacAI:
	def __init__(self, ai_mark, opp_mark):
		self.ai_mark = ai_mark
		self.opp_mark = opp_mark

	def Go(self, x, y, listXO, mark):
		listXO[x][y] = mark
		return True

	def make2(self, listXO):
		if(listXO[1][1] == 2):
			return self.Go(1,1,listXO,self.ai_mark)
		elif(listXO[0][1] == 2):
			return self.Go(0,1,listXO,self.ai_mark)
		elif(listXO[1][0] == 2):
			return self.Go(1,0,listXO,self.ai_mark)
		elif(listXO[1][2] == 2):
			return self.Go(1,2,listXO,self.ai_mark)
		elif(listXO[2][1] == 2):
			return self.Go(2,1,listXO,self.ai_mark)
		else:
			return False

	def posswin(self, listXO, mark):		
		for i in range(3):
			for j in range(3):
				listXO_copy = copy.deepcopy(listXO)
				if(listXO_copy[i][j] == 2):
					self.Go(i, j, listXO_copy, mark)
					win = checkWin(listXO_copy)
					if win==mark:
						return self.Go(i,j,listXO, self.ai_mark)
		return False

	def play(self, listXO, move):
		if move == 1:
			return self.Go(0,0, listXO, self.ai_mark)
		if self.posswin(listXO, self.ai_mark):
			return True
		if self.posswin(listXO, self.opp_mark):
			return True
		if self.make2(listXO):
			return True
		m = range(0,9)
		shuffle(m)
		for i in m:
			x = i/3
			y = i%3
			if(listXO[x][y] == 2):
				return self.Go(x, y, listXO, self.ai_mark)
		return False
		
def checkWin(listXO):
	for i in range(3):
		winr = 1	
		winc = 1	
		for j in range(3):
			winr *= listXO[i][j]
			winc *= listXO[j][i]
		if(winr==27 or winc==27):
			return 3
		elif(winr==125 or winc==125):
			return 5
	if(listXO[0][0]*listXO[1][1]*listXO[2][2] == 27 or listXO[0][2]*listXO[1][1]*listXO[2][0] == 27):
		return 3
	elif(listXO[0][0]*listXO[1][1]*listXO[2][2] == 125 or listXO[0][2]*listXO[1][1]*listXO[2][0] == 125):
		return 5
	return 0

if __name__=="__main__":
	listXO=[[2,2,2],[2,2,2],[2,2,2]]
	drawTable(listXO)
	gameOver = 0
	moveNo=1
	
	
	print("Do you want to be X or O:")
	human=3 if raw_input()=='X' else 5
	aiMark = 5 if human==3 else 3
	human_turn = 1 if human==3 else 0
	
	ai = tictacAI(aiMark, human)
	
	while((moveNo<10) and (gameOver == 0)):
		if(moveNo%2==human_turn):
			print("Your turn - \n")
			marked = markPos(human)
			if marked:
				drawTable(listXO)
				moveNo += 1
		else:
			ai.play(listXO, moveNo)
			drawTable(listXO)
			moveNo += 1
		
		gameOver = checkWin(listXO)
		if(gameOver==human):
			print("You Win")
		elif(gameOver==ai.ai_mark):
			print("Computer Wins")
		
	if(moveNo==10 and (gameOver == 0)):
		print("It's a draw")
