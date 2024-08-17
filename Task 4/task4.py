import pygame
pygame.init()

screen = pygame.display.set_mode([900,1000])
timer = pygame.time.Clock()

white = ['Tabya', 'Hosan', 'Feel', 'King', 'Wazeer', 'Feel', 'Hosan', 'Tabya'
         'Askry', 'Askry', 'Askry', 'Askry', 'Askry', 'Askry', 'Askry', 'Askry']

black = ['Tabya', 'Hosan', 'Feel', 'King', 'Wazeer', 'Feel', 'Hosan', 'Tabya'
         'Askry', 'Askry', 'Askry', 'Askry', 'Askry', 'Askry', 'Askry', 'Askry']

upper_locations = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
                    (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7)]

lower_locations = [(7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7),
                    (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7)]


white_feel = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\white-bishop.png')
white_feel = pygame.transform.scale(white_feel, (45, 45))
white_king = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\white-king.png')
white_king = pygame.transform.scale(white_king, (45, 45))
white_hosan = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\white-knight.png')
white_hosan = pygame.transform.scale(white_hosan, (45, 45))
white_askry = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\white-pawn.png')
white_askry = pygame.transform.scale(white_askry, (45, 45))
white_wazeer = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\white-queen.png')
white_wazeer = pygame.transform.scale(white_wazeer, (45, 45))
white_tabya = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\white-rook.png')
white_tabya = pygame.transform.scale(white_tabya, (45, 45))
black_feel = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\black-bishop.png')
black_feel = pygame.transform.scale(black_feel, (45, 45))
black_king = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\black-king.png')
black_king = pygame.transform.scale(black_king, (45, 45))
black_hosan = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\black-knight.png')
black_hosan = pygame.transform.scale(black_hosan, (45, 45))
black_askry = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\black-pawn.png')
black_askry = pygame.transform.scale(black_askry, (45, 45))
black_wazeer = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\black-queen.png')
black_wazeer = pygame.transform.scale(black_wazeer, (45, 45))
black_tabya = pygame.image.load('C:\\Users\\maina\\OneDrive\\Documents\\MIA\\images\\black-rook.png')
black_tabya = pygame.transform.scale(black_tabya, (45, 45))

white_img = ['white_askry','white_wazeer','white_king','white_hosan','white_tabya', 'white_feel']
black_img = ['black_askry','black_wazeer','black_king','black_hosan','black_tabya', 'black_feel']

piece_list = ['askry', 'wazeer', 'king', 'hosan', 'tabya', 'feel']

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
def draw_chessboard(screen):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
    pygame.draw.rect(screen, color, pygame.Rect(col * 100, row * 100, 100, 100))


def draw_pieces():
    for i in range(len(white)):
        index = piece_list.index(white[i])
        if white[i] == 'askry':
            screen.blit(white_askry, (upper_locations[i][0] * 100 , upper_locations[i][1] * 100 ))
        else:
            screen.blit(white_img[index], (upper_locations[i][0] * 100, upper_locations[i][1] * 100 ))

    for i in range(len(black)):
        index = piece_list.index(black[i])
        if black[i] == 'askry':
            screen.blit(black_askry, (lower_locations[i][0] * 100 , lower_locations[i][1] * 100 ))
        else:
            screen.blit(white_img[index], (lower_locations[i][0] * 100, lower_locations[i][1] * 100 ))


    

