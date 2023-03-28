import pygame as pg
import random
import time

pg.init()

window_size = (600,615)
#texts  on pygame window
screen = pg.display.set_mode(window_size)
font = pg.font.SysFont("Arial", 36)
pg.display.set_caption("Snake")


snake_size = 15
snake_move = 15 #one block is equal to 15 pixels snake moves block by block


#random generation of food
def food():
    snake_foodx = (random.randint(3,39))*snake_size
    snake_foody = (random.randint(3,39))*snake_size
    return snake_foodx,snake_foody
#start menu of the game
def start_menu():
    screen.fill("black")
    txtsurf = font.render("press space to start", True, "white")
    screen.blit(txtsurf,(100,200))
    pg.display.update()
#game over menu
def drgame_over(scr):
    screen.fill("black")
    txtsurf = font.render("game over press r to restart or q to quit", True, "white")
    txtsurf1 = font.render("score : " + str(scr), True, "white")
    screen.blit(txtsurf,(50,200))
    screen.blit(txtsurf1,(100,300))
    pg.display.update()


run = True
game_state = "start_menu"

#starting the screen and keeping it true

while run:

    #the start menu every time we restart all the values change to initial values
    if game_state == "start_menu":
        move = False
        count = 0
        score = 0
        start_menu()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False
                    pg.quit()
                    quit()
            if event.type == pg.KEYDOWN:
                
                if event.key == pg.K_SPACE:
                    game_state = "game"
                    game_over = False
                    snake_movex = 0
                    snake_movey = 0
                    snake_headx = (random.randint(0,38))*snake_size
                    snake_heady = (random.randint(3,38))*snake_size
                    snake_body = [[snake_headx,snake_heady],[snake_headx,snake_heady+15],[snake_headx,snake_heady+30]]
                    snake_foodx = (random.randint(3,39))*snake_size
                    snake_foody = (random.randint(3,39))*snake_size

    #game over screen asking for restart or quit
    elif game_state == "game_over":
        drgame_over(score)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False
            if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        game_state = "start_menu"
                        game_over = False
                    if event.key == pg.K_q:
                        pg.quit()
                        quit()

    #main game starts here
    elif game_state == "game":
        screen.fill("black")
        pg.draw.rect(screen,("blue"),(0,0,600,45)) #top score bar
        pg.draw.rect(screen,("red"),(snake_foodx,snake_foody,snake_size,snake_size)) #drawing of food
        #rendering each element in snake body array
        for i in snake_body:
            pg.draw.rect(screen,("green"),(i[0],i[1],snake_size,snake_size))

        time.sleep(0.1) #can change speed by changing time sleep
        #incrementing the snake x or y axis for moving 
        snake_headx += snake_movex
        snake_heady += snake_movey
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    run = False
            #controling snake
            if event.type == pg.KEYDOWN:
                move = True
                if snake_movey == 0 and event.key == pg.K_UP:
                    snake_movey = -snake_move
                    snake_movex = 0
                elif snake_movey == 0 and event.key == pg.K_DOWN:
                    snake_movey = snake_move
                    snake_movex = 0
                elif snake_movex == 0 and event.key == pg.K_RIGHT:
                    snake_movex = snake_move
                    snake_movey = 0
                elif snake_movex == 0 and event.key == pg.K_LEFT:
                    snake_movex = -snake_move
                    snake_movey = 0
        #deleting and adding elemnts in array sequentally for moving

        if move :
            snake_body.insert(0,[snake_headx,snake_heady])
            snake_body.pop(len(snake_body)-1)
        #if snake crosses boundry or bites itself game ends
        if 0 > snake_headx or snake_headx > 600 or 30 > snake_heady or snake_heady > 615 or count>1:
            move = False
            game_over = True
            game_state = "game_over"
            print(game_state)
        #check if snake bite it self and count 
        if [snake_headx,snake_heady] in snake_body[1::]:
            count += 1

        #counting score and adding snake body
        if snake_foodx == snake_headx and snake_foody == snake_heady :
            score = score +1 
            count = 1
            snake_foodx,snake_foody = food()
            snake_body.append([snake_headx,snake_heady])
            print(score)
        txtsurf = font.render(("score = "+ str(score)), True, "white")
        screen.blit(txtsurf,(8,1))
        pg.display.update()
    #if game over only make this statement work and stop the game
    elif game_over:
        game_state = "game_over"
        game_over = False
pg.quit()
quit()
