# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame

pygame.init()
win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")
bg = pygame.image.load("bg.jpg")



clock = pygame.time.Clock()

class Player():
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.name = name

        self.vel = 5
        self.jump_count = 10  # 跳跃高度
        self.width = width  # 人物宽度
        self.height = height  # 人物高度
        self.isJump = False
        self.walk_count = 0

        self.walk_left = [pygame.image.load('L'+str(x)+'.png') for x in range(1,10)] #左走图片列表
        self.walk_right = [pygame.image.load('R'+str(x)+'.png') for x in range(1,10)] #右走图片列表

        self.walk_count = 0 #走到第一步
        self.left = False
        self.right = False
        self.char = pygame.image.load("standing.png")

    def draw(self):
        # 判断走的步数
        if self.walk_count >= 8:
            self.walk_count = 0
        else:
            self.walk_count += 1
        # 根据左或者右来加载不同图片
        if self.left:
            win.blit(self.walk_left[self.walk_count], (self.x, self.y))
        elif self.right:
            win.blit(self.walk_right[self.walk_count], (self.x, self.y))
        else:
            win.blit(self.char, (self.x, self.y))

    def control(self, K_LEFT, K_RIGHT, K_UP):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
            print(self.name)
        elif keys[K_RIGHT] and self.x < 500 - self.width - self.vel:
            self.x += self.vel
            self.left = False
            self.right = True
        else:
            self.left = False
            self.right = False

        if self.isJump:
            if self.jump_count >= -10:
                G = 1.2
                if self.jump_count < 0:
                    G = -1.2
                self.y -= 0.5 * G * (self.jump_count ** 2)
                self.jump_count -= 1
                # print("y = %s, jump_count = %s",y,jump_count)
                # print("y = {}, jump_count = {}".format(y,jump_count))
            else:
                self.isJump = False
                self.jump_count = 10
        else:
            if keys[K_UP]:
                # y -= vel
                self.isJump = True
                self.left = False
                self.right = False
def redraw(mans):
    #global walkCount
    win.blit(bg, (0, 0)) # 将背景图从0，0位置画在窗口上
    for man in mans:
        man.draw()
    pygame.display.update() #屏幕刷新

man = Player(200,400,64,64,'lili')
man2 = Player(300,400,64,64,'jiqimao')
run = True

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # man.control(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)
    man.control(pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP)
    man2.control(pygame.K_a,pygame.K_d,pygame.K_w)  # 人物2控制信息
    redraw((man,man2))
    pygame.display.update()

pygame.quit()