import pygame
import random
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,btn_image):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(btn_image),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self,win):
    
        win.blit(self.image, (self.rect.x,self.rect.y))
        #win.blit(self.image, (self.rect.x,self.rect.y-400))


        
    def update(self):
        self.rect.x -= 2  
        if self.rect.x <=50:
            self.rect.x = 700
    def restart(self):
        self.rect.x = 700



    def spawn_obstacles():
        obstacles = pygame.sprite.Group()
         
        gap_size = 100
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()

        top_height = random.randint(0, screen_height - gap_size)
        bottom_height = screen_height - gap_size - top_height
        
        top_obstacle = Obstacle(screen_width, 0, 50, top_height)
        bottom_obstacle = Obstacle(screen_width, top_height + gap_size, 50, bottom_height)
        
        obstacles.add(top_obstacle)
        obstacles.add(bottom_obstacle)