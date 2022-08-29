# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame

pygame.init()
win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")
bg = pygame.image.load("bg.jpg")

char = pygame.image.load("standing.png")

clock = pygame.time.Clock()

x = 220
y = 400

vel = 5
jump_count = 10 #跳跃高度
width = 64 #人物宽度
height = 64 #人物高度
run = True
isJump = False

walk_left = [pygame.image.load('L'+str(x)+'.png') for x in range(1,10)] #左走图片列表
walk_right = [pygame.image.load('R'+str(x)+'.png') for x in range(1,10)] #右走图片列表
walk_count = 0 #走到第一步
left = False
right = False

def redraw_win():
    # 判断走的步数
    global walk_count
    if walk_count >= 8:
        walk_count = 0
    else:
        walk_count += 1
    win.blit(bg, (0, 0))
    # 根据左或者右来加载不同图片
    print(walk_count)
    if left:
        win.blit(walk_left[walk_count], (x, y))
    elif right:
        win.blit(walk_right[walk_count], (x, y))
    else:
        win.blit(char, (x, y))

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width -vel:
        x += vel
        left= False
        right = True
    else:
        left = False
        right = False

    if isJump:
        if jump_count >= -10:
            G = 1.2
            if jump_count < 0:
                G = -1.2
            y -= 0.5*G*(jump_count**2)
            jump_count -= 1
            # print("y = %s, jump_count = %s",y,jump_count)
            # print("y = {}, jump_count = {}".format(y,jump_count))
        else:
            isJump = False
            jump_count = 10
    else:
        if keys[pygame.K_UP]:
            # y -= vel
            isJump = True
            left= False
            right = False

    redraw_win()
    pygame.display.update()

pygame.quit()