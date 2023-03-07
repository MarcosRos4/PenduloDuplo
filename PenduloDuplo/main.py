import pygame
from PenduloDuplo import PenduloDuplo
from math import pi


pygame.init()
janela = pygame.display
tela = janela.set_mode([600,600])
p1 = PenduloDuplo(pi/2, pi, 15, 10, 200, 110, 0.7)


p2 = PenduloDuplo(pi/2, pi, 69, 100, 80, 200, 0.7)

y_anterior = 0
x_anterior = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
    pygame.draw.circle(tela,color=[255,255,255],center=(p1.x1, p1.y1),radius=10) #BOLA 1
    pygame.draw.line(tela,color=[255,255,255],start_pos=(300, 200), end_pos=(p1.x1, p1.y1),width=5) # LINHA 1
    pygame.draw.line(tela,color=[255,255,255],start_pos=(p1.x1, p1.y1), end_pos=(p1.x2, p1.y2),width=5) # LINHA 2
    pygame.draw.circle(tela,color=[255,36,6],center=(p1.x2, p1.y2),radius=10) #BOLA 2

    pygame.draw.circle(tela,color=[0,255,0],center=(p2.x1, p2.y1),radius=10) #BOLA 1
    pygame.draw.line(tela,color=[100,255,100],start_pos=(300, 200), end_pos=(p2.x1, p2.y1),width=5) # LINHA 1
    pygame.draw.line(tela,color=[100,100,255],start_pos=(p2.x1, p2.y1), end_pos=(p2.x2, p2.y2),width=5) # LINHA 2
    pygame.draw.circle(tela,color=[0,0,255],center=(p2.x2, p2.y2),radius=10) #BOLA 2


    x_anterior = p1.x2
    y_anterior = p1.y2
    p1.novaPosicao()
    p2.novaPosicao()
    

    janela.update()
    tela.fill([0,0,0])
    pygame.time.Clock().tick(60)

