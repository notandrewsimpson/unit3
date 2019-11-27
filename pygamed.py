import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Move Sprite With Keyboard')
stickman = pygame.image.load('stickman.png')

# Create the player paddle object
player = Player(50, 50)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)


done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.rect.y-=10
    if keys[pygame.K_DOWN]:
        player.rect.y+=10
    if keys[pygame.K_LEFT]:
        player.rect.x-=10
    if keys[pygame.K_RIGHT]:
        player.rect.x += 10

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         player.rect.x -= 50
        #     elif event.key == pygame.K_RIGHT:
        #         player.rect.x += player.rect.width
        #     elif event.key == pygame.K_UP:
        #         player.rect.y -= player.rect.height
        #     elif event.key == pygame.K_DOWN:
        #         player.rect.y += player.rect.height

    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)
    screen.blit(stickman, [0,0])
    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause


pygame.quit()