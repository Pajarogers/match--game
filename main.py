#Paja Rogers
#Course:
# Week 3 
# match game

# building a matching game

from math import pi
from random import Random, randint, random
from turtle import title, width
import pygame
pygame.init()
import random



#****game varibales and constants
WIDTH = 600
HEIGHT = 600
white = (255,255,255)
black = (0,0,0)
gray = (128, 128, 128)
greenyellow= (173,255,47)
green1= (0,255,0)
medgreen= (60,179,113)
blue=(0,0,255)
purple =(104,34,139)
green= (0,128,0)
cyan = (0,238,238)
#frame rate frames per second
fps =60
#define speed game run
timer = pygame.time.Clock ()
rows = 5
cols = 4
correct = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
options_list  = []
piece = []
spaces = []
used = []
first_guess=False
second_guess=False
first_guess_number=0
second_guess_number=0
score = 0
best_score = 0
matches = 0
new_board = True
gameover = False


#****creating the screen for the game
screen = pygame.display.set_mode([WIDTH, HEIGHT])

#game name display to user
pygame.display.set_caption('Numbers 1-10')

#define fonts in pygame 
title_font = pygame.font.Font('freesansbold.ttf', 46)
small_font = pygame.font.Font('freesansbold.ttf', 62)
score_font = pygame.font.Font('freesansbold.ttf', 28)


#define functions for game
def generate_board():
   global options_list
   global spaces
   global used
    #for loop for the replay button
   for item  in range(rows * cols // 2):
        options_list.append(item)
    # store the list and remove used list    
   for item in range( rows * cols):
       piece = options_list[random.randint(0, len(options_list)-1)]
       spaces.append(piece)
       if piece in used:
           used.remove(piece)
           options_list.remove(piece)
       else:
           used.append(piece)
            
   
    
def backgrounds_for_game():
    #size of the top rectangle for game name, instruction displayed to the user
    top_menu = pygame.draw.rect(screen, white, [0, 0, WIDTH, 100])
    #rending text for pygame
    title_text = title_font.render('        Numbers Match',True, medgreen,) 
    screen.blit(title_text, (10,20))
    
    board_space = pygame.draw.rect(screen, cyan, [0, 100, WIDTH, HEIGHT-200])
    bottom_menu = pygame.draw.rect(screen, black, [0, WIDTH - 100, WIDTH, 100])
    
    #replaybutton 
    replaybutton = pygame.image.load('images/play.png').convert()
    green_replay_button =pygame.transform.scale(replaybutton,(80,80))  
    restart_game_button=pygame.draw.rect(screen,black,[00, 500 , 100, 100],0) 
# coordinates of the image for play button
    screen.blit(green_replay_button, (10,510))
    
    #text for score
    score_text = score_font.render(f'   Matches:  {score}',True, medgreen,) 
    screen.blit(score_text, (350,520))
    best_text = score_font.render(f'',True, medgreen,) 
    screen.blit(best_text, (350,560))
    return restart_game_button

#creating board for game
def draw_board():
    global rows
    global cols
    global correct
    board_list = []
    for i in range(cols):
        for j in range(rows):
            piece =pygame.draw.rect(screen, white, [i * 115 + 105, j * 80 + 112, 60, 60], 0, 8)
            board_list.append (piece)
            #piece_text = small_font.render(f'{spaces[i * rows +j]}', True,green1)
            #screen.blit(piece_text, (i * 115 + 120, j * 80 + 115))
            
    for r in range(rows):
        for c in range(cols):
            if correct[r][c] ==1:
                pygame.draw.rect(screen, purple, [c * 115 + 105, r * 80 + 112, 64, 64], 3, 8)
                piece_text =small_font.render(f'{spaces [c * rows + r ]}',True, green)
                screen.blit(piece_text, (c *120 + 113, r * 80 + 112))
                
    return board_list
      
 #checking user input to see if the correct or been picked     
def check_guesses(first, second):
    global spaces
    global correct
    global score
    global matches
    if spaces[first] == spaces[second]:
        col1 =first // rows
        col2 =second // rows
        row1 = first -(col1 * rows)
        row2 = second -(col2 * rows)
        if correct[row1][col1]== 0 and correct [row2][col2]== 0:
            correct[row1][col1]=1
            correct[row2][col2]=1
            score +=1
            matches +=1
           
            
        else:
            score +=1
            
       
#****main game loop
#variable for game loop set to true
running = True
#while loop when the game is running
while running:
    timer.tick(fps)
    screen.fill(white)
    if new_board:
        generate_board()  
      
        new_board = False
    
    #backgrounds for game
    restart_game_button=backgrounds_for_game()
    board = draw_board()
    
    #check guesses
    if first_guess and second_guess:
        check_guesses(first_guess_number, second_guess_number)
        pygame.time.delay(1000)
        first_guess = False
        second_guess =False
    
    
    
    #exit for game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #event type for games choices
        if event.type == pygame.MOUSEBUTTONDOWN:
           for i in range(len(board)):
               button = board[i]
               if not gameover:
                  if button.collidepoint(event.pos) and not first_guess:
                   first_guess =True
                   first_guess_number = i
                   print (i)
                  if button.collidepoint(event.pos) and not second_guess and first_guess and i !=first_guess_number:
                   second_guess =True
                   second_guess_number = i
                   print (i)
                   
               if restart_game_button.collidepoint(event.pos):
                   options_list=[]
                   used=[]
                   spaces=[]
                   new_board=True
                   score=0
                   matches=0
                   correct = [[0,0,0,0],
                              [0,0,0,0],
                              [0,0,0,0],
                              [0,0,0,0],
                              [0,0,0,0]]
                   gameover =False
                         
 #highlight picked numbers
    if first_guess:
       piece_text = small_font.render(f'{spaces[first_guess_number]}', True,blue)
       location = (first_guess_number // rows *120 +112 , (first_guess_number - (first_guess_number //rows*rows)) * 80 + 112)
       screen.blit(piece_text, (location))  
               
    if second_guess:
       piece_text = small_font.render(f'{spaces[second_guess_number]}', True,blue)
       location = (second_guess_number // rows *120 +112 , (second_guess_number - (second_guess_number //rows*rows)) * 80 + 112)
       screen.blit(piece_text, (location))     
              
         #check to see game is over              
    if matches == rows * cols // 2:
        gameover = True 
        #winner = pygame.draw.rect(screen, white,[10, HEIGHT-350, WIDTH -40,150],0,5)
       # winner_text = title_font.render(f'You win in {score} moves!',True,purple)
        #screen.blit(winner_text, (100, HEIGHT -150))
        areplaybutton = pygame.image.load('images/blue_winner.png').convert()
        agreen_replay_button =pygame.transform.scale(areplaybutton,(275,275))  
    
        screen.blit(agreen_replay_button, (150,150))
       
            
    pygame.display.flip()
pygame.quit()
            
            

   

