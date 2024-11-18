import random
from pgzhelper import *
from move import Enemy
import pgzero
cell1= Actor("ground1")
screen_width =35
screen_height = 25 
WIDTH = cell1.width * screen_width
HEIGHT = cell1.height * screen_height
TITLE = "Roguelike"
FPS = 30 
# Enemys
enem1_target_list = [(10,10),(9,10),(8,10),
                       (10,9),(9,9),(8,9)]
enem2_target_list = [(20,20),(20,19),(20,18),(20,17),(20,16),(20,15),
                     (21,15),(22,15),(23,15),(24,15),
                     (24,16),(24,17),(24,18),(24,19),(24,20),
                     (23,20),(22,20),(21,20),(20,20)]

enemy_images = ["enemy","enemy1_2","enemy1_3"]
enemy2_images = ["wizard","enem2_2","enemy2_3"]

enemy = Actor("enemy", (160,160))
enemyy = Enemy(enem1_target_list,70,enemy,enemy_images,cell1.width,cell1.height,enemy.width,enemy.height)
enemy2 = Actor("wizard",(320,320))
enemyy2 = Enemy(enem2_target_list,100,enemy2,enemy2_images,cell1.width,cell1.height,enemy2.width,enemy2.height)

menuBackground = Actor("menuarkaplan")
cell2= Actor("ground2")
side = Actor("kenar")
player = Actor("karakter",topleft = (cell1.width * 1 ,cell1.height * 1))
x = Actor("x",(cell1.width * 28,cell1.height * 3))
mode = "menu"

potions = []
play = Actor("play",(WIDTH/2,HEIGHT/2))
sound = Actor("sesacik",(cell1.width*33,cell1.height*3))
soundOn = True
a = 0
b = 0
potion1 = Actor("potion",topleft =(cell1.width* 10,cell1.height*9))
potion2 = Actor("iksir",topleft = (cell1.width* 20,cell1.height*15))

potions.append(potion1)
potions.append(potion2)
player_pos = (0,0)

player_images = ['karakter', 'karakter2', 'karakter3']
player.images = player_images


cell2_rects = [] 
side_rects = [] 
map = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
    [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]
def map_draw():
    global cell2_rects,side_rects
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                cell1.left = cell1.width*j
                cell1.top = cell1.height*i
                cell1.draw()
            elif map[i][j] == 1:
                cell2.left = cell2.width*j
                cell2.top = cell2.height*i
                cell2.draw()
                cell2_rects.append(Rect((cell2.left, cell2.top), (cell2.width, cell2.height)))
            elif map[i][j] == 2:
                side.left = side.width*j
                side.top = side.height*i
                side.draw()
                side_rects.append(Rect((side.left, side.top), (side.width, side.height)))


music.play("muzik")
music.set_volume(0.2)
clock.schedule_interval(player.next_image, 0.5)
def draw():
    if mode == "menu":
        menuBackground.draw()
        play.draw()
        sound.draw()
        x.draw()
    elif mode == "game":
        map_draw()
        player.draw()
        sound.draw()
        enemyy.draw()
        enemyy2.draw()
        x.draw()
        for i in range(len(potions)):
            potions[i].draw()

def on_key_down(key):
    global player_x,player_y,player_pos
    player_x = player.x
    player_y = player.y
    player_pos = player.pos
    if keyboard.right and player.x < cell1.width*24:
        player.x += cell1.width
        
    elif keyboard.left and player.x > cell1.width *2:
        player.x -= cell1.width
        
    elif keyboard.up and player.y > cell1.height * 2:
        player.y -= cell1.height
    elif keyboard.down and player.y < cell1.height * 23 :
        player.y += cell1.height
def on_mouse_down(pos, button):
    global soundOn,mode
    if mode == "menu":
        if button == mouse.LEFT and sound.collidepoint(pos):
            if soundOn == True:
                soundOn = False
                sound.image = "seskapali"
                music.pause()
            else:
                soundOn = True
                sound.image = "sesacik"
                music.unpause()
        elif button == mouse.LEFT and play.collidepoint(pos):
            mode = "game"
            x.image = "x_game"
        elif button == mouse.LEFT and x.collidepoint(pos):
            exit()
    elif mode == "game":
        if button == mouse.LEFT and sound.collidepoint(pos):
            if soundOn == True:
                soundOn = False
                sound.image = "seskapali"
                music.pause()
            else:
                soundOn = True
                sound.image = "sesacik"
                music.unpause()
        elif button == mouse.LEFT and x.collidepoint(pos):
            mode = "menu"
            x.image = "x"

def update(dt):
    global mode
    enemyy.update(dt)
    enemyy2.update(dt)
    if mode == "game" and player.colliderect(enemy):
        if soundOn == True:
            sounds.carpisma.play()
        player.pos = (cell1.width* 1+ player.width /2 ,cell1.height* 1+ player.height/ 2)
    for i in range(len(potions)):
        if potions[i].colliderect(player):
            potions.pop(i)
            if soundOn == True:
                sounds.yutmasesi.play()
            player.image = "iksirtoplayincakarakter"
            break        
    for rect in cell2_rects:
        if player.colliderect(rect):
            player.pos = player_pos
        