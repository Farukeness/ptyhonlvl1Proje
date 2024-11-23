import random
from pgzhelper import *
from move import Enemy,character_move

import pgzrun
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
railcar_target_list = [(14,5),(14,6),(14,7),(14,8),(14,9),(14,10),(14,11),(14,12)]

enemy_images = ["enemy","enemy1_2","enemy1_3"]
enemy2_images = ["wizard","enem2_2","enemy2_3"]
railcar_images = ["railcar","railcar2"]
enemy = Actor("enemy", (160,160))
enemyy = Enemy(enem1_target_list,enemy,enemy_images)
enemy2 = Actor("wizard",(320,320))
enemyy2 = Enemy(enem2_target_list,enemy2,enemy2_images)
railcar = Actor("railcar",topleft =( cell1.width * 14,cell1.height*5))
railcarr = Enemy(railcar_target_list,railcar,railcar_images)
clock.schedule_interval(enemyy.update,0.4)
clock.schedule_interval(enemyy2.update,0.1)
clock.schedule_interval(railcarr.update,0.3)
#Player
character_left_moves = ["player_left","player_left2","player_left3"]
character_right_moves = ["player_right","player_right2","player_right3"]
player = Actor("character",topleft = (cell1.width * 1 ,cell1.height * 1))
player_move = character_move(player,character_left_moves,character_right_moves)
player_start_pos = (16* 1+8 ,16* 1+ 8)
clock.schedule_interval(player_move.update_animation_new,0.1)

#Buttons
x = Actor("x",topleft = (cell1.width * 34,cell1.height * 0))
mode = "menu"
play = Actor("play",(WIDTH/2,HEIGHT/2))
play_again = Actor("play_again",(WIDTH/2,HEIGHT/2))

sound = Actor("sound_on",topleft = (cell1.width*30,cell1.height*0))

#Map
cell2= Actor("ground2")
side = Actor("side")
side2 = Actor("side2")
fence = Actor("fence")
leftside = Actor("left_side")
menuBackground = Actor("menubackground")
gameoverbackground = Actor("game_over_background")
wingame = Actor("win_background")
rail = Actor("rail")
leftdoor = Actor("leftdoor",topleft = (cell1.width*25,cell1.height * 7))
rightdoor = Actor("rightdoor",topleft = (cell1.width*26,cell1.height * 7))

#Potions
potion1 = Actor("potion",topleft =(cell1.width* 10,cell1.height*9))
potion2 = Actor("potion2",topleft = (cell1.width* 20,cell1.height*15))
potions = []
def potions_add():
    potions.append(potion1)
    potions.append(potion2)
potions_add()
#hearts
hearts = []
heart = Actor("heart",topleft = (cell1.width * 25,cell1.height*0))
heart2 = Actor("heart",topleft = (cell1.width * 24,cell1.height*0))
heart3 = Actor("heart",topleft = (cell1.width * 23,cell1.height*0))
def hearts_add():
    hearts.append(heart)
    hearts.append(heart2)
    hearts.append(heart3)
hearts_add()
#win
gain = []
#sounds
music.play("muzik")
music.set_volume(0.2)
gameSound = False
soundOn = True
succesSound = False
tadaSound = False
#map draw
cell2_rects = [] 
map = [
    [5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,3,3,3,3,3,3,3,3,2], 
    [5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,2], 
    [5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,3,3,3,3,3,3,3,3,2]
]
def map_draw():
    global cell2_rects
    
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
            elif map[i][j] == 3:
                side2.left = side.width*j
                side2.top = side.height*i
                side2.draw()
            elif map[i][j] == 4:
                rail.left = rail.width*j
                rail.top = rail.height*i
                rail.draw()
            elif map[i][j] == 5:
                leftside.left = leftside.width*j
                leftside.top = leftside.height*i
                leftside.draw()
def default_settings(pos,mod="menu"):
    global soundOn,mode
    if sound.collidepoint(pos):
            if soundOn == True:
                soundOn = False
                sound.image = "sound_off"
                music.pause()
            else:
                soundOn = True
                sound.image = "sound_on"
                music.unpause()
    elif  x.collidepoint(pos):
            if mod == "game":
                mode = "menu"
                x.image = "x"
            else:
                exit()
def default_set2(pos):
    if play_again.collidepoint(pos):
        global mode,succesSound,tadaSound
        mode = "menu"
        x.image = "x_game"
        hearts.clear()
        hearts_add()
        potions_add()
        gain.clear()
        player.pos = player_start_pos
        potion1.pos = (16 * 10 + 16 / 2, 16 * 9+ 16 / 2)
        potion2.pos = (16 * 20 + 16 / 2, 16 * 15+ 16 / 2)          
        leftdoor.image = "leftdoor"
        rightdoor.image = "rightdoor"
        succesSound = False
        tadaSound = False
def collect_potion():
    for i in range(len(potions)):
        if potions[i].colliderect(player):
            potions[i].pos = (16 *(21 +i) + 8,16*0+8)
            gain.append(potions[i])
            
            if soundOn == True:
                sounds.yutmasesi.play()
            player.image = "character_with_potions"
            break        
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
        enemy.draw()
        enemy2.draw()
        x.draw()
        railcar.draw()
        leftdoor.draw()
        
        rightdoor.draw()
        for i in range(len(potions)):
            potions[i].draw()
        for i in range(len(hearts)):
            hearts[i].draw()
        for i in range(len(gain)):
            gain[i].draw()
    elif mode == "game_over":
        gameoverbackground.draw()
        sound.draw()
        x.draw()
        play_again.draw()
    elif mode == "game_win":
        wingame.draw()
        sound.draw()
        x.draw()
        play_again.draw()

def on_mouse_down(pos):
    global mode
    if mode == "menu":
        default_settings(pos)
        if play.collidepoint(pos):
            mode = "game"
            x.image = "x_game"
            
    elif mode == "game":
        default_settings(pos,"game")
        
    elif mode == "game_over":
        default_settings(pos)
        default_set2(pos)
            
    elif mode == "game_win":
        default_settings(pos)
        default_set2(pos)


def on_key_down(key):
    global player_pos
    player_pos = player.pos
    if keyboard.right and player.x < cell1.width*33 :
        player_move.move("right")
        
    elif keyboard.left and player.x > cell1.width *2:
        player_move.move("left")
        
    elif keyboard.up and player.y > cell1.height * 2:
        player_move.move("up")
    elif keyboard.down and player.y < cell1.height * 23 :
        player_move.move("down")
    for rect in cell2_rects:
        if player.colliderect(rect):
            player.pos = player_pos 

def update(dt):
    global mode,gameSound,succesSound,tadaSound
    if mode == "game":
        #colliderects
        if player.colliderect(enemy) or player.colliderect(enemy2):
            if soundOn == True:
                sounds.carpisma.play()
            player.pos = player_start_pos
            
            hearts.pop()
        elif player.colliderect(leftdoor) or player.colliderect(rightdoor):
            if leftdoor.image == "leftopendoor":
                mode = "game_win"
            
            if tadaSound == False and soundOn == True:
                tadaSound = True
                sounds.tada.play()
    collect_potion()
    
    #game over
    if len(hearts) <=0:
        mode = "game_over"
        gain.clear()
        x.image = "x"
        if soundOn == True and gameSound == False:
            sounds.game_over.play() 
            gameSound = True
    #game win
    if len(gain) ==2:
        if soundOn == True and succesSound == False:
            sounds.success.play()
            succesSound = True
        leftdoor.image = "leftopendoor"
        rightdoor.image = "rightopendoor"

pgzrun.go()