import pygame
import random
import os
#add music 
pygame.mixer.init()
pygame.mixer.music.load('back1.mp3')
pygame.mixer.music.play()
pygame.init()

#color set
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# creating game window 
screen_width = 800
screen_height = 500
screen_window = pygame.display.set_mode((screen_width, screen_height))
# background image
bgimg = pygame.image.load('backgr.jpg')
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
bgimg1 = pygame.image.load('backgr1.jpg')
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()
bgimg2 = pygame.image.load('backgr2.jpg')
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()
#create title for game window
pygame.display.set_caption("Foody_Snake")
pygame.display.update()


# Create clock time for snake 
clock = pygame.time.Clock()
# lets take a default font from the system
font = pygame.font.SysFont(None, 55)


# how to display your score on screen
def text_score(text, color, x,y):
    screen_score = font.render(text, True, color)
    screen_window.blit(screen_score,(x,y))

# how to increase the length of snake
def plot_snake(screen_window, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(screen_window, color, [x,y, snake_size,snake_size])

#lets create welcome before starting the game
def welcome():
    exit_game = False
    while not exit_game:
        screen_window.fill(white)
        screen_window.blit(bgimg, (0, 0))        
        text_score("Welcome To Foody Snake",black,190,5)
        text_score("Press Space Bar to Start Game",black,160,440)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                    pygame.mixer.music.load('back2.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        
        pygame.display.update()
        clock.tick(20)
        

            
# game loop
def gameloop():
    # pygame specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    #lets make the speed for snake 
    velocity_x = 0
    velocity_y = 0
    fps = 20
    score = 0
    snake_list = []
    snake_length = 1
    # lets make food for snake
    food_x = random.randint(30, screen_width/2)
    food_y = random.randint(30, screen_height/2)
    #if hiscore file not exist in os
    
    with open("hiscore.txt","r") as f:
        hiscore = f.read()
    while not exit_game:
    # create game over function
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            screen_window.fill(white)
            screen_window.blit(bgimg2, (0, 0))
            text_score("Game Over! Press Enter Key to Continue", red, 30, 250)            
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
        # To restart the game through Enter key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
        # create keys to move snake
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0
                # how to insert cheat code 
                    if event.key == pygame.K_q:
                        score +=10
        # food eaten by snake
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 10
                food_x = random.randint(20,screen_width)
                food_y = random.randint(20,screen_height)
        #it increase snake length
                snake_length += 3
                if score>int(hiscore):
                    hiscore = score
            
        # create speed for snake
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
        # to fill the screen with color
            screen_window.fill(white)
            screen_window.blit(bgimg1, (0, 0))
        #lets print the score on the screen
            text_score("Score: "+ str(score) + "  Hiscore: "+str(hiscore), red,5,5)
            if {not os.path.exists("hiscore.txt")}:
                with open("hiscore.txt", 'w') as f:
                    f.write("0")
        #define snake length when snake eat food
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            
            
        # it delete the head of snake
            if len(snake_list) > snake_length:
                del snake_list[0]
        # overlapping in snake
            if head in snake_list[ :-1]:
                game_over = True
                pygame.mixer.music.load('back3.wav')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('back3.wav')
                pygame.mixer.music.play()         

        # to draw snake size with color
            pygame.draw.rect(screen_window, red, [food_x, food_y, snake_size, snake_size])
        # pygame.draw.rect(screen_window, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(screen_window,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
