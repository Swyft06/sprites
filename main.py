import pygame 
pygame.init()

WIDTH = 700
HEIGHT = 500

WIN = pygame.display.set_mode([WIDTH,HEIGHT])
#Creating the class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        #Super extracts attributes of sprite class (parent class)
        super().__init__()
        #Loads and scales image
        self.image = pygame.image.load('rocket.png')
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()

    
    def update(self,pressed_keys):
        #Key functions
        if(pressed_keys[pygame.K_UP]):
            self.rect.move_ip(0,-5)
        if(pressed_keys[pygame.K_DOWN]):
            self.rect.move_ip(0,5)
        if(pressed_keys[pygame.K_LEFT]):
            self.rect.move_ip(-5,0)
        if(pressed_keys[pygame.K_RIGHT]):
            self.rect.move_ip(5,0)

        #Setting borders
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


#Creating the sprites
sprites = pygame.sprite.Group()


#Creating the object
def start_game():
    rocket = Player()
    sprites.add(rocket)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        space = pygame.image.load('space.png')
        bg=pygame.transform.scale(space,(WIDTH,HEIGHT))
        WIN.blit(bg,(0,0))
        #Checks if keys are pressed
        pressed_keys = pygame.key.get_pressed()
        rocket.update(pressed_keys)
        sprites.draw(WIN)
        pygame.display.update()

start_game()

