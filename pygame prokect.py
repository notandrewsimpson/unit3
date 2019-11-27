import pygame

white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()  #calling inheritance of the sprite function
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bullet(pygame.sprite.Sprite):

    def __init__(self, playerlocation, mouselocation):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = playerlocation[0]
        self.rect.y = playerlocation[1]
        self.direction = (playerlocation[1]-mouselocation[1])/(abs(playerlocation[0]-mouselocation[0]))*-1

    def update(self):
        self.rect.x += 1
        self.rect.y += self.direction
        print("fjfgju")


pygame.init()
screenx = 600
screeny = 800
display_surface = pygame.display.set_mode([screenx, screeny])  # setting the screen size for the game
pygame.display.set_caption("SUPER STICKMAN SHOOTER")
font = pygame.font.Font('AldotheApache2.ttf', 70)
font1 = pygame.font.Font('AldotheApache2.ttf', 90)
font2 = pygame.font.Font('AldotheApache2.ttf', 50)
text = font.render('SUPER STICKAN', True, green)
text1 = font1.render('SHOOTER', True, green)
text2 = font2.render('PRESS SPACE TO START', True, green)
textbound = text.get_rect()
textbound1 = text1.get_rect()
textbound2 = text2.get_rect()
textbound.x = ((screenx/2)-190)
textbound.y = 200
textbound1.x = ((screenx/2)- 150)
textbound1.y = 255
textbound2.x = 90
textbound2.y = 400
bg1 = pygame.image.load('background1.jpeg')
bg2 = pygame.image.load('background.jpeg')

all_sprites_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()
stickman = Player(250, 690)

all_sprites_list.add(stickman)

runtime = True
display_surface.blit(bg1, [0,0])
display_surface.blit(text, textbound)
display_surface.blit(text1, textbound1)
display_surface.blit(text2, textbound2)
start = False

while runtime == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        start = True


    if keys[pygame.K_a] and stickman.rect.x > 0:
        stickman.rect.x -= 10
    if keys[pygame.K_d] and stickman.rect.x < (600 - 75):
        stickman.rect.x += 10
    if keys[pygame.K_w]:
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        bullet = Bullet((stickman.rect.x, stickman.rect.y), (Mouse_x, Mouse_y))
        bullets.add(bullet)

        #WHILE SPACE KEY IS PRESSED STUFF HAPPEN HERE
    if start:
        display_surface.blit(bg2, [0, 0])
        all_sprites_list.draw(display_surface)
        bullets.update()
        bullets.draw(display_surface)

    pygame.display.flip()

pygame.quit()
