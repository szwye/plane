import random
import pygame

SCREEN_RECT=pygame.__rect_constructor(0, 0, 480, 852)
FRAME_PER_SEC=60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT+1


class GameSprite(pygame.sprite.Sprite):
    ''' 飞机大战精灵 '''
    def __init__(self,image_name,speed=1):
        super().__init__()
        # print(image_name)
        self.image = pygame.image.load(image_name)
        # print("Load image success")
        print(image_name,"size",self.image)
        self.rect=self.image.get_rect()
        self.speed=speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):
    def __init__(self, is_all=False):
        super(BackGround, self).__init__('./img/background.jpg')
        if is_all:
            self.rect.y =- self.rect.height

    def update(self):
        super(BackGround,self).update()
        if self.rect.y>= SCREEN_RECT.height:
            self.rect.y= - self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        super(Enemy,self).__init__('./img/smallplane.png')
        self.speed=random.randint(2,4)
        self.rect.bottom=0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print('敌机被炸毁啦！ %s' % self.rect)


class Bullet(GameSprite):
    '''子弹精灵'''
    def __init__(self):
        super().__init__('./img/bullet.png',-4)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()


class Hero(GameSprite):
    '''英雄精灵'''
    def __init__(self,ymove=False):
        super().__init__('./img/bigplane.png',0)
        self.ymove = ymove
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom=SCREEN_RECT.bottom-30
        self.bullets=pygame.sprite.Group()

    def update(self):
        if self.ymove:
            self.rect.y += self.speed
            print("Hero Y is:",self.rect.y)
        else:
            self.rect.x += self.speed
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y>SCREEN_RECT.bottom-134:
            self.rect.y = SCREEN_RECT.bottom-134
        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.right>SCREEN_RECT.right:
            self.rect.right=SCREEN_RECT.right

    def fire(self):
        bullet = Bullet()
        bullet.rect.bottom =self.rect.y
        bullet.rect.centerx =self.rect.centerx
        self.bullets.add(bullet)

    def __del__(self):
        print('主飞机被炸毁啦！')
        print('游戏结束')







