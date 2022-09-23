import pygame
import random
import os


pygame.mixer.init()

pygame.init()



white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
yellow=(255,255,0)

screen_width = 900
screen_height = 600

GameWindow = pygame.display.set_mode((screen_width,screen_height))


BackgroudImage=pygame.image.load('images/wp3906260.jpg') 
BackgroudImage=pygame.transform.scale(BackgroudImage,(screen_width,screen_height)).convert_alpha()


WelcomeImage = pygame.image.load('images/download.jpeg')
WelcomeImage = pygame.transform.scale(WelcomeImage,(screen_width,screen_height)).convert_alpha()

EndScreen = pygame.image.load('images/istockphoto-1368072565-612x612.jpg')
EndScreen = pygame.transform.scale(EndScreen,(screen_width,screen_height)).convert_alpha()


pygame.display.set_caption("Snake Game")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    GameWindow.blit(screen_text,[x,y])

def plot_snake(GameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(GameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        GameWindow.fill(white)
        GameWindow.blit(WelcomeImage, (0,0))
        text_screen("Welcome To Saanp Game Made By Ayush",white,80,240)
        text_screen("Press 'LCtrl' To play",white,260,290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL:
                    pygame.mixer.music.load('audio/Nagin Been Music.mp3')
                    pygame.mixer.music.play()
                    gameloop()





        pygame.display.update()  
        clock.tick(50)

def gameloop():
    ExistGame = False
    gameOver = False
    snake_x = 44
    snake_y = 50
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    snk__list=[]
    snk_length=1  
    
    if(not os.path.exists("utils/HighScore.txt")):
        with open("utils/HighScore.txt", 'w') as f:
            f.write("0")  
    with open('utils/HighScore.txt', "r") as f:
        HighScore = f.read()


    while not ExistGame:
        if gameOver:
            with open('utils/HighScore.txt', "w") as f:
                f.write(str(HighScore))

            GameWindow.fill(white)
            GameWindow.blit(EndScreen,(0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    ExistGame=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()    


        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    ExistGame=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0    
                    if event.key == pygame.K_q:
                        score+=4    
            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y            

            if abs(snake_x -food_x)<20 and abs(snake_y-food_y)<20:
                score+=10
                print("Score",score*10)
                food_x = random.randint(20,screen_width/2)
                food_y = random.randint(20,screen_height/2)
                snk_length+=5
                if score>int(HighScore):
                    HighScore=score
            
            GameWindow.fill(white)
            GameWindow.blit(BackgroudImage, (0,0)) 
            text_screen("Score: "+str(score) + "HighScore: "+str(HighScore),red,5,5)
            pygame.draw.rect(GameWindow,red,[food_x, food_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk__list.append(head)

            if len(snk__list)>snk_length:
                del snk__list[0]

            if head in snk__list[ :-1]:
                gameOver=True    
                pygame.mixer.music.load('audio/Big.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                gameOver= True
                pygame.mixer.music.load('audio/Big.mp3')
                pygame.mixer.music.play()

            # pygame.draw.rect(GameWindow,black,[snake_x, snake_y, snake_size, snake_size])
            plot_snake(GameWindow,yellow,snk__list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()       
welcome()