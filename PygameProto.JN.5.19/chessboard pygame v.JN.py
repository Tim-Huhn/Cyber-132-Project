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

        ###################
        # need to implement
        ###################
        # selected piece = piece
        # selected tile/piece = target
        # selected piece's original tile = fromTile
        # targetted tile = toTile
        def update(self, piece, fromTile):
            ## White/Black Pawn
            if (piece in white_group and piece in pawn_group):
                target, toTile = PawnMovement("white", fromTile)

                x,y = TileCords[toTile]
                all_sprite.remove(target)

                self.rect.x
                self.rect.y
            
            elif (piece in black_group and piece in pawn_group):
                target, toTile = PawnMovement("black", fromTile)
                self.rect.topleft = position

            ## White/Black Rook
            elif (piece in white_group and piece in rook_group):
                target, toTile = RookMovement("white", fromTile)
                self.rect.topleft = position
            
            elif (piece in black_group and piece in rook_group):
                target, toTile = RookMovement("black", fromTile)
                self.rect.topleft = position

            ## White/Black Knight
            elif (piece in white_group and piece in knight_group):
                target, toTile = KnightMovement("white", fromTile)
                self.rect.topleft = position
            
            elif (piece in black_group and piece in knight_group):
                target, toTile = KnightMovement("black", fromTile)
                self.rect.topleft = position

            ## White/Black Bishop
            elif (piece in white_group and piece in bishop_group):
                target, toTile = BishopMovement("white", fromTile)
                self.rect.topleft = position
            
            elif (piece in black_group and piece in bishop_group):
                target, toTile = BishopMovement("black", fromTile)
                self.rect.topleft = position

            ## White/Black Queen
            elif (piece in white_group and piece in queen_group):
                target, toTile = QueenMovement("white", fromTile)
                self.rect.topleft = position
            
            elif (piece in black_group and piece in queen_group):
                target, toTile = QueenMovement("black", fromTile)
                self.rect.topleft = position

            ## White/Black King
            elif (piece in white_group and piece in king_group):
                target, toTile = KingMovement("white", fromTile)
                self.rect.topleft = position
            
            elif (piece in black_group and piece in king_group):
                target, toTile = KingMovement("black", fromTile)
                self.rect.topleft = position


def PawnMovement(color, fromTile):
    availableMoves = []
    if (color == "white"):
        # Pawn First move condition
        if ("2" in fromTile):
            for i in range(1,3):
                toTile = fromTile.replace("2", str(2+i))
                if (TileSpace[toTile] == "e"): 
                    availableMoves.append(toTile)
                else:
                    break
        # Normal move condition
        else:
            toTile = fromTile.replace(fromTile[1], str(int(fromTile[1])+1))
            if (TileSpace[toTile] == "e"): 
                availableMoves.append(toTile)
            else:
                pass
    else:
        if ("7" in fromTile):
             for i in range(1,3):
                toTile = fromTile.replace("7", str(2+i))
                if (TileSpace[toTile] == "e"): 
                    availableMoves.append(toTile)
                else:
                    break
        else:
            toTile = fromTile.replace(fromTile[1], str(int(fromTile[1])-1))
            if (TileSpace[toTile] == "e"): 
                availableMoves.append(toTile)
            else:
                pass
    return availableMoves
    pass

def RookMovement(fromTile):
    availableMoves = []               

    # Move Down
    for i in range(int(fromTile[1])-1, 0, -1):
        toTile = fromTile.replace(fromTile[1], str(xAxis.index(xAxis[i])))
        if (TileSpace[toTile] == "e"): 
            availableMoves.append(toTile)
        else:
            break

    # Move Up
    for i in range(int(fromTile[1]), 8):
        toTile = fromTile.replace(fromTile[1], str(xAxis.index(xAxis[i])+1))
        if (TileSpace[toTile] == "e"): 
            availableMoves.append(toTile)
        else:
            break

    # Move Right
    tempIndex = xAxis.index(fromTile[0])
    for i in (xAxis[(tempIndex + 1):]):
        toTile = fromTile.replace(fromTile[0], i)
        if (TileSpace[toTile] == "e"):
            availableMoves.append(toTile)
        else:
            break

    # Move Left
    tempIndex = xReverse.index(fromTile[0])
    for i in (xReverse[(tempIndex + 1):]):
        toTile = fromTile.replace(fromTile[0], i)
        if (TileSpace[toTile] == "e"):
            availableMoves.append(toTile)
        else:
            break
        
    return availableMoves
##  pass

def KnightMovement(fromTile):
    availableMoves = []
    
    tempIndex = xAxis.index(fromTile[0])
    if (tempIndex + 2) <= 7:
        if ((int(fromTile[1]) + 1) <= 7):
            toTile = str(xAxis[(tempIndex + 2)] + str(int(fromTile[1])+1))
            if(TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                pass
            
        if ((int(fromTile[1]) - 1) >= 0):
            toTile = str(xAxis[(tempIndex + 2)] + str(int(fromTile[1])-1))
            if(TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                pass
            
    elif (tempIndex + 1) <= 7:
        if ((int(fromTile[1]) + 2) <= 7):
            toTile = str(xAxis[(tempIndex + 1)] + str(int(fromTile[1])+2))
            if(TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                pass
            
        if ((int(fromTile[1]) - 2) >= 0):
            toTile = str(xAxis[(tempIndex + 1)] + str(int(fromTile[1])-2))
            if(TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                pass
            
    elif (tempIndex - 2) >= 0:
        if ((int(fromTile[1]) + 1) <= 7):
            toTile = str(xAxis[(tempIndex - 2)] + str(int(fromTile[1])+1))
            if(TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                pass
            
        if ((int(fromTile[1]) - 1) >= 0):
            toTile = str(xAxis[(tempIndex - 2)] + str(int(fromTile[1])-1))
            if(TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                pass
            
    elif (tempIndex - 1) >= 0:
        if ((int(fromTile[1]) + 2) <= 7):
            toTile = str(xAxis[(tempIndex - 1)] + str(int(fromTile[1])+2))
            if(TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                pass
            
        if ((int(fromTile[1]) - 2) >= 0):
            toTile = str(xAxis[(tempIndex - 1)] + str(int(fromTile[1])-2))
            if(TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                pass
    
    return availableMoves
##    pass

def BishopMovement(fromTile):
    availableMoves = []
    
    # North-East Diagonal
    tempIndex = xAxis.index(fromTile[0])
    for i in (xAxis[(tempIndex + 1):]):
        toTile = str(i + str(xAxis.index(i) + 2))
        if (int(toTile[1]) <= 8):
            if (TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                break
        else:
            break
    
    # South=East Diagonal
    tempIndex = xAxis.index(fromTile[0])
    for i in (xAxis[(tempIndex + 1):]):
        if ((xReverse.index(i) - 1) >= 1):
            toTile = str(i + str(xReverse.index(i) - 1))
            if (TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                break
        else:
            break

    # North-West Diagonal
    tempIndex = xReverse.index(fromTile[0])
    for i in (xReverse[(tempIndex + 1):]):
        toTile = str(i + str(xReverse.index(i) - 1))
        if (int(toTile[1]) <= 8):
            if (TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                break
        else:
            break

    # South-West Diagonal
    tempIndex = xReverse.index(fromTile[0])
    for i in (xReverse[(tempIndex + 1):]):
        if ((xReverse.index(i) - 1) >= 1):
            toTile = str(i + str(xAxis.index(i) + 2))
            if (TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                break
        else:
            break
    
    return availableMoves
##    pass

def QueenMovement(fromTile):
    availableMoves = []
    
    # Move Down
    for i in range(int(fromTile[1])-1, 0, -1):
        toTile = fromTile.replace(fromTile[1], str(xAxis.index(xAxis[i])))
        if (TileSpace[toTile] == "e"): 
            availableMoves.append(toTile)
        else:
            break

    # Move Up
    for i in range(int(fromTile[1]), 8):
        toTile = fromTile.replace(fromTile[1], str(xAxis.index(xAxis[i])+1))
        if (TileSpace[toTile] == "e"): 
            availableMoves.append(toTile)
        else:
            break

    # Move Right
    tempIndex = xAxis.index(fromTile[0])
    for i in (xAxis[(tempIndex + 1):]):
        toTile = fromTile.replace(fromTile[0], i)
        if (TileSpace[toTile] == "e"):
            availableMoves.append(toTile)
        else:
            break

    # Move Left
    tempIndex = xReverse.index(fromTile[0])
    for i in (xReverse[(tempIndex + 1):]):
        toTile = fromTile.replace(fromTile[0], i)
        if (TileSpace[toTile] == "e"):
            availableMoves.append(toTile)
        else:
            break

    # North-East Diagonal
    tempIndex = xAxis.index(fromTile[0])
    for i in (xAxis[(tempIndex + 1):]):
        toTile = str(i + str(xAxis.index(i) + 2))
        if (int(toTile[1]) <= 8):
            if (TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                break
        else:
            break
    
    # South=East Diagonal
    tempIndex = xAxis.index(fromTile[0])
    for i in (xAxis[(tempIndex + 1):]):
        if ((xReverse.index(i) - 1) >= 1):
            toTile = str(i + str(xReverse.index(i) - 1))
            if (TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                break
        else:
            break

    # North-West Diagonal
    tempIndex = xReverse.index(fromTile[0])
    for i in (xReverse[(tempIndex + 1):]):
        toTile = str(i + str(xReverse.index(i) - 1))
        if (int(toTile[1]) <= 8):
            if (TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                break
        else:
            break

    # South-West Diagonal
    tempIndex = xReverse.index(fromTile[0])
    for i in (xReverse[(tempIndex + 1):]):
        if ((xReverse.index(i) - 1) >= 1):
            toTile = str(i + str(xAxis.index(i) + 2))
            if (TileSpace[toTile] == "e"):
                availableMoves.append(toTile)
            else:
                break
        else:
            break
    
    return availableMoves
##    pass

def KingMovement(fromTile):
    availableMoves = []

    # Move Up
    toTile = fromTile.replace(fromTile[1], str(int(fromTile[1])+1))
    if (TileSpace[toTile] == "e"): 
        availableMoves.append(toTile)
    else:
        pass

    # Move Down
    toTile = fromTile.replace(fromTile[1], str(int(fromTile[1])-1))
    if (TileSpace[toTile] == "e"): 
        availableMoves.append(toTile)
    else:
        pass

    # Move Right
    tempIndex = xAxis.index(fromTile[0])
    toTile = fromTile.replace(fromTile[0], xAxis[(tempIndex + 1)])
    if (TileSpace[toTile] == "e"): 
        availableMoves.append(toTile)
    else:
        pass

    # Move Left
    tempIndex = xAxis.index(fromTile[0])
    toTile = fromTile.replace(fromTile[0], xAxis[(tempIndex - 1)])
    if (TileSpace[toTile] == "e"): 
        availableMoves.append(toTile)
    else:
        pass

    # Move North-East
    tempIndex = xAxis.index(fromTile[0])
    toTile = str(xAxis[(tempIndex + 1)] + str(int(fromTile[1])+1))
    if (TileSpace[toTile] == "e"): 
        availableMoves.append(toTile)
    else:
        pass

    # Move South-East
    tempIndex = xAxis.index(fromTile[0])
    toTile = str(xAxis[(tempIndex + 1)] + str(int(fromTile[1])-1))
    if (TileSpace[toTile] == "e"): 
        availableMoves.append(toTile)
    else:
        pass

    # Move North-West
    tempIndex = xAxis.index(fromTile[0])
    toTile = str(xAxis[(tempIndex - 1)] + str(int(fromTile[1])+1))
    if (TileSpace[toTile] == "e"): 
        availableMoves.append(toTile)
    else:
        pass

    # Move South-West
    tempIndex = xAxis.index(fromTile[0])
    toTile = str(xAxis[(tempIndex - 1)] + str(int(fromTile[1])-1))
    if (TileSpace[toTile] == "e"): 
        availableMoves.append(toTile)
    else:
        pass
    

    
    return availableMoves
##    pass

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
                black_group.append(PieceID)
                pawn_group.append(PieceID)
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
                white_group.append(PieceID)
                pawn_group.append(PieceID)
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
                black_group.append(PieceID)
                rook_group.append(PieceID)
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
                white_group.append(PieceID)
                rook_group.append(PieceID)
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
                black_group.append(PieceID)
                knight_group.append(PieceID)
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
                white_group.append(PieceID)
                knight_group.append(PieceID)
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
                black_group.append(PieceID)
                bishop_group.append(PieceID)
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
                white_group.append(PieceID)
                bishop_group.append(PieceID)
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
        black_group.append(PieceID)
        queen_group.append(PieceID)
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
        white_group.append(PieceID)
        queen_group.append(PieceID)
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
        black_group.append(PieceID)
        king_group.append(PieceID)
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
        white_group.append(PieceID)
        king_group.append(PieceID)
        TileSpace[tile] = PieceID

##        for sprite in white_group:
##            print sprite
##
##        for sprite in black_group:
##            print sprite
##
##        for sprite in pawn_group:
##            print sprite
##
##        for sprite in rook_group:
##            print sprite
##
##        for sprite in knight_group:
##            print sprite
##
##        for sprite in bishop_group:
##            print sprite
##
##        for sprite in king_group:
##            print sprite
##
##        for sprite in queen_group:
##            print sprite

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

# lists for piece's movements
xAxis = ["A", "B", "C", "D", "E", "F", "G", "H"]
xReverse = ["H", "G", "F", "E", "D", "C", "B", "A"]

# get another list of X_Axis and Y_Axis keys
# + for right and - for left
X_list = sorted(X_Axis.keys())
# - for up and + for down
Y_list = sorted(Y_Axis.keys())
Y_list.reverse()

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

black_group = []
white_group = []

pawn_group = []
rook_group = []
knight_group = []
bishop_group = []
king_group = []
queen_group = []

# add pieces
DefaultPieces()

# since game hasn't started yet, these things should be set by default
mouseClicked = False

# main game loop, start playing
while True:
        # keep loop running at the right speed
        clock.tick(FPS)
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
                            
                            mouseClicked = True
                            print "A tile was clicked"
                            print tile
                            print piece
                            all_sprites.remove(ALL_PIECES[piece])
                            TileSpace[tile] = "e"
                        #PieceHolder = TilePressed(mousex, mousey, mouseClicked)

##                elif event.type == MOUSEBUTTONUP and mouseClicked == True:
##                        print "oh no"
##                        mouseClicked = False
##                        mousex, mousey = event.pos
##                        PieceHolder = TilePressed(mousex, mousey, mouseClicked)

        # Update
        ##all_sprites.update()
        
        # Draw / render
        Display()
        all_sprites.draw(DISPLAYSURF)
        # *after* drawing everything, flip the display
        pygame.display.flip()
    
