# import requests 
# import json
# endpoint = " http://127.0.0.1:8000/"

# data = {
#     "title":"This field is done"
# }

# get_response = requests.get(endpoint, json=data)
# print(type(get_response))
# print(get_response.json())


import pygame,random
from pygame.locals import*
screen_width = 800
screen_height = 800
pygame.init()
game_display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
board_size = 3
player1 = 1
player2 = 2
##startx = 150
##endx = 650
##vertical_start_x = 300
##vertical_end_x = 500
##vertical_start_y = 100
##vertical_end_y = 500
##hor_start_x = 150
##hor_start_y = 100 + 400//3
##hor_end_x = 650
##hor_end_y = 100 + 800//3
def draw_board(board):
    game_display.fill(white)
    pygame.draw.line(game_display, black, (300,100), (300,700))
    pygame.draw.line(game_display, black, (500,100), (500,700))
    pygame.draw.line(game_display, black, (100,300),(700,300))
    pygame.draw.line(game_display, black, (100,500),(700,500))
    for x in range(board_size):
        for y in range(board_size):
            if board[x][y] == player1:
                pygame.draw.circle(game_display, red, (200 + 200 * x, 200 + 200 * y),50,1)            
            elif board[x][y] == player2:
                pygame.draw.line(game_display, blue, (100 + x * 200 + 50, 100 + y * 200 + 50),(300 + 200 * x - 50, 300 + 200 * y - 50))
                pygame.draw.line(game_display, blue ,(300 + 200 * x - 50, 100 + y * 200 + 50),(100 + 200 * x + 50, 300 + 200 * y - 50))
    
    pygame.display.update()
    clock.tick()

def get_board():
    board = []
    for i in range(board_size):
        board.append([None]*board_size)
    return board

def text_objects(text,font,color):
    text_surf = font.render(text, True, color)
    return text_surf,text_surf.get_rect()

def is_win(board,player):
    for x in range(board_size):
        for y in range(board_size-2):
            if board[x][y] == board[x][y+1] == board[x][y+2] == player:
                return True

    for x in range(board_size - 2):
        for y in range(board_size):
            if board[x][y] == board[x+1][y] == board[x+2][y] == player:
                return True

    for x in range(board_size - 2):
        for y in range(board_size - 2):
            if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == player:
                return True

    if board[2][0] == board[1][1] == board[0][2] == player:
        return True

    return False


def is_tie(board):
    for x in range(board_size):
        for y in range(board_size):
            if board[x][y] != None:
                return False
    return True
            
def play():
    board = get_board()
    if random.randint(0,1)==1:
        turn = player2
    else:
        turn = player1
    while True:
        draw_board(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if turn == player1:
            board = get_player_move(board,player1)
            turn = player2
            if is_win(board,player1):
                text = 'Player 1 Wins'
                break
        elif turn == player2:
            board = get_player_move(board,player2)
            turn = player1
            if is_win(board,player2):
                text = 'Player 2 Wins'
                break
        if is_tie(board):
            text = 'It''s a tie'
            break
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                play()
        text_name = pygame.font.Font('freesansbold.ttf',55)
        text_surf,text_rect = text_objects(text,text_name,black)
        text_rect.center = ((400,50))
        game_display.blit(text_surf, text_rect)
        pygame.display.update()
        clock.tick()


def get_player_move(board,player):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                posx,posy = event.pos
                if 100 < posx < 7000 and 100 < posy < 700:
                    col = (posx - 100)//200
                    row = (posy - 100)//200
                    if board[col][row] == None:
                        board[col][row] = player
                        draw_board(board)
                        return board
    return board
play()