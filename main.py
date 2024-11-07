import random
from pgzhelper import *

import pgzero
hucre= Actor("ground1")
screen_width =50
screen_height = 25 
WIDTH = hucre.width * screen_width
HEIGHT = hucre.height * screen_height
TITLE = "Roguelike"
FPS = 30 # Saniyedeki Kare Sayısı
menuArkaplan = Actor("menuarkaplan")
hucre2= Actor("ground2")
kenar = Actor("kenar")
player = Actor("karakter")
enemy = Actor("enemy",(hucre.width * 10,hucre.height * 10))

mode = "menu"
play = Actor("play")
sesacik = Actor("sesacik",(hucre.width*45,hucre.height*3))
sesacikmi = True




player_images = ['karakter', 'karakter2', 'karakter3']
player.images = player_images
#enem1_target_list = [(hucre.width* 10,hucre.height * 10),(hucre.width* 9,hucre.height * 10),(hucre.width* 8,hucre.height * 10),
#                     (hucre.width* 10,hucre.height * 9),(hucre.width* 9,hucre.height * 9),(hucre.width* 8,hucre.height * 9)]
enem1_target_list = [(10,10),(9,10),(8,10),
                       (10,9),(9,9),(8,9)]


map = [[2, 2, 2, 2, 2, 2, 2, 2, 2,2,2,2], 
          [2, 0, 0, 0, 1, 0, 0, 0, 0,0,0,2], 
          [2, 0, 0, 0, 0, 0, 0, 0, 0,0,0,2], 
          [2, 0, 1, 0, 0, 0, 0, 0, 0,0,0,2], 
          [2, 0, 0, 0, 0, 0, 0, 0, 0,0,0,2], 
          [2, 0, 1, 0, 0, 1, 0, 0, 0,0,0,2], 
          [2, 0, 0, 0, 0, 0, 0, 0, 0,0,0,2], 
          [2, 0, 0, 0, 0, 0, 0, 0, 0,0,0,2], 
          [2, 0, 0, 0, 0, 1, 0, 0, 0,0,0,2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0,0,0,2],
          [2, 2, 2, 2, 2, 2, 2, 2, 2,2,2,2]] 
def map_draw():
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                hucre.left = hucre.width*j
                hucre.top = hucre.height*i
                hucre.draw()
            elif map[i][j] == 1:
                hucre2.left = hucre2.width*j
                hucre2.top = hucre2.height*i
                hucre2.draw()
            elif map[i][j] == 2:
                kenar.left = kenar.width*j
                kenar.top = kenar.height*i
                kenar.draw()

kontrol = 0
def enemy_move():
    global kontrol
    if len(enem1_target_list)-1> kontrol:
        kontrol +=1
        
    else:
        kontrol = 0
    enemy.pos = enem1_target_list[kontrol][0] * hucre.width+ enemy.width / 2 , enem1_target_list[kontrol][1]* hucre.height+ enemy.height / 2





#music.play("muzik")
music.set_volume(0.2)
clock.schedule_interval(enemy_move, 1.0)
clock.schedule_interval(player.next_image, 0.5)
def draw():
    if mode == "menu":
        menuArkaplan.draw()
        play.draw()
        sesacik.draw()
    elif mode == "game":
        
            
        map_draw()
        player.draw()
        sesacik.draw()
        enemy.draw()
        screen.draw.text(str(kontrol),pos= (hucre.width*5,hucre.height*2))

def on_key_down(key):
    if keyboard.right:
        player.x += hucre.width
        
    elif keyboard.left:
        player.x -= hucre.width
        
    elif keyboard.up:
        player.y -= hucre.height
    elif keyboard.down:
        player.y += hucre.height

def on_mouse_down(pos, button):
    global sesacikmi,mode
    if mode == "menu":
        if button == mouse.LEFT and sesacik.collidepoint(pos):
            if sesacikmi == True:
                sesacikmi = False
                sesacik.image = "seskapali"
                music.pause()
            else:
                sesacikmi = True
                sesacik.image = "sesacik"
                music.unpause()
        elif button == mouse.LEFT and play.collidepoint(pos):
            mode = "game"
    elif mode == "game":
        if button == mouse.LEFT and sesacik.collidepoint(pos):
            if sesacikmi == True:
                sesacikmi = False
                sesacik.image = "seskapali"
                music.pause()
            else:
                sesacikmi = True
                sesacik.image = "sesacik"
                music.unpause()


def update(dt):
    #player.next_image()
    #enemy_move()
    if player.colliderect(enemy):
        #sounds.carpisma.play()
        pass