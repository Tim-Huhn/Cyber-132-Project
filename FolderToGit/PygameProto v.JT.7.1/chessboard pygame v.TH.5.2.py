import pygame, sys
from pygame.locals import *

pygame.init()

# Screen Settings
WIDTH = 800
HEIGHT = 480
BoardDisplacement = (WIDTH-HEIGHT)/2
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
WHITE = (255, 255, 255)

# Background Pics
chessboardIMG = pygame.image.load('ChessBoardv2.jpg')
golfBackground = pygame.image.load('GreenBackground.gif')

# Chess Piece GIFs
WHITE_ROOK = pygame.image.load('white_rook.gif')
WHITE_QUEEN = pygame.image.load('white_queen.gif')
WHITE_PAWN = pygame.image.load('white_pawn.gif')
WHITE_KNIGHT = pygame.image.load('white_knight.gif')
WHITE_KING = pygame.image.load('white_king.gif')
WHITE_BISHOP = pygame.image.load('white_bishop.gif')

BLACK_ROOK = pygame.image.load('black_rook.gif')
BLACK_QUEEN = pygame.image.load('black_queen.gif')
BLACK_PAWN = pygame.image.load('black_pawn.gif')
BLACK_KNIGHT = pygame.image.load('black_knight.gif')
BLACK_KING = pygame.image.load('black_king.gif')
BLACK_BISHOP = pygame.image.load('black_bishop.gif')

# X-Axis Pixels
X_Axis = {"H":442,"G":384,"F":326,"E":268,"D":210,"C":152,"B":95,"A":37}

# Y-Axis Pixels set
Y_Axis = {"8":37,"7":95,"6":152,"5":210,"4":268,"3":326,"2":384,"1":442}

# Blank Tiles set
Tiles = {}

# Grid class aka Point class
class Grid(object):
    def __init__(self, x = 0, y = 0, i = 0, j = 0):
        self.x = x
        self.y = y
        self.i = i
        self.j = j

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = (value)
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = (value)

    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, value):
        self._i = (value)
    
    @property
    def j(self):
        return self._j

    @j.setter
    def j(self, value):
        self._j = (value)

    def __str__(self):
        return "{}{} = ({},{})".format(self.i, self.j, self.x, self.y)    

# Function to dsiplay the contents of the game
def Display():
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(golfBackground,(0, 0))
    DISPLAYSURF.blit(chessboardIMG,(BoardDisplacement, 0))
    DefaultPieces()

# Default placement of chess pieces
def DefaultPieces():
    # White/Black Pawn
    for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        z = (i + "7")
        DISPLAYSURF.blit(BLACK_PAWN,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))
        z = (i + "2")
        DISPLAYSURF.blit(WHITE_PAWN,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))

    # White/Black Rook
    for i in ["A", "H"]:
        z = (i + "8")
        DISPLAYSURF.blit(BLACK_ROOK,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))
        z = (i + "1")
        DISPLAYSURF.blit(WHITE_ROOK,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))

    # White/Black Knight
    for i in ["B", "G"]:
        z = (i + "8")
        DISPLAYSURF.blit(BLACK_KNIGHT,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))
        z = (i + "1")
        DISPLAYSURF.blit(WHITE_KNIGHT,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))

    # White/Black Bishop
    for i in ["C", "F"]:
        z = (i + "8")
        DISPLAYSURF.blit(BLACK_BISHOP,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))
        z = (i + "1")
        DISPLAYSURF.blit(WHITE_BISHOP,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))

    # White/Black Queen
    i = "D"
    z = (i + "8")
    DISPLAYSURF.blit(BLACK_QUEEN,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))
    z = (i + "1")
    DISPLAYSURF.blit(WHITE_QUEEN,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))

    # White/Black King
    i = "E"
    z = (i + "8")
    DISPLAYSURF.blit(BLACK_KING,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))
    z = (i + "1")
    DISPLAYSURF.blit(WHITE_KING,(BoardDisplacement + Tiles[z].x - 25, Tiles[z].y - 25))

    
# Prepare before starting the game
pygame.display.set_caption('Chessboard')

for i in X_Axis:
        for j in Y_Axis:
            Tiles[i+j] = Grid(X_Axis[i], Y_Axis[j], i, j)

Display()

# main game loop, start playing
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()
    pygame.display.update()

