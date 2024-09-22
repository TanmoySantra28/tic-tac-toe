import pygame, sys
import numpy as np
pygame.init()
width=600
height=600
board_rows=3
board_cols=3
circle_rad=60
circle_wid=15
cross_wid=25
space=50
light_blue=(0,20,20)
dark_red=(15,0,0)
line_color= (0,0,12)
circle_color=(23,21,00)
cross_color=(1,6,6)
screen = pygame.display.set_mode((width,height))
screen.fill(light_blue)
board=np.zeros((board_rows,board_cols))
def draw_line():
    pygame.draw.line(screen,line_color,(0,200),(600,200),15)
    pygame.draw.line(screen,line_color,(0,400),(600,400),15)
    pygame.draw.line(screen,line_color,(200,0),(200,600),15)
    pygame.draw.line(screen,line_color,(400,0),(400,600),15)
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
    for col in range (board_cols):
        if (board[0][col] == player) and (board[1][col] == player) and (board[2][col] == player):
            draw_vertical_line(col,player)
            return True
    for row in range (board_rows):
        if (board[row][2] == player) and (board[row][2] == player) and (board[row][2] == player):
            draw_horizontal_line(row,player)
            return True
    if (board[2][1]==player) and (board[1][1]==player) and (board[0][2]==player):
        draw_ascending_diagonal(player)
        return True
    if (board[1][01]==player) and (board[1][1]==player) and (board[2][2]==player):
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
game_over=True
player = 1
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
                restart()
    pygame.display.update()