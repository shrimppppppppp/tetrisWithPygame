import pygame 
import time
import random
import pieceModel

# Khoi tao cac thu 

pygame.init()
surface = pygame.display.set_mode((1000, 1000))
bg = pygame.image.load('migu.png').convert(24)
myfont = pygame.font.SysFont("Comic Sans MS", 30)
label = myfont.render("Your score UwU: ", 1, (255, 255, 0))

playerScore = 0
currentX = 250
currentY = 100
currentRotation = 0
maxI = [450, 300]
maxZ = [350, 400]
maxO = [400]

grid = [[0 for x in range(15)] for y in range(25)]

##############################################################################
class __init__:
    
    def drawGridAfter(surface):
        for i in range(20):
            for j in range(10):
                if grid[i][j] == 1:
                    print(i, j)
                    pygame.draw.rect(surface, (0, 0, 255), [j * 50, i * 50, 50, 50], 0)

    def drawGrid(surface):
        blockSize = 50
        for x in range(0, 500, blockSize):
            for y in range(0, 1000, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(surface, (255, 255, 255), rect, 1)
    
    def drawPiece(surface, piece, x, y, rotation):
        __init__.drawGrid(surface)
        for i in range(len(piece[rotation])):
            for j in range(len(piece[rotation][i])):
                if piece[rotation][i][j] == 1:
                    pygame.draw.rect(surface, (0, 0, 255), [x + j * 50, y + i * 50, 50, 50], 0)
    
    def drawCurrentPiece(surface):
        pygame.draw.rect(surface, (0, 0, 255), [700, 50, 300, 475], 2)

##############################################################################

class scoreUpdate:
    def updateScore(score):
        score += 1
        return score

    def printScore(surface, myfont, score):
        showScore = myfont.render(str(score), 1, (255, 255, 0))
        surface.blit(showScore, (975, 5))

##############################################################################

class pieceBehavior:

    def pickPiece():
        return random.choice([pieceModel.pieceI, pieceModel.pieceZ, pieceModel.pieceO, pieceModel.pieceL, pieceModel.pieceT, pieceModel.pieceJ])

    def processPiece(surface, piece, rotation, currentX, currentY):
        surface.blit(bg, (0, 0))
        surface.blit(label, (700, 5))
        __init__.drawGrid(surface)
        __init__.drawGridAfter(surface)
        __init__.drawCurrentPiece(surface)
        __init__.drawPiece(surface, piece, currentX, currentY, rotation)
        __init__.drawPiece(surface, currentPiece, 800, 100, currentRotation)

    def changeGrid(surface, piece, rotation, currentX, currentY):
            for i in range(len(piece[rotation])):
                for j in range(len(piece[rotation][i])):
                    if piece[rotation][i][j] == 1:
                        grid[(currentY + i * 50) // 50][(currentX + j * 50) // 50] = 1
            return grid 

    def checkLimitX(piece, rotation, currentX):
        if (piece == pieceModel.pieceI and currentX > maxI[rotation]): 
            currentX = maxI[rotation]
        if (piece == pieceModel.pieceZ and currentX > maxZ[rotation]):
            currentX = maxZ[rotation]
        if (currentX < 0):
            currentX = 0
        return currentX

    def checkLimitY(currentPiece, currentRotation, currentX, currentY):
        if (currentY > 1000 - len(currentPiece[currentRotation]) * 50):
            currentY = 0
            currentPiece = pieceBehavior.pickPiece()
            currentX = 250
            currentY = 0
            currentRotation = 0
            
        return currentPiece, currentRotation, currentX, currentY

    def changeRotation(piece, rotation, currentX):
        if (rotation == len(piece) - 1):
            rotation = 0
        else:
            rotation += 1
        currentX = pieceBehavior.checkLimitX(piece, rotation, currentX)
        return currentX, rotation

##############################################################################

# Main loop
currentPiece = pieceBehavior.pickPiece()
while True:
    # pygame.display.update() 
    __init__.drawGridAfter(surface)
    if (currentY > 1000 - len(currentPiece[currentRotation]) * 50):
        grid = pieceBehavior.changeGrid(surface, currentPiece, currentRotation, currentX, 1000 - len(currentPiece[currentRotation]) * 50)
    currentPiece, currentRotation, currentX, currentY = pieceBehavior.checkLimitY(currentPiece, currentRotation, currentX, currentY)

    # # print(grid)
    pieceBehavior.processPiece(surface, currentPiece, currentRotation, currentX, currentY)
    # changeRotation(pieceZ, currentRotation) 
    for event in pygame.event.get(): 
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_LEFT):
                currentX -= 50
                currentX = pieceBehavior.checkLimitX(currentPiece, currentRotation, currentX)
                pieceBehavior.processPiece(surface, currentPiece, currentRotation, currentX, currentY)
            if (event.key == pygame.K_RIGHT):
                currentX += 50
                currentX = pieceBehavior.checkLimitX(currentPiece, currentRotation, currentX)
                pieceBehavior.processPiece(surface, currentPiece, currentRotation, currentX, currentY)
            if (event.key == pygame.K_UP):
                currentX, currentRotation = pieceBehavior.changeRotation( currentPiece, currentRotation, currentX)
                pieceBehavior.processPiece(surface,  currentPiece, currentRotation, currentX, currentY)
            # if (event.key == pygame.K_DOWN):
            #     while (pygame.key.get_pressed()[pygame.K_DOWN]):
            #         currentY += 50
            #     processPiece(surface,  currentPiece, currentRotation, currentX, currentY)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    currentY += 50
    pygame.display.flip()
    time.sleep(0.2)
