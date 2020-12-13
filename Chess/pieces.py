import pygame
from settings import *
#Main Peices Class
class Peices():
	def __init__(self, Game_Window,  Box_List, Board, Color):
		#Making Valid Moves List
		self.Valid_Moves = []

		#Getting Color
		self.Color = Color
		#Game Window
		self.Game_Window = Game_Window
		#Boxes List
		self.Box_List = Box_List
		#Getting Board
		self.Board= Board

	#Showing Valid Moves
	def Show(self):

		#Iterating Throung Valid Moves List
		for i,j in self.Valid_Moves:
			#Changing Color
			self.Box_List[i][j] = pygame.draw.rect(self.Game_Window, (125,125,125), [Box_Size*i, Box_Size*j + Difference, Box_Size, Box_Size])

		return self.Box_List

#Bishop Classes
class Bishop(Peices):
	def __init__(self,Game_Window, Board, Box_List, x, y, Color):
		super().__init__(Game_Window, Box_List, Board, Color)
		#Getting Position
		self.x = x
		self.y = y
	def Get_Valid_Moves(self):
		#Setting Temporary Position
		x = self.x
		y = self.y
		#Getting Moves List
		Moves_Check = [(-1,-1), (1,1), (-1,1), (1,-1)]
		for i,j in Moves_Check:
			#Updating X And Y
			x +=i
			y +=j
			while  x>-1 and y>-1 and y<8 and x<8: 
				#Checking That Next Box is Empty
				if self.Board[x][y] == "":
					self.Valid_Moves.append([x,y])
					x +=i
					y +=j
				#Checking If Next Box is Of another Color
				elif self.Board[x][y][0] != self.Color:
					self.Valid_Moves.append([x,y])
					break
				else:
					break
			#Resetting Postion
			x = self.x
			y = self.y

#Knight Class
class Knight(Peices):
	def __init__(self,Game_Window, Board, Box_List, x, y, Color):
		super().__init__(Game_Window, Box_List, Board, Color)
		#Getting Position
		self.x = x
		self.y = y

	def Get_Valid_Moves(self):
		#Setting Temporary Position
		x = self.x
		y = self.y
		#Getting Moves List
		Moves_Check = [(-1,-2), (1,2), (-2,-1), (2,1), (-1,2), (1,-2), (-2,1), (2,-1)]
		for i,j in Moves_Check:
			#Updating X And Y
			x +=i
			y +=j
			if  x>-1 and y>-1 and y<8 and x<8: 
				#Checking That Next Box is Empty
				if self.Board[x][y] == "":
					self.Valid_Moves.append([x,y])
				#Checking If Next Box is Of another Color
				elif self.Board[x][y][0] != self.Color:
					self.Valid_Moves.append([x,y])
			#Resetting Postion
			x = self.x
			y = self.y

#Rook Classes
class Rook(Peices):
	def __init__(self,Game_Window, Board, Box_List, x, y, Color):
		super().__init__(Game_Window, Box_List, Board, Color)
		#Getting Position
		self.x = x
		self.y = y

	def Get_Valid_Moves(self):
		#Setting Temporary Position
		x = self.x
		y = self.y
		#Getting Moves List
		Moves_Check = [(0,1), (1,0), (-1,0), (0,-1)]
		for i,j in Moves_Check:
			#Updating X And Y
			x +=i
			y +=j
			while  x>-1 and y>-1 and y<8 and x<8: 
				#Checking That Next Box is Empty
				if self.Board[x][y] == "":
					self.Valid_Moves.append([x,y])
					x +=i
					y +=j
				#Checking If Next Box is Of another Color
				elif self.Board[x][y][0] != self.Color:
					self.Valid_Moves.append([x,y])
					break
				else:
					break
			#Resetting Postion
			x = self.x
			y = self.y

#Queen Class
class Queen(Peices):
	def __init__(self,Game_Window, Board, Box_List, x, y, Color):
		super().__init__(Game_Window, Box_List, Board, Color)
		#Getting Position
		self.x = x
		self.y = y

	def Get_Valid_Moves(self):
		#Setting Temporary Position
		x = self.x
		y = self.y
		#Getting Moves List
		Moves_Check = [(0,1), (1,0), (-1,0), (0,-1), (-1,-1), (1,1), (-1,1), (1,-1)]
		for i,j in Moves_Check:
			#Updating X And Y
			x +=i
			y +=j
			while  x>-1 and y>-1 and y<8 and x<8: 
				#Checking That Next Box is Empty
				if self.Board[x][y] == "":
					self.Valid_Moves.append([x,y])
					x +=i
					y +=j
				#Checking If Next Box is Of another Color
				elif self.Board[x][y][0] != self.Color:
					self.Valid_Moves.append([x,y])
					break
				else:
					break
			#Resetting Postion
			x = self.x
			y = self.y

#King Class
class King(Peices):
	def __init__(self,Game_Window, Board, Box_List, x, y, Color):
		super().__init__(Game_Window, Box_List, Board, Color)
		#Getting Position
		self.x = x
		self.y = y

	def Get_Valid_Moves(self):
		#Setting Temporary Position
		x = self.x
		y = self.y
		#Getting Moves List
		Moves_Check = [(0,1), (1,0), (-1,0), (0,-1), (-1,-1), (1,1), (-1,1), (1,-1)]
		for i,j in Moves_Check:
			#Updating X And Y
			x +=i
			y +=j
			if x>-1 and y>-1 and y<8 and x<8: 
				#Checking That Next Box is Empty
				if self.Board[x][y] == "":
					self.Valid_Moves.append([x,y])
					x +=i
					y +=j
				#Checking If Next Box is Of another Color
				elif self.Board[x][y][0] != self.Color:
					self.Valid_Moves.append([x,y])
			#Resetting Postion
			x = self.x
			y = self.y


#Pawn Class
class Pawn(Peices):
	def __init__(self,Game_Window, Board, Box_List, x, y, Color):
		super().__init__(Game_Window, Box_List, Board, Color)
		#Getting Position
		self.x = x
		self.y = y
		#List For  En Passant
		self.En_Passant = {}

	def Get_Valid_Moves(self):
		#Checking Pawn is Of Whinte
		if self.Color == "W":

			#Is It At Starting Position
			if self.y == 6:
				if self.Board[self.x][5] == "":
					self.Valid_Moves.append([self.x,5])
					if self.Board[self.x][4] == "":
						self.Valid_Moves.append([self.x,4])
			#Else Allowing It Only One Box
			else:
				if self.y -1 > -1:
					if self.Board[self.x][self.y-1] == "":
						self.Valid_Moves.append([self.x,self.y - 1])

			#Checking To Capture Pieces
			if self.y -1 > -1:
				if self.x - 1 > 0:
					if self.Board[self.x-1][self.y -1] != "" and self.Board[self.x-1][self.y -1][0] != self.Color:
						self.Valid_Moves.append([self.x -1,self.y - 1])

				if self.x + 1 < 8:
					if self.Board[self.x+1][self.y -1] != "" and self.Board[self.x+1][self.y -1][0] != self.Color:
						self.Valid_Moves.append([self.x +1,self.y - 1])
			#Checking For En Passant
			if self.y == 3:

				if self.Board[self.x-1][self.y] == "Bp" :
					self.Valid_Moves.append([self.x -1,self.y - 1])
					self.En_Passant[(self.x -1,self.y - 1)] = [self.x -1,self.y]

				elif self.Board[self.x+1][self.y] == "Bp" :
					self.Valid_Moves.append([self.x +1,self.y - 1])
					self.En_Passant[(self.x +1,self.y - 1)] = [self.x +1,self.y]

		#Checking Pawn is Of Black
		elif self.Color == "B":

			#Is It At Starting Position
			if self.y == 1:
				if self.Board[self.x][2] == "":
					self.Valid_Moves.append([self.x,2])
					if self.Board[self.x][3] == "":
						self.Valid_Moves.append([self.x,3])
			#Else Allowing It Only One Box
			else:
				if self.y + 1 < 8:
					if self.Board[self.x][self.y+1] == "":
						self.Valid_Moves.append([self.x,self.y + 1])

			#Checking To Capture Pieces
			if self.y + 1 < 8:
				if self.x - 1 > -1:
					if self.Board[self.x-1][self.y +1] != "" and self.Board[self.x-1][self.y +1][0] != self.Color:
						self.Valid_Moves.append([self.x -1,self.y +1])
				if self.x + 1 < 8:
					if self.Board[self.x+1][self.y +1] != "" and self.Board[self.x+1][self.y +1][0] != self.Color:
						self.Valid_Moves.append([self.x +1,self.y + 1])

			#Checking For En Passant
			if self.y == 4:

				if self.x-1 >-1 and self.Board[self.x-1][self.y] == "Wp":
					self.Valid_Moves.append([self.x -1,self.y + 1])
					self.En_Passant[(self.x -1,self.y + 1)] = [self.x -1,self.y]

				elif self.x+1 < 8 and self.Board[self.x+1][self.y] == "Wp" :
					self.Valid_Moves.append([self.x +1,self.y + 1])
					self.En_Passant[(self.x +1,self.y + 1)] = [self.x +1,self.y]
