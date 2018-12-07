from Plane import *

class PlaneGame(object):
    '''

    '''
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 创建游戏窗口
        self.clock=pygame.time.Clock()  # 创建游戏时钟
        self.__create_sprite()  # 创建物件
        pygame.time.set_timer(CREATE_ENEMY_EVENT,100000)  # 创建敌机事件，每隔1秒出现一个敌机
        pygame.time.set_timer(HERO_FIRE_EVENT,600)  # 设置发射子弹事件，默认每隔0.3秒发射一个

    def __create_sprite(self):
        bg1 = BackGround()  # 背景图片，设置背景物件
        bg2 = BackGround(True)  # 设置背景
        self.back_ground=pygame.sprite.Group(bg1,bg2)  # 两个背景图片交替出现
        self.enermy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group=pygame.sprite.Group(self.hero)


    def start_game(self):
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handle()
            self.__check_collide()
            self.__update_sprite()
            pygame.display.update()

    def __event_handle(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                PlaneGame.__game_over()  # 为什么使用PlaneGame，而不使用self呢？
            elif event.type==CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enermy_group.add(enemy)
            elif HERO_FIRE_EVENT:
                self.hero.fire()
            elif event.type==pygame.KEYDOWN and event.type==pygame.K_RIGHT:
                print('向右移动')
            keys_pressed=pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                speed=5
            else:
                speed=2
            if keys_pressed[pygame.K_LEFT]:
                print("Click Left Arrow")
                self.hero.speed=-speed
                self.hero.ymove=False
            elif keys_pressed[pygame.K_RIGHT]:
                print("Click Right Arrow")
                self.hero.speed=speed
                self.hero.ymove=False
            elif keys_pressed[pygame.K_UP]:
                print("Click Up Arrow")
                self.hero.speed=-speed
                self.hero.ymove=True
                # surface = self.hero.image
                # print(type(surface))
                # self.hero.image=pygame.transform.smoothscale(surface, (80,120))
            elif keys_pressed[pygame.K_DOWN]:
                print("Click Down Arrow")
                self.hero.speed=speed;
                self.hero.ymove=True
            else:
                self.hero.speed=0

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enermy_group,True,True)
        enemies = pygame.sprite.spritecollide(self.hero,self.enermy_group,True)
        if len(enemies)>0:
            self.hero.kill()
            self.__game_over()

    def __update_sprite(self):
        self.back_ground.update()
        self.back_ground.draw(self.screen)
        self.enermy_group.update()
        self.enermy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @ staticmethod
    def __game_over():
        pygame.quit()
        exit()

# 程序执行的入口
if __name__ == '__main__':
    while True:
        game = PlaneGame()
        game.start_game()
