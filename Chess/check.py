from pieces import *
import copy

def Get_Position(Board, Color):
	for i in range(8):
		for j in range(8):
			#Checking For King
			if Board[i][j] == Color + "k":
				return [i, j]

def Check_Check(Board, Color):
	#Getting Position Of King
	Position = Get_Position(Board, Color)
	for j in range(8):
		for i in range(8):
			if Board[i][j] != "" and Board[i][j][0] != Color:
				#Checking It Is A Bishop
				if Board[i][j][1] == "b":

					#Creating Bishop Class
					Piece = Bishop(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A Rook
				elif Board[i][j][1] == "r":

					#Creating Rook Class
					Piece = Rook(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A Queen
				elif Board[i][j][1] == "q":

					#Creating Queen Class
					Piece = Queen(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A King
				elif Board[i][j][1] == "k":

					#Creating King Class
					Piece = King(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A Knight
				elif Board[i][j][1] == "n":

					#Creating Knight Class
					Piece = Knight(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A Pawn
				elif Board[i][j][1] == "p":

					#Creating Pawn Class
					Piece = Pawn(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()

				#Checking if King Is Check
				if Position in Piece.Valid_Moves:
					return True
	return False

def Check_Checkmate(Board, Color):
	for i in range(8):
		for j in range(8):
			if Board[i][j] != "" and Board[i][j][0] == Color:
				#Checking It Is A Bishop
				if Board[i][j][1] == "b":

					#Creating Bishop Class
					Piece = Bishop(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A Rook
				elif Board[i][j][1] == "r":

					#Creating Rook Class
					Piece = Rook(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A Queen
				elif Board[i][j][1] == "q":

					#Creating Queen Class
					Piece = Queen(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A King
				elif Board[i][j][1] == "k":

					#Creating King Class
					Piece = King(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A Knight
				elif Board[i][j][1] == "n":

					#Creating Knight Class
					Piece = Knight(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()
					

				#Checking It Is A Pawn
				elif Board[i][j][1] == "p":

					#Creating Pawn Class
					Piece = Pawn(None, Board, [], i, j, Board[i][j][0])
					Piece.Get_Valid_Moves()

				#Looping Valid Moves
				for i_move,j_move  in Piece.Valid_Moves:

					#Copying Board
					Temp_Board = copy.deepcopy(Board)
					Temp_Board[i][j],Temp_Board[i_move][j_move] = "", Temp_Board[i][j]
					#Checking It A Move Removes A Check
					if not Check_Check(Temp_Board,Color):
						return False
	return True
