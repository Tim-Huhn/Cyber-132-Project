import pygame
import sys
import Tkinter
from pygame.locals import *

# Function to dsiplay the contents of the game
def Display():
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(golfBackground,(0, 0))
    DISPLAYSURF.blit(chessboardIMG,(BoardDisplacement, 0))

# pieces class
class Pieces(pygame.sprite.Sprite):
        # constructor
        def __init__(self, piece, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = piece
            self.rect =self.image.get_rect()
            self.rect.topleft = position

        def update(self, fromTile, fromPiece, toTile, toPiece):
            if(fromPiece == "e" or fromPiece == None or toPiece != "e"):
                pass
            else:
                #FX,FY = TileCords[fromTile]
                TX,TY = TileCords[toTile]
                
                self.rect.x = TX
                self.rect.y = TY
                print fromPiece+" moves from "+fromTile+" to "+toTile+" and takes "+toPiece
                
                TileSpace[toTile] = fromPiece
                TileSpace[fromTile] = "e"

            # L is a letter / N is a number
##          L = tile[0]
##          N = tile[1]
##          # X-Axis Pixels
##          # X_Axis = {"H":442,"G":384,"F":326,"E":268,"D":210,"C":152,"B":95,"A":37}
##          # Y-Axis Pixels set
##          # Y_Axis = {"8":37,"7":95,"6":152,"5":210,"4":268,"3":326,"2":384,"1":442}
##          A = X_keys.index(L)
##          B = Y_keys.index(N)
            # L is a letter / N is a number
##          FL = fromTile[0]
##          FN = fromTile[1]
##          FA = X_keys.index(L)
##          FB = Y_keys.index(N)
##          if A < 8:
##              L = X_keys[A]
##              N = Y_keys[B]
##              tile = L+N
##              X,Y = TileCords[tile]
##                    
                

def getInput():
    fromSquareChosen = False
    toSquareChosen = False
    while (fromSquareChosen == False or toSquareChosen == False):
        #print "SQ1: ", fromSquareChosen, toSquareChosen
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()
        
            # when a tile is clicked, determine if piece is on tile
            # if a piece is on the clicked tile, confirm that a mouse button was clicked
            if event.type == MOUSEBUTTONDOWN:
                print "MBD"
                mousex, mousey = event.pos
                tile, piece = TilePressed(mousex, mousey)
                print "TP1: ", tile, piece
                if(piece == None):
                    pass
                elif (fromSquareChosen == False and toSquareChosen == False):
                    if (piece != "e"):
                        print "SQ1: ", fromSquareChosen, toSquareChosen
                        print "TP2: ", tile, piece
                        fromTile = tile
                        fromPiece = piece
                        fromSquareChosen = True
                        print "SQ2: ", fromSquareChosen, toSquareChosen
                elif (fromSquareChosen == True and toSquareChosen == False):
                    if (piece == "e"):
                        print "SQ3: ", fromSquareChosen, toSquareChosen
                        print "TP3: ", tile, piece
                        toTile = tile
                        toPiece = piece
                        toSquareChosen = True
                        print "SQ4: ", fromSquareChosen, toSquareChosen
                    elif (piece != "e"):
                        print "SQ5: ", fromSquareChosen, toSquareChosen
                        print "TP4: ", tile, piece
                        toTile = tile
                        toPiece = piece
                        takenPiece.append(toPiece)
                        toSquareChosen = True
                        print "SQ6: ", fromSquareChosen, toSquareChosen

    return fromTile,fromPiece,toTile,toPiece

# Default placement of chess pieces
def DefaultPieces():
        ## White/Black Pawn
        for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
                # black pawn
                tile = (i + "7")
                image = "BLACK_PAWN"
                x,y = TileCords[tile]
                print tile, image, x, y
                PieceID = image + "_" + i
                ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
                # add to sprites
                all_sprites.add(ALL_PIECES[PieceID])
                TileSpace[tile] = PieceID
                
                # white pawn
                tile = (i + "2")
                image = "WHITE_PAWN"
                x,y = TileCords[tile]
                print tile, image, x, y
                PieceID = image + "_" + i
                ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
                # add to sprites
                all_sprites.add(ALL_PIECES[PieceID])
                TileSpace[tile] = PieceID

        ## White/Black Rook
        for i in ["A", "H"]:
                # black rook
                tile = (i + "8")
                image = "BLACK_ROOK"
                x,y = TileCords[tile]
                print tile, image, x, y
                PieceID = image + "_" + i
                ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
                # add to sprites
                all_sprites.add(ALL_PIECES[PieceID])
                TileSpace[tile] = PieceID
                
                # white rook
                tile = (i + "1")
                image = "WHITE_ROOK"
                x,y = TileCords[tile]
                print tile, image, x, y
                PieceID = image + "_" + i
                ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
                # add to sprites
                all_sprites.add(ALL_PIECES[PieceID])
                TileSpace[tile] = PieceID

        ## White/Black Knight
        for i in ["B", "G"]:
                # black knight
                tile = (i + "8")
                image = "BLACK_KNIGHT"
                x,y = TileCords[tile]
                print tile, image, x, y
                PieceID = image + "_" + i
                ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
                # add to sprites
                all_sprites.add(ALL_PIECES[PieceID])
                TileSpace[tile] = PieceID
                
                # white knight
                tile = (i + "1")
                image = "WHITE_KNIGHT"
                x,y = TileCords[tile]
                print tile, image, x, y
                PieceID = image + "_" + i
                ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
                # add to sprites
                all_sprites.add(ALL_PIECES[PieceID])
                TileSpace[tile] = PieceID

        ## White/Black Bishop
        for i in ["C", "F"]:
                # black bishop
                tile = (i + "8")
                image = "BLACK_BISHOP"
                x,y = TileCords[tile]
                print tile, image, x, y
                PieceID = image + "_" + i
                ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
                # add to sprites
                all_sprites.add(ALL_PIECES[PieceID])
                TileSpace[tile] = PieceID
                
                # white bishop
                tile = (i + "1")
                image = "WHITE_BISHOP"
                x,y = TileCords[tile]
                print tile, image, x, y
                PieceID = image + "_" + i
                ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
                # add to sprites
                all_sprites.add(ALL_PIECES[PieceID])
                TileSpace[tile] = PieceID

        ## Black/White Queen
        i = "D"
        # black queen
        tile = (i + "8")
        image = "BLACK_QUEEN"
        x,y = TileCords[tile]
        print tile, image, x, y
        PieceID = image + "_" + i
        ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
        # add to sprites
        all_sprites.add(ALL_PIECES[PieceID])
        TileSpace[tile] = PieceID
        
        # white queen
        tile = (i + "1")
        image = "WHITE_QUEEN"
        x,y = TileCords[tile]
        print tile, image, x, y
        PieceID = image + "_" + i
        ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
        # add to sprites
        all_sprites.add(ALL_PIECES[PieceID])
        TileSpace[tile] = PieceID


        ## Black/White King
        i = "E"
        # black king
        tile = (i + "8")
        image = "BLACK_KING"
        x,y = TileCords[tile]
        print tile, image, x, y
        PieceID = image + "_" + i
        ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
        # add to sprites
        all_sprites.add(ALL_PIECES[PieceID])
        TileSpace[tile] = PieceID
        
        # white king
        tile = (i + "1")
        image = "WHITE_KING"
        x,y = TileCords[tile]
        print tile, image, x, y
        PieceID = image + "_" + i
        ALL_PIECES[PieceID] = Pieces(PieceImages[image],(x,y))
        # add to sprites
        all_sprites.add(ALL_PIECES[PieceID])
        TileSpace[tile] = PieceID

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

# sees what to do based on what is in clicked tile, returns what was on the tile
def TilePressed(MX, MY):
    # gets the tile that was clicked
    tile = TilePosition(MX, MY)
    # gets what is in the tile
    if tile in TileSpace.keys():
        piece = TileSpace[tile]
    else:
        piece = None

    return tile, piece


#######
# main
#######
# Initialie pygame
pygame.init()

# Screen Settings
WIDTH = 800
HEIGHT = 480
BoardDisplacement = (WIDTH-HEIGHT)/2
FPS = 30
WHITE = (255, 255, 255)

# Dictionary for every piece, DO NOT REMOVE WILL DESTABLIZE EVERYTHING
ALL_PIECES = {}
takenPiece = []


# X-Axis Pixels
X_Axis = {"H":442,"G":384,"F":326,"E":268,"D":210,"C":152,"B":95,"A":37}

# Y-Axis Pixels set
Y_Axis = {"8":37,"7":95,"6":152,"5":210,"4":268,"3":326,"2":384,"1":442}

# Boundry of tiles
XLeft = [BoardDisplacement + x - 25 for x in (X_Axis.values())]
XRight = [BoardDisplacement + x + 25 for x in (X_Axis.values())]
YTop = [x - 25 for x in (Y_Axis.values())]
YBottom = [x + 25 for x in (Y_Axis.values())]

# get list of X_Axis and Y_Axis keys
X_keys = (X_Axis.keys())
Y_keys = (Y_Axis.keys())

# cords to place a piece
TileCords = {}
for i in X_keys:
        for j in Y_keys:
                TileCords[i+j] = (XLeft[X_keys.index(i)], YTop[Y_keys.index(j)])
                
# dictionary of what's in a tile
TileSpace = {}
for i in X_keys:
        for j in Y_keys:
                TileSpace[i+j] = "e"

# create window
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Chessboard')
clock = pygame.time.Clock()

# images
# Background Pics
chessboardIMG = pygame.image.load('ChessBoardv2.jpg')
golfBackground = pygame.image.load('GreenBackground.gif')

# White Chess Piece GIFs
WHITE_ROOK = pygame.image.load('white_rook.gif')
WHITE_QUEEN = pygame.image.load('white_queen.gif')
WHITE_PAWN = pygame.image.load('white_pawn.gif')
WHITE_KNIGHT = pygame.image.load('white_knight.gif')
WHITE_KING = pygame.image.load('white_king.gif')
WHITE_BISHOP = pygame.image.load('white_bishop.gif')

# Black Chess Piece GIFs
BLACK_ROOK = pygame.image.load('black_rook.gif')
BLACK_QUEEN = pygame.image.load('black_queen.gif')
BLACK_PAWN = pygame.image.load('black_pawn.gif')
BLACK_KNIGHT = pygame.image.load('black_knight.gif')
BLACK_KING = pygame.image.load('black_king.gif')
BLACK_BISHOP = pygame.image.load('black_bishop.gif')

# Green dot to mark where a piece can move
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

# group of every sprite
all_sprites = pygame.sprite.Group()

# add pieces
DefaultPieces()

# since game hasn't started yet, these things should be set by default
mouseClicked = False
drawn = False

# main game loop, start playing
while True:
        # keep loop running at the right speed
        clock.tick(FPS)
##        if drawn == True:
##            # get input
##            fromTile,fromPiece,toTile,toPiece = getInput()
##            mouseClicked = True
##            print "A tile was clicked"
##            print tile
##            print piece
##            print fromTile,fromPiece,toTile,toPiece
##            #all_sprites.remove(ALL_PIECES[piece])
##            ALL_PIECES[piece].update(fromTile,fromPiece,toTile,toPiece)
        # Process input (events)
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        pygame.display.update()

                # when a tile is clicked, determine if piece is on tile
                # if a piece is on the clicked tile, confirm that a mouse button was clicked
                if event.type == MOUSEBUTTONDOWN:
                        mousex, mousey = event.pos
                        tile, piece = TilePressed(mousex, mousey)
                        if(piece == "e" or piece == None):
                            pass
                        else:
                            fromTile,fromPiece,toTile,toPiece = getInput()
                            mouseClicked = True
                            print "A tile was clicked"
                            #print tile
                            #print piece
                            print fromTile,fromPiece,toTile,toPiece
                            #all_sprites.remove(ALL_PIECES[piece])
                            ALL_PIECES[piece].update(fromTile,fromPiece,toTile,toPiece)
                            #TileSpace[fromTile] = "e"
                        #PieceHolder = TilePressed(mousex, mousey, mouseClicked)

##                elif event.type == MOUSEBUTTONUP and mouseClicked == True:
##                        print "oh no"
##                        mouseClicked = False
##                        mousex, mousey = event.pos
##                        PieceHolder = TilePressed(mousex, mousey, mouseClicked)

        # Update
        #all_sprites.update()
        
        # Draw / render
        Display()
        all_sprites.draw(DISPLAYSURF)
        # *after* drawing everything, flip the display
        pygame.display.flip()
##        drawn = True
    
