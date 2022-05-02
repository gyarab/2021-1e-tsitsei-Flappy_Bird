import pygame

mariox=50
marioy=400

game=[]
x=150
y=320
for k in range(5):
    pos=[(x,y),1]
    game.append(pos)
    x=x+100
    y=y-50

mario=pygame.image.load("mario.png")
mariorect = mario.get_rect()
mario=pygame.image.load("mario.png")
mariorect = mario.get_rect()

block=pygame.image.load("wall.png")
blockrect = block.get_rect()

coin=pygame.image.load("coin.png")
coinrect = coin.get_rect()

bg=pygame.image.load("bg.png")
bgrect = bg.get_rect()
f=0
WHITE = (255, 255, 255)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Маріо")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)

    move=0

    screen.blit(bg, (0,0))

    for element in game:
        wallx=element[0][0]
        wally=element[0][1]
        screen.blit(block, (wallx,wally))
        if abs(mariox-wallx)<30 and abs((marioy-40)-(wally-50))<40:
            move=1
            element[1]=0
        if element[1]==1:
            screen.blit(coin, (wallx+10,wally-50))
    if f==1:
        f=0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            mariox-=5
            f=1
        if event.key == pygame.K_RIGHT:
            mariox+=5
            f=1
        if event.key == pygame.K_UP:
            marioy-=10
            f=1
    if f==1:

    if mariox > 650:
        mariox=650
    if mariox < 0:
        mariox=0
    if marioy > 400:
        marioy=400
    if marioy < 0:
        marioy=0

    if move==0:
        marioy+=5

    screen.blit(mario, (mariox,marioy))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
