import pygame
import os
import sys
import time
import random

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
    match actual_number % 32:
        case 0:
            return clock_img
        case 1:
            return dice_img
        case 2:
            return reset_img
        case 3:
            return bomb_img
        case 4:
            return clock_img
        case 5:
            return bomb_img
        case 6:
            return dice_img
        case 7:
            return clock_img
        case 8:
            return dice_img
        case 9:
            return bomb_img
        case 10:
            return heal_img
        case 11:
            return skull_img
        case _:
            return blank_img

def drawGrid():

    global random_seed_list
    global timer_bonus
    global grid_swap_speed
    global player_health
    global running
    global screen_type

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
            target = round((float(givetime()) + random_seed) * (grid_swap_speed * 0.01) * random_seed_list[grid_identification_number] + grid_identification_number) % 32
            if ((grid_array_info[grid_identification_number]) == 0):
                # screen.blit(imgFromNumber(random_seed + round(float(givetime()) * (0.1 * random_seed_list[grid_identification_number]) + (grid_identification_number + (random_seed_list[grid_identification_number]) * random_seed_list[grid_identification_number])) % 12), (x,y))
                screen.blit(imgFromNumber(target), (x,y))
                # screen.blit(imgFromNumber(1),(x,y))
            elif ((grid_array_info[grid_identification_number]) == 1):
                match int(target):
                    case 0:
                        timer_bonus += 5
                    case 1:
                        random_seed_list = [random.randint(0, 99) for _ in range(100)]
                    case 2:
                        for i in range(100):
                            grid_array_info[i] = 0
                    case 3:
                        player_health -= 1
                    case 4:
                        timer_bonus += 5
                    case 5:
                        player_health -= 1
                    case 6:
                        random_seed_list = [random.randint(0, 99) for _ in range(100)]
                    case 7:
                        timer_bonus += 5
                    case 8:
                        random_seed_list = [random.randint(0, 99) for _ in range(100)]
                    case 9:
                        player_health -= 1
                    case 10:
                        player_health += 1
                    case 11:
                        screen_type = "Death"
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
    # minutes, seconds = divmod(seconds, 60)
    # hours, minutes = divmod(minutes, 60)
    # return f"{hours:02}:{minutes:02}:{seconds:02}"
    # return f"{seconds:02}"
    return seconds

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
        # THIS CODE DOESN'T ACTUALLY DO ANYTHING
        ones = (player_pos.x - 242) / 70
        tens = ((player_pos.y - 92) / 70)
        select_target = (tens*10) + ones
        if (grid_array_info[int(select_target)]) == 0:
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
        if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
            if (player_ymin_limit < player_pos.y):
                player_pos.y -= blockSize
        elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
            if (player_xmin_limit < player_pos.x):
                player_pos.x -= blockSize
        elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
            if (player_ymin_limit + 600 > player_pos.y):
                player_pos.y += blockSize
        elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
            if (player_xmin_limit + 600 > player_pos.x):
                player_pos.x += blockSize
        elif event.key == pygame.K_SPACE:
            ones = (player_pos.x - 242) / 70
            tens = ((player_pos.y - 92) / 70)
            select_target = (tens*10) + ones
            if (grid_array_info[int(select_target)]) == 0:
                grid_array_info[int(select_target)] = 1

def parallel_process():
    while True:
        time.sleep(3)

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def coordinates_touching(playerx,playery,sawbladex,sawbladey,range):
    x_range_min = playerx - range/2
    x_range_max = playerx + range/2
    y_range_min = playery - range/2
    y_range_max = playery + range/2
    if ((x_range_min < sawbladex < x_range_max) and (y_range_min < sawbladey < y_range_max)):
        return True
# ----------

pygame.init()
screen = pygame.display.set_mode((480*2.5, 360*2.5))
clock = pygame.time.Clock()
running = True
screen_type = "Menu"
dt = 0
random_seed = random.randint(999, 999999)
random_seed_list = [random.randint(0, 99) for _ in range(100)]
timer_bonus = 0
grid_swap_speed = 1
player_health = 5

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
reset_img = pygame.image.load(imagepath + '\Reset.png')
sawblade_img = pygame.image.load(imagepath + '\Sawblade.png')
end_tutorial_button = pygame.image.load(imagepath + '\End Tutorial Button.png')
end_tutorial_button_2 = pygame.image.load(imagepath + '\End Tutorial Button Hovered Over.png')
intro_tutorial_screen = pygame.image.load(imagepath + '\Intro Tutorial Screen.png')
death_screen = pygame.image.load(imagepath + '\Death Screen.png')
return_to_main_menu = pygame.image.load(imagepath + '\Return to Main Menu.png')
return_to_main_menu_hovered = pygame.image.load(imagepath + '\Return to Main Menu Hovered Over.png')
start_button_img = pygame.image.load(imagepath + '\START.png')
start_button_img_2 = pygame.image.load(imagepath + '\START_2.png')
# start_img = pygame.image.load(resource_path('start_btn.png')).convert_alpha()

player_pos = pygame.Vector2((screen.get_width()/2) - 8, (screen.get_height()/2) - 8)

font = pygame.font.SysFont('Georgia',40,bold=True)
surf = font.render('Quit',True, 'white')
button = pygame.Rect(50,50,110,60)
button_2 = start_button_img.get_rect()
# pygame.Rect(CX(110),CY(60),110,60)
button_2_x = CX(212 * 2)
button_2_y = CY(51 * 2)
button_2.center = (button_2_x + 212, button_2_y + 51)
button_3 = end_tutorial_button_2.get_rect()
button_3_x = 650
button_3_y = 40
button_3.center = (button_3_x + 248, button_3_y + 63)
button_4 = return_to_main_menu.get_rect()
button_4_x = CX(262*2)
button_4_y = 650
button_4.center = (button_4_x + 262, button_4_y + 45)
#pygame.Rect(CX(0),CY(-100),110,60)
sawbladeR_x = -100
sawbladeR_y = 92
sawbladeL_x = 1300
sawbladeL_y = 92 + (blockSize * 9)
sawbladeU_x = 242
sawbladeU_y = 1000
sawbladeD_x = 242 + (blockSize * 9)
sawbladeD_y = -100

# ----------

while running:
    screen.fill("black")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if SC("Menu"):
                if button.collidepoint(event.pos):
                    pygame.quit()
                if button_2.collidepoint(event.pos):
                    screen_type = "Tutorial"
                    # t = threading.Thread(target=parallel_process)
                    # t.start()
            if SC("Tutorial"):
                if button_3.collidepoint(event.pos):
                    screen_type = "Game"
                    seconds_elapsed = 0
                    randomizer_timer = 0
            if SC("Death"):
                if button_4.collidepoint(event.pos):
                    screen_type = "Menu"
                    random_seed = random.randint(999, 999999)
                    random_seed_list = [random.randint(0, 99) for _ in range(100)]
                    timer_bonus = 0
                    grid_swap_speed = 1
                    player_health = 5
                    for i in range(100):
                        grid_array_info[i] = 0
                    player_pos = pygame.Vector2((screen.get_width()/2) - 8, (screen.get_height()/2) - 8)

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
            screen.blit(start_button_img_2,(button_2_x + 0, button_2_y + 0))
            # pygame.draw.rect(screen,(180,180,180),button_2)
        else:
            screen.blit(start_button_img,(button_2_x + 0, button_2_y + 0))
            # pygame.draw.rect(screen,(110,110,110),button_2)
        screen.blit(surf,(button.x+5, button.y+5))
    if SC("Tutorial"):
        screen.blit(intro_tutorial_screen,(0,0))
        if button_hovered_over(button_3):
            screen.blit(end_tutorial_button_2,(button_3_x + 0, button_3_y + 0))
            # pygame.draw.rect(screen,(180,180,180),button_3)
        else:
            screen.blit(end_tutorial_button,(button_3_x + 0, button_3_y + 0))
            # pygame.draw.rect(screen,(110,110,110),button_3)
    if SC("Game"):

        # if (randomizer_timer < float(givetime())):
        #     random_seed_list = [random.randint(0, 99) for _ in range(100)]
        #     randomizer_timer += 1
        if (player_health <= 0):
            screen_type = "Death"
        screen.blit(select_img, (player_pos))
        grid_swap_speed = 1.0
        # egg = font.render(str(player_pos.x) + ' ' + str(player_pos.y),True, 'white')
        egg = font.render('fps: ' + str(clock)[11:16],True, 'white')
        screen.blit(egg,(0, 0))
        start_time = time.time()
        end_time = time.time()
        # elapsed_time = end_time - start_times
        # timer = font.render(f"Elapsed time: {elapsed_time:.2f} seconds",True, 'white')
        time_to_display = truncate((float(givetime()) + timer_bonus), 3)
        timer = font.render(f"Timer: " + str((time_to_display)),True, 'white')
        # timer = font.render(f"Timer: " + str(givetime()),3,True, 'white')
        health_display = font.render(f"HP: " + str((player_health)),True, 'white')
        screen.blit(timer,(0, 50))
        screen.blit(health_display,(0, 100))
        drawGrid()
        if (sawbladeR_x > 1300):
            sawbladeR_x = -100
            sawbladeR_y = (random.randint(0, 9) * blockSize) + 92
        if (sawbladeL_x < -100):
            sawbladeL_x = 1300
            sawbladeL_y = (random.randint(0, 9) * blockSize) + 92
        if (sawbladeU_y < -100):
            sawbladeU_x = (random.randint(0, 9) * blockSize) + 242
            sawbladeU_y = 1000
        if (sawbladeD_y > 1000):
            sawbladeD_x = (random.randint(0, 9) * blockSize) + 242
            sawbladeD_y = -100
        sawblade_speed = (float(seconds_elapsed)/5) + 2
        sawbladeR_x += sawblade_speed + 0.1
        sawbladeL_x -= sawblade_speed + 0.2
        sawbladeU_y -= sawblade_speed + 0.3
        sawbladeD_y += sawblade_speed + 0.4
        if (coordinates_touching(player_pos.x,player_pos.y,sawbladeR_x,sawbladeR_y,130)):
            player_health -= 1
            sawbladeR_x = 1300
        if (coordinates_touching(player_pos.x,player_pos.y,sawbladeL_x,sawbladeL_y,130)):
            player_health -= 1
            sawbladeL_x = -100
        if (coordinates_touching(player_pos.x,player_pos.y,sawbladeU_x,sawbladeU_y,130)):
            player_health -= 1
            sawbladeU_y = -100
        if (coordinates_touching(player_pos.x,player_pos.y,sawbladeD_x,sawbladeD_y,130)):
            player_health -= 1
            sawbladeD_y = 1000
        screen.blit(rot_center(sawblade_img, float(seconds_elapsed) * 1000),(sawbladeR_x,sawbladeR_y))
        screen.blit(rot_center(sawblade_img, float(seconds_elapsed) * 1000),(sawbladeL_x,sawbladeL_y))
        screen.blit(rot_center(sawblade_img, float(seconds_elapsed) * 1000),(sawbladeU_x,sawbladeU_y))
        screen.blit(rot_center(sawblade_img, float(seconds_elapsed) * 1000),(sawbladeD_x,sawbladeD_y))
        seconds_elapsed += dt
    if SC("Death"):
        screen.blit(death_screen,(0,0))
        time_to_display = truncate((float(givetime()) + timer_bonus), 3)
        timer_length = len("Final Time: " + str((time_to_display)))
        timer = font.render(f"Final Time: " + str((time_to_display)),True, 'white')
        screen.blit(timer,(CX(timer_length*20), CY(0)))
        if button_hovered_over(button_4):
            screen.blit(return_to_main_menu_hovered,(button_4_x + 0, button_4_y + 0))
        else:
            screen.blit(return_to_main_menu,(button_4_x + 0, button_4_y + 0))
        # running = False
        
    # flip() the display to put your work on screen
    pygame.display.flip()
    # time.sleep(0.1)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()