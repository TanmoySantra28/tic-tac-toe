import pygame, sys
import numpy as np

pygame.init()

width=600   
height=600
line_width=15
board_rows=3
board_cols=3
circle_rad=60
circle_wid=15
cross_wid=25
space=50
light_blue=(0,205,205)
dark_red=(153,0,0)
line_color= (0,102,102)
circle_color=(239,231,200)
cross_color=(66,66,66)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Simple Tic Tac Toe')
screen.fill(light_blue)

#console board
board=np.zeros((board_rows,board_cols))

#pygame.draw.line(screen,dark_red,(10,10),(300,300),10)

def draw_line():
    #horizontal 1
    pygame.draw.line(screen,line_color,(0,200),(600,200),line_width)
    #horizontal 2
    pygame.draw.line(screen,line_color,(0,400),(600,400),line_width)
    #vertical 1
    pygame.draw.line(screen,line_color,(200,0),(200,600),line_width)
    #vertical 2
    pygame.draw.line(screen,line_color,(400,0),(400,600),line_width)

def draw_figure():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col]==1:
                pygame.draw.circle(screen,circle_color,(int(col*200 + 100),int(row*200 + 100)),circle_rad,circle_wid)
            elif board[row][col]==2:
                pygame.draw.line(screen,cross_color,(col*200+space,row*200+200-space),(col*200+200-space,row*200+space),cross_wid)
                pygame.draw.line(screen,cross_color,(col*200+space,row*200+space),(col*200+200-space,row*200+200-space),cross_wid)

def mark(row,col,player):
    board[row][col]=player

def available(row,col):
    if board[row][col] == 0:
        return True
    else:
        return False
    
def is_board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    #vertical win check
    for col in range (board_cols):
        if (board[0][col] == player) and (board[1][col] == player) and (board[2][col] == player):
            draw_vertical_line(col,player)
            return True
    #horizontal win check
    for row in range (board_rows):
        if (board[row][0] == player) and (board[row][1] == player) and (board[row][2] == player):
            draw_horizontal_line(row,player)
            return True
    #ascending diagonal win check
    if (board[2][0]==player) and (board[1][1]==player) and (board[0][2]==player):
        draw_ascending_diagonal(player)
        return True
    #ascending diagonal win check
    if (board[0][0]==player) and (board[1][1]==player) and (board[2][2]==player):
        draw_descending_diagonal(player)
        return True
    return False

def draw_vertical_line(col,player):
    posX = col*200+100
    if(player==1):
        color=circle_color
    elif(player==2):
        color=cross_color
    pygame.draw.line(screen,color,(posX,15),(posX,height-15),15)

def draw_horizontal_line(col,player):
    posY = col*200+100
    if(player==1):
        color=circle_color
    elif(player==2):
        color=cross_color
    pygame.draw.line(screen,color,(15,posY),(width-15,posY),15)

def draw_ascending_diagonal(player):
    if(player==1):
        color=circle_color
    elif(player==2):
        color=cross_color
    pygame.draw.line(screen,color,(15,height-15),(width-15,15),15)

def draw_descending_diagonal(player):
    if(player==1):
        color=circle_color
    elif(player==2):
        color=cross_color
    pygame.draw.line(screen,color,(15,15),(width-15,height-15),15)

def restart():
    screen.fill(light_blue)
    draw_line()
    player=1
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col]=0

draw_line()

player = 1
game_over=False

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row= int(mouseY//200)
            clicked_col= int(mouseX//200)

            if available (clicked_row,clicked_col):
                if player==1:
                    mark(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over = True
                    player=2

                elif player==2:
                    mark(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over = True
                    player=1

                draw_figure()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over=False
                restart()

    pygame.display.update()