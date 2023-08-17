import math
import pygame, asyncio
from pygame import mixer
import random
pygame.init() #intialize the pygame
screen=pygame.display.set_mode((800,600)) # create a game screen
#title icon and logo
pygame.display.set_caption("gotta catch'em")
icon=pygame.image.load('icons8-pokemon-go-64.png')
pygame.display.set_icon(icon)
#score
score=0
font=pygame.font.Font('freesansbold.ttf',32)
score_x=10
score_y=10
#game over

gameover_font=pygame.font.Font('freesansbold.ttf',64)

# bcakground sound
mixer.music.load('pokemon theme song.mp3')
mixer.music.play(-1)
#pokemon trainer image
ply_img=pygame.image.load('pokemon-trainer.png')
ply_imgX=370
ply_imgY=480
ply_xchng=0
# pokemons image
poke_img=[]
poke_imgX=[]
poke_imgY=[]
poke_xchng=[]
poke_ychng=[]
no_of_pigi=6
for x in range(no_of_pigi):
    poke_img.append(pygame.image.load('pidgey_icon-icons.com_67536.png'))
    poke_imgX.append(random.randint(0,720))
    poke_imgY.append(random.randint(50,150))
    poke_xchng.append(0.7)
    poke_ychng.append(40)
#pokeball
ball_img=pygame.image.load('Ultra_Ball_icon-icons.com_67500.png')
ball_imgX=0
ball_imgY=480
ball_xchng=0
ball_ychng=0.6
ball_state="ready" # cannot see the pokeball in screen
#background
bcgrd=pygame.image.load('background.jpg')
def showScore(x,y):
    score_value=font.render("SCORE:" + str(score),True,(0,0,255))
    screen.blit(score_value,(x,y))
def pikachu(x,y,i):
    screen.blit(poke_img[i],(x,y))
def gameOver():
    game_over = gameover_font.render("GAME OVER", True, (0, 0, 255))
    screen.blit(game_over, (200,250))

def player(x,y):
    screen.blit(ply_img,(x,y))         # create an image ply_img in the game
def pokeball(x,y):
    global ball_state
    ball_state="fire"
    screen.blit(ball_img,(x+16,y+10))
def caught(ball_imgX,ball_imgY,poke_imgX,poke_imgY):
    distance=math.sqrt(math.pow(ball_imgX-poke_imgX,2)+math.pow(ball_imgY-poke_imgY,2))
    if distance<25:
      return True
    else:
      return False
running= True
while running:
#game loop
    screen.fill((0,0,0))
    screen.blit(bcgrd,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running==False
        #keystroke
        if event.type == pygame.KEYDOWN:
             if event.key==pygame.K_LEFT:
                  ply_xchng=-0.1
             if event.key == pygame.K_RIGHT:
                  ply_xchng=+0.1
             if event.key==pygame.K_SPACE:
                 if ball_state=="ready":
                  ball_imgX=ply_imgX
                  pokeball(ball_imgX,ball_imgY)
        if event.type == pygame.KEYUP:
             if event.type==pygame.K_LEFT or event.type==pygame.K_RIGHT :
              ply_xchng=0

    ply_imgX+=ply_xchng
    if ply_imgX<=0:
        ply_imgX=0
    elif ply_imgX>=736:
        ply_imgX=736
    for i in range(no_of_pigi):
        # game over
          if poke_imgY[i]>400:
            for j in range(no_of_pigi):
                poke_imgY[j]=2000
            gameOver()
            break

          poke_imgX[i]+=poke_xchng[i]
          if poke_imgX[i]<=0:
            poke_xchng[i]=0.1
            poke_imgY[i]+=poke_ychng[i]
          elif poke_imgX[i]>=736:
            poke_xchng[i]=-0.1
            poke_imgY[i]+=poke_ychng[i]
          gotta=caught(ball_imgX,ball_imgY,poke_imgX[i],poke_imgY[i])
          if gotta:
            ball_imgY=480
            ball_state="ready"

            score+=1
            poke_imgX[i] = random.randint(0, 720)
            poke_imgY[i] = random.randint(50, 250)
          pikachu(poke_imgX[i], poke_imgY[i],i)
    #pokeball movement
    if ball_imgY<=0:
        ball_imgY=480
        ball_state="ready"
    if ball_state =="fire":
        ball_imgX=ply_imgX
        pokeball(ball_imgX,ball_imgY)
        ball_imgY-=ball_ychng
    showScore(score_x,score_y)
    player(ply_imgX,ply_imgY)
    pygame.display.update()

