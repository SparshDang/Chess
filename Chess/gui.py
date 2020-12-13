import pygame
import settings
from pieces import *
import check
from time import sleep

pygame.init()

class Chess():
	def __init__(self):

		#Setting Board
		self.Board = settings.Board
		self.Last_Move = []

		self.Height = settings.Height
		self.Width = settings.Width
		self.Difference = settings.Difference

		#Current Turn
		self.Turn = "W"

		#Setting The Display
		self.Game_Window = pygame.display.set_mode((self.Width,self.Height))
		pygame.display.set_caption("Chess")
	
		#Definig Variable
		self.Game_Exit = False
		self.Game_Start = False
		self.Box_Size = settings.Box_Size
		self.Selected = False
		self.Check = False
		self.Checkmate = False
		self.Play_Font = pygame.font.SysFont(None, 72)
		self.Play_Text = self.Play_Font.render("PLAY", True, (255,0,0))
		self.Title_Font = pygame.font.SysFont(None, 70)

		self.Board_Box_List = []
		self.Title_Image = pygame.image.load("Images/All.png")
		self.Title_Image = pygame.transform.scale(self.Title_Image, (self.Width, int(self.Height/3))).convert_alpha()

		#Starting Game
		self.Game_Loop()
	
	#Function For Game Loop
	def Game_Loop(self):
	
		while not self.Game_Exit:
			if self.Game_Start:
				for event in pygame.event.get():
					#Ending Program On Exit
					if event.type == pygame.QUIT:
						self.Game_Exit = True

					#If Mouse Button Is Pressed
					elif event.type == pygame.MOUSEBUTTONDOWN:
	
						self.Settings_Game_Board_List()
						#Getting Position Of Click
						pos = event.pos

						x = pos[0]//self.Box_Size
						y = (pos[1] - self.Difference)//self.Box_Size

						#Changing Box Color
						self.Board_Box_List[int(x)][int(y)] = pygame.draw.rect(self.Game_Window, (255,0,0), [self.Box_Size*x, self.Box_Size*y + self.Difference, self.Box_Size, self.Box_Size] )

						#Checking If There Is Peice on Seleted Box					
						if self.Board[int(x)][int(y)] != "" and not self.Selected and self.Board[int(x)][int(y)][0] == self.Turn and not self.Checkmate:
							#Checking It Is A Bishop
							if self.Board[int(x)][int(y)][1] == "b":

								#Creating Bishop Class
								Piece = Bishop(self.Game_Window, self.Board, self.Board_Box_List, int(x), int(y), self.Board[int(x)][int(y)][0])
								Piece.Get_Valid_Moves()
								Piece.Show()

							#Checking It Is A Rook
							elif self.Board[int(x)][int(y)][1] == "r":
	
								#Creating Rook Class
								Piece = Rook(self.Game_Window, self.Board, self.Board_Box_List, int(x), int(y), self.Board[int(x)][int(y)][0])
								Piece.Get_Valid_Moves()
								Piece.Show()

							#Checking It Is A Queen
							elif self.Board[int(x)][int(y)][1] == "q":

								#Creating Queen Class
								Piece = Queen(self.Game_Window, self.Board, self.Board_Box_List, int(x), int(y), self.Board[int(x)][int(y)][0])
								Piece.Get_Valid_Moves()
								Piece.Show()

							#Checking It Is A King
							elif self.Board[int(x)][int(y)][1] == "k":
	
								#Creating King Class
								Piece = King(self.Game_Window, self.Board, self.Board_Box_List, int(x), int(y), self.Board[int(x)][int(y)][0])
								Piece.Get_Valid_Moves()
								Piece.Show()

							#Checking It Is A Knight
							elif self.Board[int(x)][int(y)][1] == "n":

								#Creating Knight Class
								Piece = Knight(self.Game_Window, self.Board, self.Board_Box_List, int(x), int(y), self.Board[int(x)][int(y)][0])
								Piece.Get_Valid_Moves()
								Piece.Show()

							#Checking It Is A Pawn
							elif self.Board[int(x)][int(y)][1] == "p":
	
								#Creating Pawn Class
								Piece = Pawn(self.Game_Window, self.Board, self.Board_Box_List, int(x), int(y), self.Board[int(x)][int(y)][0])
								Piece.Get_Valid_Moves()
								Piece.Show()

							#Making Self Selected True
							self.Selected = True


						#If A Piece Is Selected
						elif self.Selected:
							#If Move Is Valid
							if [int(x), int(y)] in Piece.Valid_Moves:
								#Checking If Piece Is Pawn
								if type(Piece) == Pawn:
									#Checking If Moves Is Of En Passant
									if (int(x), int(y)) in list(Piece.En_Passant.keys()):

										En_Passant = Piece.En_Passant[(int(x), int(y))]
										self.Board[En_Passant[0]][En_Passant[1]] = ""

								self.Last_Move = [Piece.x, Piece.y,int(x), int(y), self.Board[Piece.x][Piece.y], self.Board[int(x)][int(y)]]
								#Changing Position Of Piece
								self.Board[Piece.x][Piece.y],self.Board[int(x)][int(y)] = "", self.Board[Piece.x][Piece.y]

								if type(Piece) == Pawn:
									if self.Turn == "W":
										if Piece.y == 1:
											self.Board[int(x)][int(y)] = "Wq"
									elif self.Turn == "B":
										if Piece.y == 6:
											self.Board[int(x)][int(y)] = "Bq"

								#Checing For Invalid Moves
								if check.Check_Check(self.Board, self.Turn):

									self.Creating_Board()
									sleep(0.1)

									self.Board[Piece.x][Piece.y] = self.Last_Move[4]
									self.Board[self.Last_Move[2]][self.Last_Move[3]] = self.Last_Move[5]

									self.Creating_Board()

									self.Turn = "W" if self.Turn == "B" else "B"

								#Changing Turn
								self.Turn = "W" if self.Turn == "B" else "B"
	
								#Checking For Check
								if check.Check_Check(self.Board, self.Turn):
									self.Check = True
									#Checking Its Check
									if check.Check_Checkmate(self.Board, self.Turn):
										self.Checkmate = True
								else:
									self.Check = False

								#Checking If Its Stalemate
								if check.Check_Checkmate(self.Board, self.Turn):

									#Setting Title
									self.screen_text("Stalemate", self.Width/2 - 40, 45, (255,255,255))

							#Making Selected False
							self.Selected = False
						elif self.Checkmate:
							self.Reset()
							self.Game_Start = False


				self.Creating_Board()
			else:
				self.Home_Screen()
				for event in pygame.event.get():
					#Ending Program On Exit
					if event.type == pygame.QUIT:
						self.Game_Exit = True
					#If Button Was Clicked
					elif event.type == pygame.MOUSEBUTTONDOWN:
						pos = event.pos
						#Checking Button Is Pressed
						if self.Width/2 - self.Play_Text.get_width()/2 <= pos[0] <= self.Width/2 + self.Play_Text.get_width()/2  and self.Height/1.5< pos[1] < self.Height/1.5 + self.Play_Text.get_height():
							self.Game_Start = True

	#Home Screen
	def Home_Screen(self):
		self.Game_Window.fill((0,0,0))
		pygame.draw.rect(self.Game_Window, (255,255,255), [self.Width/2 - self.Play_Text.get_width()/2, self.Height/1.5, self.Play_Text.get_width(), self.Play_Text.get_height()])
		self.Game_Window.blit(self.Play_Text, [self.Width/2 - self.Play_Text.get_width()/2, self.Height/1.5,] )
		self.Game_Window.blit(self.Title_Image, [0, 0])

		pygame.display.update()

	#Function To Show Text On Screen
	def screen_text(self, text, x, y, Color):

		#Bliting Text
		text = pygame.font.SysFont(None, 55).render(text, True, Color)
		self.Game_Window.blit(text, [x,y])

	def Creating_Board(self):
		#Setting Game_Board
		if not self.Selected:
			self.Settings_Game_Board_List()
		#Setting Background
		pygame.draw.rect(self.Game_Window, (0,0,0), [0,0, self.Width, self.Difference])
		#Showing Color Of Board
		for i in self.Board_Box_List:
			for j in i:
				j

		#Bliting Text
		for i in range(len(self.Board)):
			for j in range(len(self.Board)):
				if self.Board[i][j] != "":
					piece = pygame.image.load('Images/' +self.Board[i][j] + '.png')
					piece = pygame.transform.scale(piece, (int(self.Box_Size), int(self.Box_Size))).convert_alpha()
					self.Game_Window.blit(piece, [i*self.Box_Size,j*self.Box_Size + self.Difference])

		#Setting Title
		if not self.Check:
				self.Title_Font_Text = self.Title_Font.render("White Turn" if self.Turn == "W" else "Black Turn", True, (255,255,255))
				self.Game_Window.blit(self.Title_Font_Text, [self.Width/2 - self.Title_Font_Text.get_width()/2, self.Height/12,] )
		elif self.Check:
				self.Title_Font_Text = self.Title_Font.render("CHECK", True, (255,0,0))
				self.Game_Window.blit(self.Title_Font_Text, [self.Width/2 - self.Title_Font_Text.get_width()/2, self.Height/12,] )
		elif self.Checkmate:
				self.Title_Font_Text = self.Title_Font.render("CHECK-MATE", True, (255,0,0))
				self.Game_Window.blit(self.Title_Font_Text, [self.Width/2 - self.Title_Font_Text.get_width()/2, self.Height/12,] )

			

		#Updating Display
		pygame.display.update()

	#Reseting Game Board Color
	def Settings_Game_Board_List(self):
		
		#Loop For Rows
		for i in range(8):
			#Appending Row To Board Box List
			self.Board_Box_List.append([])

			#Loop For Columns
			for j in range(8):
				#Drawing Rectangle 
				self.Board_Box_List[-1].append(pygame.draw.rect(self.Game_Window, (50,50,50) if (i + j)%2 == 1 else (255,255,255), [self.Box_Size*i, self.Box_Size*j + self.Difference, self.Box_Size, self.Box_Size] ))
	def Reset(self):
		self.Box_Size = settings.Box_Size
		self.Selected = False
		self.Check = False
		self.Checkmate = False
		self.Board = [["Br", "Bp", "", "" ,"", "", "Wp", "Wr"],
		["Bn", "Bp", "", "" ,"", "", "Wp", "Wn"],
		["Bb", "Bp", "", "" ,"", "", "Wp", "Wb"],
		["Bq", "Bp", "", "" ,"", "", "Wp", "Wq"],
		["Bk", "Bp", "", "" ,"", "", "Wp", "Wk"],
		["Bb", "Bp", "", "" ,"", "", "Wp", "Wb"],
		["Bn", "Bp", "", "" ,"", "", "Wp", "Wn"],
		["Br", "Bp", "", "" ,"", "", "Wp", "Wr"]]
		self.Turn = "W"

		

if __name__ == "__main__":
	Game = Chess()
