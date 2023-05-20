import pygame
class Button(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,btn_image):
        self.image = pygame.transform.scale(pygame.image.load(btn_image),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
    
    def Draw(self,window):
        pos = pygame.mouse.get_pos()
        action = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        window.blit(self.image,(self.rect.x,self.rect.y))
        return action        
    