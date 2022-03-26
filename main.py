import pygame
from random import randint
import time
start_time = time.time()
pygame.init()
# Constants:
WIDTH = 700
HEIGHT = 650
SHIP_Y_POS = HEIGHT-70
SHIP_X_SPEED = 7
SHIP_SIZE = (75, 50)
SHIP_IMG = r'spaceship.png'
INV_IMG = r'invader.png'
INV_SIZE = (50,40)
INV_Y_SPEED = 1
INV_X_SPEED = 2
ROCKET_Y_SPEED = 2
display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
display_surface.fill((255,255,255))
clock = pygame.time.Clock()
SCORE = 0
GAME_STATE = True

class ship:
    def __init__(self, x_pos):
        self.img = pygame.image.load(SHIP_IMG)
        self.img = pygame.transform.scale(self.img, SHIP_SIZE)
        self.x_speed = SHIP_X_SPEED
        self.x_pos = x_pos
        self.y_pos = SHIP_Y_POS
# ship is ship(Naturel)
# a space ship with img and x position and y position and horizontal speed
ship = ship(WIDTH/2)
# def fn_for_ship(s):
#     s.img
#     s.x_pos
#     s.y_pos
#     s.x_speed

class invader:
    def __init__(self, pos, direction=1):
        self.img = pygame.image.load(INV_IMG)
        self.img = pygame.transform.scale(self.img, INV_SIZE)
        self.x_speed = INV_X_SPEED * direction
        self.y_speed = INV_Y_SPEED
        self.x_pos = pos[0]
        self.y_pos = pos[1]
# invader is invader(tuple(Naturel,Naturel))
# an invader with img and passing coordinate as tuples and x , y velocity
invader_obj = invader((100,100))
# def fn_for_invader(i):
#     i.img
#     i.x_pos
#     i.y_pos
#     i.x_speed
#     i.y_speed

class rocket:
    def __init__(self, pos):
        self.y_speed = ROCKET_Y_SPEED
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.img = pygame.Rect(self.x_pos,self.y_pos,10,10)
# rocket is rocket(tuple(Naturel,Naturel))
# a rocket with img and passing coordinate as tuples and y_speed
rocket_obj = rocket((30,30))
# def fn_for_invader(r):
#     r.img
#     r.x_pos
#     r.y_pos
#     r.y_speed

# list of invaders
loinv = []
# loinv.append(invader_obj)
# def fn_for_loinv(loinv):
#   for i in loinv:
#       t

# list of rockets
loroc = []
# loroc.append(rocket_obj)
# def fn_for_loro(loro):
#     for i in loro:
#         t

# function:
# loinv, loro, ship  ->  image
# a function that takes a list of invaders and list of rockets and ship and draw the in tha screen
def draw(linv, loroc, ship):
    fill()
    draw_ship(ship)
    draw_invaders(linv)
    draw_rockets(loroc)
    print_score()
# fill is a subfunction of draw it takes nothing and preduce a white screen
def fill():
    display_surface.fill((255,255,255))
# draw_ship is subfunction of draw it takes a ship and draw it in tha screen
# take template from ship
def draw_ship(s):
    display_surface.blit(s.img, (s.x_pos, s.y_pos))
# draw_invaders is subfunction of draw it takes a list of invaders and draw them in tha screen
# take template from loinv and invader
def draw_invaders(loinv):
    for i in loinv:
        display_surface.blit(i.img, (i.x_pos, i.y_pos))
# draw_rockets is subfunction of draw it takes a list of rockets and draw them in tha screen
# take template from loiro and rocket
def draw_rockets(lorc):
    for i in lorc:
        i.img.y = i.y_pos
        pygame.draw.rect(display_surface,(0,0,0),i.img, border_radius=7)

# draw_score is a subfunction of draw it draws the score in the the top left corner
def print_score():
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(f'{SCORE}', True, (0,0,0), (255,255,255))
    textRect = text.get_rect()
    textRect.center = (30, 20)
    display_surface.blit(text, textRect)

# ship  ->  ship
# a function that take a ship and change its position and preduce the new ship
def move_ship(s, event):
    if event.text == "l" and cross_border(s) != 1:
        s.x_pos += s.x_speed
    elif event.text == "k" and cross_border(s) != -1:
        s.x_pos -= s.x_speed
# cross_border is a sub function of move_ship it check if the ship crosses the border and return 0 if not 1 if on the right side -1 if in the left side
def cross_border(s):
    if s.x_pos <= 0:
        return -1
    if s.x_pos + SHIP_SIZE[0] >= WIDTH:
        return 1
    return 0
# loroc  ->  loroc
# a function that takes loroc and ship and preduce add a rocket is the same pos as ship to loroc
def create_rocket(loroc, s):
    loroc.append(rocket((s.x_pos+ SHIP_SIZE[0]/2, s.y_pos)))

# loroc  ->  loroc
# a function that takes loroc and substrate y_speed from their y_pos remove if some is out of screen
def move_rockets(loroc):
    for i in loroc:
        i.y_pos -= i.y_speed
        remove_out_screen(i, loroc)
# remove_out_screen is a subfunction that takes a rocket and remove it from loroc if it is out of screen
def remove_out_screen(i, loroc):  
    if i.y_pos < 0:
        loroc.remove(i)

# loinv  ->  loinv
# a function that take loinv and add an invader is random x_pos[0, WIDTH] and random direction (left or right)
def create_invaders(loinv):
    y = 0
    x = randint(0, WIDTH)
    direction = randint(0, 1)
    if not direction:
        loinv.append(invader((x,y),-1))
    else:
        loinv.append(invader((x,y),1))
# loinv  ->  loinv
# a function that take loinv and change the pos by speeds and check if collision with wal switch the direction of x_speed (multiply it by -1)
def move_invader(loinv):
    for i in loinv:
        check_collision(i)
        i.x_pos += i.x_speed
        i.y_pos += i.y_speed
# check_collision is a subfunction of move_invader it and checks if collision with wal switch the direction of x_speed (multiply it by -1)
def check_collision(inv):
    if inv.x_pos<0:
        inv.x_pos = 0
        inv.x_speed *= -1
    if inv.x_pos+INV_SIZE[0]> WIDTH:
        inv.x_pos = WIDTH-INV_SIZE[0]
        inv.x_speed *= -1

# loinv, loroc  ->  loinv, loroc
# a function that takes loinv, loroc and check if a rocket get in an invader and update the score

def check_kill(loinv, loroc):
    global SCORE
    for i in loroc:
        for j in loinv:
            if j.y_pos<=i.y_pos<=j.y_pos+INV_SIZE[0] and j.x_pos<=i.x_pos<=j.x_pos+INV_SIZE[1]:
                loinv.remove(j)
                loroc.remove(i)
                SCORE += 1

# loinv, loroc -> loinv, loroc
# check_bottom_collision IS A FUNCTION THAT TAKES loin and check if an invader reached the bottom
# take template from loinv
def check_bottom_collision(loinv, loroc):
    global GAME_STATE, SCORE
    for i in loinv:
        if i.y_pos+INV_SIZE[0] >= HEIGHT:
            GAME_STATE = False
            fill()
            print_game_over()
            loinv.clear()
            loroc.clear()
            SCORE = 0

# print_game_over is a function that print "GAME OVER" in the screen
def print_game_over():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('GAME OVER', True, (255,0,0), (255,255,255))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    display_surface.blit(text, textRect)


while True:
    if GAME_STATE:
        draw(loinv, loroc, ship)
        move_rockets(loroc)
        move_invader(loinv)
        check_kill(loinv, loroc)
        check_bottom_collision(loinv, loroc)
        if time.time() - start_time > 1:
            create_invaders(loinv)
            start_time = time.time()
        clock.tick(60)
        pygame.display.flip()
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        if GAME_STATE:
            if event.type == 771:
                move_ship(ship, event)
            if event.type == 768 and event.key == 13:
                # pressing enter means shot
                create_rocket(loroc, ship)
        # restart when pressing enter
        elif event.type == 768 and event.key == 13:
            GAME_STATE = True