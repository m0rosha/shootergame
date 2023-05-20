import pygame 

class Plane(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,btn_image):
        super().__init__()
        
        self.image = pygame.transform.scale(pygame.image.load(btn_image),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0

    def update(self):
        self.vel_y += 1  
        self.rect.y += self.vel_y

    def restarts(self):
        self.rect.x = 200
        self.rect.y = 200
        self.vel_y = 0
    def jump(self):
        self.vel_y = -10  
    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.jump()
        
       
    def draw(self, window):
        window.blit(self.image, self.rect)