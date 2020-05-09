import pygame, sys
from pygame.locals import *

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
        PlacePiece(z, "BLACK_PAWN")
        z = (i + "2")
        PlacePiece(z, "WHITE_PAWN")

    # White/Black Rook
    for i in ["A", "H"]:
        z = (i + "8")
        PlacePiece(z, "BLACK_ROOK")
        z = (i + "1")
        PlacePiece(z, "WHITE_ROOK")

    # White/Black Knight
    for i in ["B", "G"]:
        z = (i + "8")
        PlacePiece(z, "BLACK_KNIGHT")
        z = (i + "1")
        PlacePiece(z, "WHITE_KNIGHT")

    # White/Black Bishop
    for i in ["C", "F"]:
        z = (i + "8")
        PlacePiece(z, "BLACK_BISHOP")
        z = (i + "1")
        PlacePiece(z, "WHITE_BISHOP")

    # White/Black Queen
    i = "D"
    z = (i + "8")
    PlacePiece(z, "BLACK_QUEEN")
    z = (i + "1")
    PlacePiece(z, "WHITE_QUEEN")

    # White/Black King
    i = "E"
    z = (i + "8")
    PlacePiece(z, "BLACK_KING")
    z = (i + "1")
    PlacePiece(z, "WHITE_KING")

# function to put an image on the board
def PlacePiece(tile, image):
    x,y = TileCords[tile]
    DISPLAYSURF.blit(PieceImages[image],(BoardDisplacement + Tiles[tile].x - 25, Tiles[tile].y - 25))
    TileSpace[tile] = image

# gets what tile the mouse clicks
def TilePosition(MX, MY):
    x = ""
    y = ""
    for i in range(0, 8):
        if (MX > XLeft[i] and MX < XRight[i]):
            x = X_keys[i]

        if (MY > YTop[i] and MY < YBottom[i]):
            y = Y_keys[i]
    if (x in X_keys and y in Y_keys):
        return x+y

# sees what to do based on what is in clicked tile
def TilePressed(MX, MY):
    # gets the tile that was clicked
    tile = TilePosition(MX, MY)
    # gets what is in the tile
    if tile in TileSpace.keys():
        piece = TileSpace[tile]
    else:
        piece = None

    ########
    # need to implement piece movement
    ########
    if piece in TileSpace.values():
        print piece
        

#######
# main
#######

PieceHolder = None

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

GREEN_DOT = pygame.image.load("green_dot.gif")

# adds images to dictionary
PieceImages = {}
PieceImages["WHITE_ROOK"] = WHITE_ROOK
PieceImages["WHITE_QUEEN"] = WHITE_QUEEN
PieceImages["WHITE_PAWN"] = WHITE_PAWN
PieceImages["WHITE_KNIGHT"] = WHITE_KNIGHT
PieceImages["WHITE_KING"] = WHITE_KING
PieceImages["WHITE_BISHOP"] = WHITE_BISHOP
PieceImages["BLACK_ROOK"] = BLACK_ROOK
PieceImages["BLACK_QUEEN"] = BLACK_QUEEN
PieceImages["BLACK_PAWN"] = BLACK_PAWN
PieceImages["BLACK_KNIGHT"] = BLACK_KNIGHT
PieceImages["BLACK_KING"] = BLACK_KING
PieceImages["BLACK_BISHOP"] = BLACK_BISHOP

# lists of values and keys of PieceImages


# X-Axis Pixels
X_Axis = {"H":442,"G":384,"F":326,"E":268,"D":210,"C":152,"B":95,"A":37}

# Y-Axis Pixels set
Y_Axis = {"8":37,"7":95,"6":152,"5":210,"4":268,"3":326,"2":384,"1":442}

# Blank Tiles set
Tiles = {}

# Boundry of tiles
XLeft = [160 + x - 25 for x in X_Axis.values()]
XRight = [160 + x + 25 for x in X_Axis.values()]
YTop = [x - 25 for x in Y_Axis.values()]
YBottom = [x + 25 for x in Y_Axis.values()]

# get list of X_Axis and Y_Axis keys
X_keys = X_Axis.keys()
Y_keys = Y_Axis.keys()

# cords to place a piece
TileCords = {}
for i in X_keys:
    for j in Y_keys:
        TileCords[i+j] = (XLeft[X_keys.index(i)], YTop[Y_keys.index(j)])

# dictionary of what's in a tile
TileSpace = {}
for i in X_keys:
    for j in Y_keys:
        TileSpace[i+j] = None

# Prepare before starting the game
pygame.display.set_caption('Chessboard')

for i in X_Axis:
        for j in Y_Axis:
            Tiles[i+j] = Grid(X_Axis[i], Y_Axis[j], i, j)


# setup board
Display()

# main game loop, start playing
while True:
    mouseClicked = False
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.display.update()
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseClicked = True
            TilePressed(mousex, mousey)
    pygame.display.update()

