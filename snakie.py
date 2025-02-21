import pygame #for game development
import time
import random #for generating random food positions

pygame.init() #initialize pygame modules

#simply, defining colors
white = (255, 255, 255) #for text
yellow = (255, 255, 102) #for score text
black = (0, 0, 0) #for snake
red = (213, 50, 80) #for "Game over"
green = (0, 255, 0) #for food
blue = (50, 153, 213) #for background

#display dimensions
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height)) #set mode() creates game window
pygame.display.set_caption('Snakie') #set caption() creates the title

#a clock object to control frame rate
clock = pygame.time.Clock()

#game variables
snake_block = 10
snake_speed = 10 #how fast the game runs

font_style = pygame.font.SysFont("bahnschrift", 25) # for messages
score_font = pygame.font.SysFont("comicsansms", 35) #for score


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow) #render() creates text surface
    dis.blit(value, [0, 0]) #blit() places the text at (0,0) on the screen.


def our_snake(snake_block, snake_list):
    for x in snake_list: #Loops through snake_list (which stores all body segments) and draws them.
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block]) #draw.rect() draws a black rectangle for each body part.


#displays text messages on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    #initial position for snake and food
    x1 = dis_width / 2
    y1 = dis_height / 2 #x1 and y1 start at the centre

    x1_change = 0
    y1_change = 0

    snake_List = [] #stores the snake body parts
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #random.randrange() generates random x, y coordinates within screen bounds.
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 #round() * 10.0 ensures the food aligns with the snake's grid.

    while not game_over:

        while game_close == True: #handles "game over" state
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get(): #handles user input for restart or quit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: #quits
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: #restart
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True #game over if snakie hits wall
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True #this loop ends the game if snake hits itself

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody: #check food is eaten
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()