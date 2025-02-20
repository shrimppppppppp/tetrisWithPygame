import pygame 
import main

pygame.init()
pygame.display.set_caption('Tetris created by Shrimp')
surface = pygame.display.set_mode((1000, 1000))
bg = pygame.image.load("C:\\Users\\shrimp\\OneDrive\\Documents\\pyGameViTaoCay\\Tetris\\picture\\Tetris with Hatsune Miku.png").convert(24)
sticker = pygame.image.load("C:\\Users\\shrimp\\OneDrive\\Documents\\pyGameViTaoCay\\Tetris\\picture\\miguSticker.jpg")
myfont = pygame.font.Font("C:/Users/shrimp/OneDrive/Documents/pyGameViTaoCay/Tetris/Press_Start_2P/PressStart2P-Regular.ttf", 60)
# label = myfont.render("START", 1, (0, 0, 0))

for i in range(10):
    surface.blit(sticker, (0, i * 104))
for i in range(10):
    surface.blit(sticker, (896, i * 104))

surface.blit(bg, (104, 0))

def textHollow(font, message, fontcolor):
    notcolor = [c^0xFF for c in fontcolor]
    base = font.render(message, 0, fontcolor, notcolor)
    size = base.get_width() + 2, base.get_height() + 2
    img = pygame.Surface(size, 16)
    img.fill(notcolor)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img

def textOutLine(font, message, fontcolor, outlinecolor):
    base = font.render(message, 0, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img

surface.blit(textOutLine(myfont, "START", (255, 0, 0), (255, 255, 255)), (370, 500))

while True:

    for event in pygame.event.get():
        if (pygame.mouse.get_pressed()[0]):
            x, y = pygame.mouse.get_pos()
            if (x >= 363 and x <= 657 and y >= 485 and y <= 561):
                main.mainGame()
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()
    pygame.display.flip()
