# 2  Часть Исскуственный Интеллект
import pygame
import random
import moviepy.editor


lang = int(input('Enter the language: 1 - English, 2 - Russian '))
if lang == 1:
    Endless = input('Do you want to play in Endless mode? True/False: ')
if lang == 2:
    Endless = input('Вы хотите играть в режиме Бесконечности? True/False: ')
if lang == 567256:
    lang = 1
    print('Dev mode is ON, please wait...')
    Endless = input('Do you want to play in Endless mode? True/False: ')
    room = int(input('Enter room number: '))
else:
    room = 0


# Параметры окна
width = 900
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SPOOKY'S JUMPSCARE MANSION 2D DEMAKE")
clock = pygame.time.Clock()
FPS = 60
Door_triger_E = 800
Door_triger_S = 600

# Переменные
Character = pygame.image.load('Character.png')
Door = pygame.image.load('DoorTriger.png')
Beef_png = pygame.image.load('ezgif-3-ff66a457af.png')
Beef_png2 = pygame.image.load('ezgif-1-096bfc2334.png')
Heart = pygame.image.load('ezgif-6-54f6e96153.png')
Icon = pygame.image.load('menu_tex.png')
pygame.display.set_icon(Icon)
Slow = 6
Stamine = 400
Speed = 5
X = 0
Y = 500
Attacking = False
stamine_weight = 100
stamine_height = 10
health = 100
property_Stamine = 400
Gel = 9999
Gel2 = 9999
Food_demon = 9999
Food_demon2 = 9999
Beaver = 9999
Beaver2 = 9999

Rooms = room

Rooms_desinge = random.randint(1, 4)
Timer = 0
Ambience_2 = pygame.mixer.Sound('1-34. Dum loopy thing.mp3')
Bloop_Attack = pygame.mixer.Sound('1-11. UNKNOWN_HUG.mp3')
Beef_Attack = pygame.mixer.Sound('We_Have_The_Beef.mp3')
Healing = pygame.mixer.Sound('fortnite-care.mp3')
Beaver_Attack = pygame.mixer.Sound('hallway-ambiance-extended-five-nights-at-freddys-2-music.mp3')
# Текст
font = pygame.font.Font('freesansbold.ttf', 20)
door_font = pygame.font.SysFont('8bitwonderrusbylyajka_nominal.ttf', 20)
room_font = pygame.font.SysFont('8bitwonderrusbylyajka_nominal.ttf', 30)

# Флаги
flag_Spain_help = False
flag_Door_help = False
no_tips = False

# Spooky
spooky_number_iter = 0
img_list_spooky = [] # Список изображений
for i in range(9):
    img_spooky = pygame.image.load("frame_"+str(i)+"_delay-0.08s.png")
    img_list_spooky.append(img_spooky)
spooky_appear_widht = -110
spooky_appear_height = 300
#Bloop
bloop_number_iter = 0
img_list_bloop = [] # Список изображений
for i in range(5):
    img_bloop = pygame.image.load("bloop_frame_"+str(i)+"_delay-0.1s.png")
    img_list_bloop.append(img_bloop)
bloop_appear_widht = -110
husk_appear_height = 500
# Food Demon
food_demon_number_iter = 0
img_list_food_demon = [] # Список изображений
for i in range(10):
    img_food_demon = pygame.image.load("demon_frame_0"+str(i)+"_delay-0.07s.png")
    img_list_food_demon.append(img_food_demon)
food_demon_appear_widht = -110
food_demon_appear_height = 400
# Troch
troch_number_iter = 0
img_list_troch = [] # Список изображений
for i in range(6):
    img_troch = pygame.image.load("torch_frame_"+str(i)+"_delay-0.13s.png")
    img_list_troch.append(img_troch)
# Beaver
beaver_number_iter = 0
img_list_beaver = [] # Список изображений
for i in range(4):
    img_beaver = pygame.image.load("beaver_frame_"+str(i)+"_delay-0.15s.png")
    img_list_beaver.append(img_beaver)
beaver_appear_widht = -110
beaver_appear_height = 500

# Приколы со временем
flag_time_spooky_reavel = 0

# Цикл
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        X += Speed
        Speed = 5
        if keys[pygame.K_LSHIFT] and Stamine >= 0:
            Speed = 10
            Stamine -= 20
            stamine_weight -= 5
    if keys[pygame.K_a]:
        X -= Speed
        Speed = 5
        if keys[pygame.K_LSHIFT] and Stamine >= 0:
            Speed = 10
            Stamine -= 20
            stamine_weight -= 5
    if keys[pygame.K_h] and keys[pygame.K_e] and keys[pygame.K_l] and keys[pygame.K_p]:
        health = 100
        Fps = 24
        video = moviepy.editor.VideoFileClip("Mesmerizer.mp4")
        video.preview()
        pygame.quit()
    if keys[pygame.K_w] and keys[pygame.K_a] and keys[pygame.K_y]:
        health = 100
        Fps = 24
        video = moviepy.editor.VideoFileClip("SillyBilly.mp4")
        video.preview()
        pygame.quit()
    if keys[pygame.K_h] and keys[pygame.K_e] and keys[pygame.K_s] and keys[pygame.K_o]:
        health = 100
        Ambience_2.stop()
        if Rooms >= Gel and Rooms <= Gel2 - Rooms and Attacking == False:
            Bloop_Attack.stop()
            Healing.play()
            Bloop_Attack.play()
        if Rooms >= Food_demon and Rooms <= Food_demon2 - Rooms and Attacking == False:
            Beef_Attack.stop()
            Healing.play()
            Beef_Attack.play()
        if Rooms >= Beaver and Rooms <= Beaver2 - Rooms and Attacking == False:
            Beaver_Attack.stop()
            Healing.play()
            Beaver_Attack.play()
        Healing.set_volume(0.1)
        Healing.play()
        Ambience_2.play()
    if keys[pygame.K_b] and keys[pygame.K_e] and keys[pygame.K_a] and keys[pygame.K_r]:
        video = moviepy.editor.VideoFileClip("Мем с медведем который подходит к камере ОАОАООАОАОАОАОРАА-(480p).mp4")
        video.preview()
        pygame.quit()
    if keys[pygame.K_e] and X >= Door_triger_E:
        if Rooms >= 60 and Attacking == False:
            Gel = random.randint(Rooms, Rooms+20)
            Gel2 = random.randint(Rooms, Rooms+20)
        if Rooms >= 120 and Attacking == False:
            Food_demon = random.randint(Rooms, Rooms+20)
            Food_demon2 = random.randint(Rooms, Rooms+20)
        if Rooms >= 200 and Attacking == False:
            Beaver = random.randint(Rooms, Rooms+20)
            Beaver2 = random.randint(Rooms, Rooms+20)
        Rooms_desinge = random.randint(1, 10)
        X = 0
        Y = 500
        Rooms += 1
        if Attacking == True:
            food_demon_appear_widht = random.randint(X, 900)
            beaver_appear_widht = -110
    if keys[pygame.K_s] and keys[pygame.K_a] and keys[pygame.K_v] and keys[pygame.K_e]:
        print(Rooms, X)
    # Обработка событий
    spooky_number_iter += 1
    Stamine += 10
    flag_time_spooky_reavel += 1
    bloop_number_iter += 1
    food_demon_number_iter += 1
    health += 0.1
    Timer += 1
    troch_number_iter += 1
    beaver_number_iter += 1
    # Обновление экрана
    if Stamine > property_Stamine:
        Stamine = property_Stamine
    if Stamine <= 0:
        Stamine = 0
        Speed = 5
    screen.fill((255, 255, 255))
    if stamine_weight < 100:
        stamine_weight += 1
    if stamine_weight < 0:
        stamine_weight = 0
    elif stamine_weight > 100:
        stamine_weight = 100
    if health >= 100:
        health = 100
    # Не выходи за рамки дозволенного!
    if X < 0:
        X = 0
    if X > 850:
        X = 850
    # Поведение дверей
    if X >= Door_triger_S:
        if no_tips == False:
            if lang == 1:
                if Rooms_desinge == 3 or Rooms_desinge == 8 or Rooms_desinge == 5 or Rooms_desinge == 10:
                    tips = door_font.render('To open door press E', True, (255, 255, 255))
                else:
                    tips = door_font.render('To open door press E', True, (0, 0, 0))
            if lang == 2:
                if Rooms_desinge == 3 or Rooms_desinge == 8 or Rooms_desinge == 5 or Rooms_desinge == 10:
                    tips = door_font.render('Дверь открыть на E', True, (255, 255, 255))
                else:
                    tips = door_font.render('Дверь открыть на E', True, (0, 0, 0))
            flag_Door_help = True
    # Отрисовка
    # Cчётчик Дверей
    if lang == 1:
        rooms_apper = room_font.render(f'Room {Rooms}', True, (255, 215, 0))
    if lang == 2:
        rooms_apper = room_font.render(f'Комната {Rooms}', True, (255, 215, 0))
    Ambience_2.set_volume(0.000001)
    # Spooky 1 первый раз
    if flag_time_spooky_reavel == 180 and Rooms <= 10:
        flag_time_spooky_reavel = 180
        pygame.mixer.init()
        Ambience_2.stop()
        pygame.mixer.music.load('Spooky_01.mp3')
        pygame.mixer.music.set_volume(10)
        pygame.mixer.music.play(1)
    if flag_time_spooky_reavel > 1780:
        spooky_appear_widht += 3
    if spooky_appear_widht <= 400:
        spooky_appear_widht += 3
    # Рандомайзер комнат
    if Rooms_desinge == 1:
        pygame.draw.rect(screen, (128, 128, 128), (0, 0, 900, 250))
        pygame.draw.rect(screen, (105, 105, 105), (0, 250, 900, 600))
        pygame.draw.rect(screen, (128, 128, 128), (0, 600, 900, 600))
    elif Rooms_desinge == 2:
        pygame.draw.rect(screen, (82, 58, 107), (0, 0, 900, 250))
        pygame.draw.rect(screen, (56, 40, 74), (0, 250, 900, 600))
        pygame.draw.rect(screen, (82, 58, 107), (0, 600, 900, 600))
    elif Rooms_desinge == 3:
        pygame.draw.rect(screen, (38, 37, 45), (0, 0, 900, 250))
        pygame.draw.rect(screen, (38, 38, 46), (0, 250, 900, 600))
        pygame.draw.rect(screen, (38, 37, 45), (0, 600, 900, 600))
    elif Rooms_desinge == 4:
        pygame.draw.rect(screen, (110, 64, 9), (0, 0, 900, 250))
        pygame.draw.rect(screen, (61, 36, 5), (0, 250, 900, 600))
        pygame.draw.rect(screen, (110, 64, 9), (0, 600, 900, 600))
    elif Rooms_desinge == 12:
        pygame.draw.rect(screen, (168, 168, 168), (0, 0, 900, 250))
        pygame.draw.rect(screen, (143, 143, 143), (0, 250, 900, 600))
        screen.blit(Beef_png2, (150, 250))
        screen.blit(Beef_png2, (650, 250))
        screen.blit(Beef_png2, (400, 250))
        screen.blit(Beef_png, (200, 500))
        pygame.draw.rect(screen, (168, 168, 168), (0, 600, 900, 600))
    elif Rooms_desinge == 5 and Attacking == False:
        pygame.draw.rect(screen, (62, 61, 74), (0, 0, 900, 250))
        pygame.draw.rect(screen, (38, 38, 46), (0, 250, 900, 600))
        pygame.draw.rect(screen, (62, 61, 74), (0, 600, 900, 600))
        screen.blit(Door, (200, 500))
    if Rooms_desinge == 6:
        pygame.draw.rect(screen, (128, 128, 128), (0, 0, 900, 250))
        pygame.draw.rect(screen, (105, 105, 105), (0, 250, 900, 600))
        pygame.draw.rect(screen, (128, 128, 128), (0, 600, 900, 600))
        number_frame_troch = troch_number_iter // 6 % 3
        screen.blit(img_list_troch[number_frame_troch], (800, 500))
    elif Rooms_desinge == 7:
        pygame.draw.rect(screen, (82, 58, 107), (0, 0, 900, 250))
        pygame.draw.rect(screen, (56, 40, 74), (0, 250, 900, 600))
        pygame.draw.rect(screen, (82, 58, 107), (0, 600, 900, 600))
        number_frame_troch = troch_number_iter // 6 % 3
        screen.blit(img_list_troch[number_frame_troch], (100, 500))
        screen.blit(img_list_troch[number_frame_troch], (800, 500))
    elif Rooms_desinge == 8:
        pygame.draw.rect(screen, (38, 37, 45), (0, 0, 900, 250))
        pygame.draw.rect(screen, (38, 38, 46), (0, 250, 900, 600))
        pygame.draw.rect(screen, (38, 37, 45), (0, 600, 900, 600))
        number_frame_troch = troch_number_iter // 6 % 3
        screen.blit(img_list_troch[number_frame_troch], (450, 500))
    elif Rooms_desinge == 9:
        pygame.draw.rect(screen, (110, 64, 9), (0, 0, 900, 250))
        pygame.draw.rect(screen, (61, 36, 5), (0, 250, 900, 600))
        pygame.draw.rect(screen, (110, 64, 9), (0, 600, 900, 600))
    elif Rooms_desinge == 10:
        pygame.draw.rect(screen, (62, 61, 74), (0, 0, 900, 250))
        pygame.draw.rect(screen, (38, 38, 46), (0, 250, 900, 600))
        pygame.draw.rect(screen, (62, 61, 74), (0, 600, 900, 600))
        screen.blit(Door, (200, 500))
        number_frame_troch = troch_number_iter // 6 % 3
        screen.blit(img_list_troch[number_frame_troch], (150, 500))

    # Здоровье
    pygame.draw.rect(screen, (0, 255, 0), (0, 10, stamine_weight, stamine_height))
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, health, 10))
    # Персы и аннимация
    number_frame_spooky = spooky_number_iter // 6 % 9
    number_frame_bloop = bloop_number_iter // 6 % 5
    number_frame_demon = food_demon_number_iter // 6 % 10
    number_frame_beaver = beaver_number_iter // 6 % 4
    screen.blit(img_list_spooky[number_frame_spooky], (spooky_appear_widht, 300))
    screen.blit(Door, (0, 500))
    screen.blit(Door, (850, 500))
    screen.blit(Character, (X, Y))
    # Приколы с помощью
    if flag_Door_help == True:
        screen.blit(tips, (700, 400))
        flag_Door_help = False
    # AI и Появление врагов
    if Rooms >= Gel and Rooms <= Gel2 - Rooms and Attacking == False:
        Attacking = True
        number_frame_bloop = bloop_number_iter // 6 % 5
        screen.blit(img_list_bloop[number_frame_bloop], (bloop_appear_widht, 400))
        Ambience_2.stop()
        Bloop_Attack.set_volume(0.1)
        Bloop_Attack.play()
        if bloop_appear_widht > X:
            bloop_appear_widht -= 1
        else:
            bloop_appear_widht +=1
        if bloop_appear_widht == X - 25 or bloop_appear_widht == X - 50 or bloop_appear_widht == X:
            health -= 45
            screen.fill((255, 0, 0))
        if health <= 0:
            pygame.mixer.music.stop()
            video = moviepy.editor.VideoFileClip("0518(1).mp4")
            video.preview()
            pygame.quit()
    else:
        Attacking = False
        Ambience_2.play()
        Bloop_Attack.stop()
    if Rooms >= Food_demon and Rooms <= Food_demon2 and Attacking == False:
        Attacking = True
        Rooms_desinge = 12
        number_frame_demon = food_demon_number_iter // 6 % 10
        screen.blit(img_list_food_demon[number_frame_demon], (food_demon_appear_widht, 300))
        Ambience_2.stop()
        Beef_Attack.set_volume(0.1)
        Beef_Attack.play()
        if food_demon_appear_widht > X:
            food_demon_appear_widht -= 4
        else:
            food_demon_appear_widht += 4
        if food_demon_appear_widht == X - 25 or food_demon_appear_widht == X - 50 or food_demon_appear_widht == X:
            health -= 45
            screen.fill((255, 0, 0))
        if health <= 0:
            health -= 0.1
            Beef_Attack.stop()
            pygame.draw.rect(screen, (255, 0, 0), (0, 0, 900, 900))
            if X == 600:
                if lang == 1:
                    print(f'{Timer} how long have you lived')
                if lang == 2:
                    print(f'{Timer} это сколько ты прожил')
                video = moviepy.editor.VideoFileClip("05181.mp4")
                video.preview()
                pygame.quit()
    else:
        Attacking = False
        Ambience_2.play()
        Beef_Attack.stop()
    if Rooms >= Beaver and Rooms <= Beaver2 and Attacking == False:
        Rooms_desinge = 8
        Attacking = True
        number_frame_beaver = beaver_number_iter // 6 % 4
        screen.blit(img_list_beaver[number_frame_beaver], (beaver_appear_widht, 420))
        Ambience_2.stop()
        Beaver_Attack.set_volume(0.1)
        Beaver_Attack.play()
        if beaver_appear_widht > X:
            beaver_appear_widht -= 6
        else:
            beaver_appear_widht += 6
        if beaver_appear_widht == X - 25 or beaver_appear_widht == X - 50 or beaver_appear_widht == X:
            health -= 15
            screen.fill((255, 0, 0))
        if health <= 0:
            health -= 0.1
            Beaver_Attack.stop()
            Ambience_2.stop()
            if X == 600:
                health -= 0.1
                X+=1
                if lang == 1:
                    print(f'{Timer} how long have you lived')
                if lang == 2:
                    print(f'{Timer} это сколько ты прожил')
                video = moviepy.editor.VideoFileClip("0518.mp4")
                video.preview()
    else:
        Attacking = False
        Ambience_2.play()
        Beaver_Attack.stop()
    if Rooms == 99:
        spooky_appear_widht = -110
        if spooky_appear_widht <= 400:
            spooky_appear_widht += 1
        Attacking = True
        pygame.mixer.init()
        Ambience_2.stop()
        pygame.mixer.music.load('Spooky_02.mp3')
        pygame.mixer.music.set_volume(10)
        pygame.mixer.music.play(1)
    if Rooms >= 15:
        Ambience_2.play()
        Ambience_2.set_volume(0.1)
    if Endless == 'False':
        if Rooms == 1000:
            Rooms_desinge = 4
            health = 0
            spooky_appear_widht = -120
            screen.blit(Heart, (X+25, Y+50))
            Character = pygame.image.load('Char_Dead.png')
            Ambience_2.stop()
            Door_triger_E = 950
            Door_triger_S = 950
            if X >= 850:
                if lang == 2:
                    print('Извините, я не успел доделать концовку по этому вот')
                if lang == 1:
                    print('Sorry, I have no time for this scene')
                video = moviepy.editor.VideoFileClip("051911.mp4")
                video.preview()
                if lang == 1:
                    video = moviepy.editor.VideoFileClip("0519.mp4")
                    video.preview()
                    pygame.quit()
                if lang == 2:
                    video = moviepy.editor.VideoFileClip("05191.mp4")
                    video.preview()
                    pygame.quit()
    if Endless == 'True':
        if Rooms == 1000:
            Door_triger_E = 800
            Door_triger_S = 600
            Character = pygame.image.load('Character.png')
            Ambience_2.play()
    screen.blit(rooms_apper, (700, 0))
    print(Rooms_desinge)
    pygame.display.flip()
pygame.quit()