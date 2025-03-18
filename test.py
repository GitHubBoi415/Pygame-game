import pygame
import os
import sys
import time
import random
import threading

def resource_path(relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

def button_hovered_over(button):
    return button.x <= a <= button.x + button.width and button.y <= b <= button.y + button.height

def SC(screen):
    return (screen_type == screen)

def CX(width):
    return (screen.get_width()/2)-(width/2)

def CY(height):
    return (screen.get_height()/2)-(height/2)

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700

blockSize = 70

grid_array_info = [0] * 100

def imgFromNumber(number):
    actual_number = number
    # actual_number = (round(random_seed_list[grid_number]) + number) % 12
    match actual_number % 12:
        case 0:
            return bomb_img
        case 1:
            return blank_img
        case 2:
            return clock_img
        case 3:
            return dice_img
        case 4:
            return heal_img
        case 5:
            return blank_img
        case 6:
            return bomb_img
        case 7:
            return clock_img
        case 8:
            return dice_img
        case 9:
            return heal_img
        case 10:
            return blank_img
        case 11:
            return skull_img
        case _:
            return blank_img

def drawGrid():

    global random_seed_list

    # blockSize = 70 #Set the size of the grid block
    grid_xmin = round(CX(WINDOW_WIDTH))
    grid_ymin = round(CY(WINDOW_HEIGHT))
    x_counter = -1
    y_counter = -1
    for x in range(grid_xmin, grid_xmin + WINDOW_WIDTH, blockSize):
        x_counter += 1
        y_counter = -1
        for y in range(grid_ymin, grid_ymin + WINDOW_HEIGHT, blockSize):
            y_counter += 1
            grid_identification_number = (10*y_counter) + x_counter
            target = round((float(givetime()) + random_seed) * 0.01 * random_seed_list[grid_identification_number] + grid_identification_number) % 12
            if ((grid_array_info[grid_identification_number]) == 0):
                # screen.blit(imgFromNumber(random_seed + round(float(givetime()) * (0.1 * random_seed_list[grid_identification_number]) + (grid_identification_number + (random_seed_list[grid_identification_number]) * random_seed_list[grid_identification_number])) % 12), (x,y))
                screen.blit(imgFromNumber(target), (x,y))
                # screen.blit(imgFromNumber(1),(x,y))
            elif ((grid_array_info[grid_identification_number]) == 1):
                match int(target):
                    case 3:
                        print("ok")
                        random_seed_list = [random.randint(0, 99) for _ in range(100)]
                    case 8:
                        print("ok")
                        random_seed_list = [random.randint(0, 99) for _ in range(100)]
                    case _:
                        print(target)
                grid_array_info[grid_identification_number] = 2
                # you need to find a way to get the number the screen blit was on
            else:
                screen.blit(disabled_img,(x,y))

def wait_until_key_released(key):
    while pygame.key.get_pressed()[key]:
        pygame.event.pump() # Handle internal pygame events
        time.sleep(0.01)    # Small delay to prevent excessive CPU usage

def display_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    # return f"{hours:02}:{minutes:02}:{seconds:02}"
    return f"{seconds:02}"

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def givetime():
    return truncate(display_time(seconds_elapsed),3)

def fast_movement():
    keys = pygame.key.get_pressed()
    player_xmin_limit = round(CX(WINDOW_WIDTH))
    player_ymin_limit = round(CY(WINDOW_HEIGHT))
    if keys[pygame.K_w]:
        if (player_ymin_limit < player_pos.y):
            player_pos.y -= blockSize
        wait_until_key_released(pygame.K_w)
    if keys[pygame.K_s]:
        if (player_ymin_limit + 600 > player_pos.y):
            player_pos.y += blockSize
        wait_until_key_released(pygame.K_s)
    if keys[pygame.K_a]:
        if (player_xmin_limit < player_pos.x):
            player_pos.x -= blockSize
        wait_until_key_released(pygame.K_a)
    if keys[pygame.K_d]:
        if (player_xmin_limit + 600 > player_pos.x):
            player_pos.x += blockSize
        wait_until_key_released(pygame.K_d)
    if keys[pygame.K_SPACE]:
        ones = (player_pos.x - 242) / 70
        tens = ((player_pos.y - 92) / 70)
        select_target = (tens*10) + ones
        grid_array_info[int(select_target)] = 1
        print(select_target)

def movement_example():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print ("Space bar pressed down.")
            elif event.key == pygame.K_ESCAPE:
                print ("Escape key pressed down.")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print ("Space bar released.")
            elif event.key == pygame.K_ESCAPE:
                print ("Escape key released.")

def movement():
    player_xmin_limit = round(CX(WINDOW_WIDTH))
    player_ymin_limit = round(CY(WINDOW_HEIGHT))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            if (player_ymin_limit < player_pos.y):
                player_pos.y -= blockSize
        elif event.key == pygame.K_a:
            if (player_xmin_limit < player_pos.x):
                player_pos.x -= blockSize
        elif event.key == pygame.K_s:
            if (player_ymin_limit + 600 > player_pos.y):
                player_pos.y += blockSize
        elif event.key == pygame.K_d:
            if (player_xmin_limit + 600 > player_pos.x):
                player_pos.x += blockSize
        elif event.key == pygame.K_SPACE:
            ones = (player_pos.x - 242) / 70
            tens = ((player_pos.y - 92) / 70)
            select_target = (tens*10) + ones
            grid_array_info[int(select_target)] = 1

def parallel_process():
    while True:
        time.sleep(3)
# ----------

pygame.init()
screen = pygame.display.set_mode((480*2.5, 360*2.5))
clock = pygame.time.Clock()
running = True
screen_type = "Menu"
dt = 0
random_seed = random.randint(999, 999999)
random_seed_list = [random.randint(0, 99) for _ in range(100)]

pygame.display.set_caption('i love being able to edit what the pygame window says')

# WINDOWS
imagepath = os.path.abspath(__file__)[:-len(os.path.basename(__file__))] + "\images"

# MAC
# imagepath = 
# IMPORTANT!!! when distributing, use the lower line, the top one is for your personal 'puter
start_img = pygame.transform.scale(pygame.image.load(imagepath + '\start_btn.png').convert_alpha(),(60,700))
select_img = pygame.image.load(imagepath + '\Select.png')
blank_img = pygame.image.load(imagepath + '\Blank.png')
bomb_img = pygame.image.load(imagepath + '\Bomb.png')
clock_img = pygame.image.load(imagepath + '\Clock.png')
dice_img = pygame.image.load(imagepath + '\Dice.png')
heal_img = pygame.image.load(imagepath + '\Heal.png')
skull_img = pygame.image.load(imagepath + '\Skull.png')
disabled_img = pygame.image.load(imagepath + '\Disabled.png')
# start_img = pygame.image.load(resource_path('start_btn.png')).convert_alpha()

player_pos = pygame.Vector2((screen.get_width()/2) - 8, (screen.get_height()/2) - 8)

font = pygame.font.SysFont('Georgia',40,bold=True)
surf = font.render('Quit',True, 'white')
button = pygame.Rect(200,200,110,60)
button_2 = pygame.Rect(CX(110),CY(60),110,60)

# ----------

while running:
    screen.fill("purple")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                pygame.quit()
            if button_2.collidepoint(event.pos):
                screen_type = "Game"
                seconds_elapsed = 0
                randomizer_timer = 0
                # t = threading.Thread(target=parallel_process)
                # t.start()

        if SC("Game"):
            movement()

    a,b = pygame.mouse.get_pos()

    player_x = 0
    player_y = 0
    
    if SC("Menu"):
        if button_hovered_over(button):
            pygame.draw.rect(screen,(180,180,180),button)
        else:
            pygame.draw.rect(screen,(110,110,110),button)

        if button_hovered_over(button_2):
            pygame.draw.rect(screen,(180,180,180),button_2)
        else:
            pygame.draw.rect(screen,(110,110,110),button_2)
        screen.blit(surf,(button.x+5, button.y+5))
    if SC("Game"):

        # if (randomizer_timer < float(givetime())):
        #     random_seed_list = [random.randint(0, 99) for _ in range(100)]
        #     randomizer_timer += 1
        
        screen.blit(select_img, (player_pos))
        
        # egg = font.render(str(player_pos.x) + ' ' + str(player_pos.y),True, 'white')
        egg = font.render('fps: ' + str(clock)[11:16],True, 'white')
        screen.blit(egg,(0, 0))
        start_time = time.time()
        end_time = time.time()
        # elapsed_time = end_time - start_time
        # timer = font.render(f"Elapsed time: {elapsed_time:.2f} seconds",True, 'white')
        timer = font.render(f"Timer: " + str(givetime()),True, 'white')
        # timer = font.render(f"Timer: " + str(givetime()),3,True, 'white')
        screen.blit(timer,(0, 50))
        seconds_elapsed += dt
        drawGrid()

    # flip() the display to put your work on screen
    pygame.display.flip()
    # time.sleep(0.1)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()