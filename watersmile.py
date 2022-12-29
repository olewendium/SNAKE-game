import pygame
import random
import time
pygame.init()



dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')

game_over = False


#сообщение
font_style = pygame.font.SysFont(None, 50)
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [100, 200])

def sscore(msg , color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [0, 0])

#фпс
clock = pygame.time.Clock()

#переменные

game_end=False

while not game_end:
    eaten = True
    co = [0, 0]
    telo = []
    score = 1
    xy = [300, 300]
    x1_change = 0
    y1_change = 0
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_end=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y1_change = 25
                    x1_change = 0
                if event.key == pygame.K_UP:
                    y1_change = -25
                    x1_change = 0
                if event.key == pygame.K_LEFT:
                    x1_change = -25
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = 25
                    y1_change = 0




        dis.fill(white)
        lastcoord = [xy[0],xy[1]]
        xy[0] += x1_change
        xy[1] += y1_change
        if xy[0]>800:
            game_over=True
        if xy[0]<0:
            game_over=True
        if xy[1]>600:
            game_over=True
        if xy[1]<0:
            game_over=True


        #модуль яблока

        if co == xy:
            eaten=True
            score=score+1
        if eaten==True:
            applesX = random.randint(1, 31)*25
            applesY = random.randint(1, 23)*25
            co=[applesX, applesY]

            eaten = False
        pygame.draw.rect(dis, 'pink', (co[0], co[1], 25,25))



        #модуль для змейки

        pygame.draw.rect(dis, black, [xy[0], xy[1], 25, 25])
        if len(telo) != 1:
            for i in range(len(telo)):
                pygame.draw.rect(dis, black,(telo[i][0], telo[i][1], 25, 25))
                if xy == telo[i]:
                    game_over=True
        if len(telo)==score:
            telo.pop(0)

        telo.append([xy[0],xy[1]])
        sscore(f'score: {score}','blue')


        pygame.display.update()
        clock.tick(8.5)
    if game_over == True and game_end == False:
        dis.fill(white)
        message(f'you lose with score: {score}', red)
        pygame.display.update()
        time.sleep(2)
        game_over = False
pygame.quit()
quit()
