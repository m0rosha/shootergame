#Створи власний Шутер!

from pygame import *
from random import *
import time as timer


lol = 0 
score = 0 
window = display.set_mode((700, 500))
display.set_caption('TRYHARD GAME hell nah')
da = 3
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')

bkgrnd_img = image.load('galaxy.jpg')
bkgrnd = transform.scale(bkgrnd_img, (700,500))
font.init()
run = True
clock = time.Clock()
font = font.Font(None, 70)
text2 = font.render('Lost:' + str(lol), True, (255,0,0))
text = font.render('Killed:'+ str(score), True, (0,255,0))
result = font.render('LOSE',True, (255,0,0 ))
dada = font.render('Lives:'+ str(da), True, (255,255,0))

class Sprite(sprite.Sprite):

    
    def __init__(self, pic_name, x,y,speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(pic_name),(width,height))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        speed = 2
    

        self.speed = speed
    

        
    def Fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx-5, self.rect.top,3, 15,15)
        bullets.add(bullet)
    def render(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(Sprite):
    def move(self):
        keys = key.get_pressed()
        
        
        if keys[K_RIGHT]and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_LEFT]and self.rect.x > 5:
           self.rect.x -= self.speed
lost = 0

class Enemy(Sprite):
    
    def update(self):
        self.rect.y = self.rect.y + self.speed
        global lost
        
        if self.rect.y >= 500:
            lost = lost+1
            self.rect.y = 50
            self.rect.x = randint(50, 650)
            self.speed = randint(1,2)
            new_monster = Enemy('ufo.png', self.rect.x, self.rect.y, self.speed, 50, 50)
            monsters.add(new_monster)
monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()
for i in range(1,6):
    asteroid = Enemy('asteroid.png',randint(50,650),0,randint(1,2),50,50)
    asteroids.add(asteroid)
for i in range(1,6):
    monster = Enemy('ufo.png', randint(50,650), 0, randint(1,2), 50,50)
    monsters.add(monster)
    

class Bullet(Sprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <=0:
            self.kill()
hit = False
finish = False
raketa= Player('rocket.png', 350, 400, 60, 65, 65)

while run:
     
    if finish != True:
        window.blit(bkgrnd,(0,0))
        raketa.render()
        monsters.draw(window)
        monsters.update()
        window.blit(text,(0,0))
        window.blit(text2,(0,60))
        bullets.draw(window)
        bullets.update()
        raketa.move()
        sprites_list = sprite.spritecollide(raketa, monsters, True)
        sprites_listt = sprite.spritecollide(raketa, asteroids,True)
        window.blit(dada,(500,0))
        asteroids.draw(window)
        asteroids.update()
        for monster in sprites_list:
            da = da -  1 
            dada = font.render('Lives:'+str(da),True,(255,255,0))
        for asteroid in sprites_listt:
            da = da - 1 
            dada = font.render('Lives:'+str(da),True,(255,255,0))
        if da <= 0:
            finish = True
            result = font.render('YOU LOSE', True, (255,0,0))
            
            window.blit(result,(700/2,500/2))
             
            
        if lol >= 3:
            finish = True
            result = font.render('YOU LOSE', True, (255,0,0))
            window.blit(result,(700/2,500/2))
            
        if score >= 6:
            result = font.render('YOU WIN', True,(0,255,0))
            window.blit(result,(700/2, 500/2 ))
            finish = True
                
    for a in event.get():
        if a.type == QUIT:
            run = False
        elif a.type == KEYDOWN:
            if a.key == K_SPACE:
                raketa.Fire()
    for bullet in bullets:
        for monster in monsters:
            if bullet.rect.colliderect(monster.rect):
                bullet.kill()
                monster.kill()
                fire.play()
                score += 1
                hit = True
    for monster in monsters:
        if monster.rect.y >= 498:
            lol = lol  + 1
            text2 = font.render('Lost:' + str(lol), True, (255,0,0))
    if hit:
        score + 1
        hit = False
        text = font.render('Killed:' + str(score), True, (0,255,0))
    clock.tick(60)
    display.update()
