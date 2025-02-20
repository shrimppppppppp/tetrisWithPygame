def mainGame():
    import pygame 
    import time
    import random
    import pieceModel

    # Khoi tao cac thu 

    pygame.init()
    pygame.display.set_caption('Tetris created by Shrimp')
    surface = pygame.display.set_mode((1000, 1000))
    bg = pygame.image.load("C:\\Users\\shrimp\\OneDrive\\Documents\\pyGameViTaoCay\\Tetris\\picture\\migu.png").convert(24)
    myfont = pygame.font.SysFont("C:/Users/shrimp/OneDrive/Documents/pyGameViTaoCay/Tetris/Press_Start_2P/PressStart2P-Regular.ttf", 30)
    label = myfont.render("Your score UwU: ", 1, (255, 255, 0))

    playerScore = 0
    currentX = 250
    currentY = 100
    currentRotation = 0
    maxI = [450, 300]
    maxZ = [350, 400]
    maxS = [350, 400]
    maxO = [400]
    maxL = [350, 400, 350, 400]
    maxT = [350, 400, 350, 400]
    maxJ = [350, 400, 350, 400]
    grid = [[0 for x in range(15)] for y in range(25)]

    ##############################################################################
    class __init__:
        
        def pieceColor(pieceChar):
            if (pieceChar == 'i'):
                return pieceModel.color[0]
            elif (pieceChar == 'j'):
                return pieceModel.color[1]
            elif (pieceChar == 'l'):
                return pieceModel.color[2]
            elif (pieceChar == 'o'):
                return pieceModel.color[3]
            elif (pieceChar == 's'):
                return pieceModel.color[4]
            elif (pieceChar == 't'):
                return pieceModel.color[5]
            elif (pieceChar == 'z'):
                return pieceModel.color[6]

        def drawGridAfter(surface):
            for i in range(20):
                for j in range(10):
                    if grid[i][j] != 0:
                        pygame.draw.rect(surface, __init__.pieceColor(grid[i][j]), [j * 50, i * 50, 50, 50], 0)

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
                    if piece[rotation][i][j] != 0:
                        pygame.draw.rect(surface, __init__.pieceColor(piece[rotation][i][j]), [x + j * 50, y + i * 50, 50, 50], 0)
        
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
            return random.choice([pieceModel.pieceI, pieceModel.pieceZ, pieceModel.pieceS, pieceModel.pieceO, pieceModel.pieceL, pieceModel.pieceT, pieceModel.pieceJ])

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
                        if piece[rotation][i][j] != 0:
                            grid[(currentY + i * 50) // 50][(currentX + j * 50) // 50] = piece[rotation][i][j]
                return grid 

        def checkLimitX(piece, rotation, currentX):
            if (piece == pieceModel.pieceI and currentX > maxI[rotation]): 
                currentX = maxI[rotation]
            if (piece == pieceModel.pieceZ and currentX > maxZ[rotation]):
                currentX = maxZ[rotation]
            if (piece == pieceModel.pieceS and currentX > maxS[rotation]):
                currentX = maxS[rotation]
            if (piece == pieceModel.pieceO and currentX > maxO[rotation]):
                currentX = maxO[rotation]
            if (piece == pieceModel.pieceL and currentX > maxL[rotation]):
                currentX = maxL[rotation]
            if (piece == pieceModel.pieceJ and currentX > maxJ[rotation]):
                currentX = maxJ[rotation]
            if (piece == pieceModel.pieceT and currentX > maxT[rotation]):
                currentX = maxT[rotation]
            if (currentX < 0):
                currentX = 0
            return currentX

        def checkLimitY(currentPiece, currentRotation, currentX, currentY, grid):
            if (currentY > 1000 - len(currentPiece[currentRotation]) * 50):
                grid = pieceBehavior.changeGrid(surface, currentPiece, currentRotation, currentX, 1000 - len(currentPiece[currentRotation]) * 50)
                currentY = 0
                currentPiece = pieceBehavior.pickPiece()
                currentX = 250
                currentY = 0
                currentRotation = 0
                
            return currentPiece, currentRotation, currentX, currentY, grid

        def changeRotation(piece, rotation, currentX):
            if (rotation == len(piece) - 1):
                rotation = 0
            else:
                rotation += 1
            currentX = pieceBehavior.checkLimitX(piece, rotation, currentX)
            return currentX, rotation

    ##############################################################################
    # currentPiece = pieceBehavior.pickPiece()
    currentPiece = pieceModel.pieceL
# Main loop

    while True:

        __init__.drawGridAfter(surface)
        currentPiece, currentRotation, currentX, currentY, grid = pieceBehavior.checkLimitY(currentPiece, currentRotation, currentX, currentY, grid)
        pieceBehavior.processPiece(surface, currentPiece, currentRotation, currentX, currentY)

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
                # while (pygame.key.get_pressed()[pygame.K_DOWN]):
                #     currentY += 100
                #     pieceBehavior.processPiece(surface,  currentPiece, currentRotation, currentX, currentY)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        currentY += 50
        pygame.display.flip()
        time.sleep(0.25)
