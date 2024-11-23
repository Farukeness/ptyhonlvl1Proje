class Enemy:
    def __init__(self, target_list,enemy,enemy_images):
        self.target_list = target_list 
        self.enemy = enemy
        self.enemy_images = enemy_images
        self.current_target = 0   
        self.start_number = 0  

    def update(self):
        target_x, target_y = self.target_list[self.current_target]        
        target_pos_x = target_x * 16 + 16 / 2
        target_pos_y = target_y * 16 + 16 / 2

        if len(self.target_list) - 1 >self.current_target:
            self.current_target += 1
        else:
            self.current_target = 0
        self.enemy.x = target_pos_x
        self.enemy.y = target_pos_y
        if len(self.enemy_images)-1>self.start_number:
            self.start_number +=1
        else:
            self.start_number = 0
        self.enemy.image = self.enemy_images[self.start_number]
        
class character_move:
    def __init__(self, actor,left_list,right_list):
        self.actor = actor  
        self.left_list = left_list
        self.right_list = right_list
        self.current_direction = "right"  
        self.start_number = 0
    def update_animation_new(self):
        if self.current_direction == "right":
            if len(self.right_list) -1 > self.start_number: 
                self.start_number +=1
            else:
                 self.start_number= 0
            self.actor.image = self.right_list[self.start_number]
            
        elif self.current_direction == "left":
             if len(self.left_list) -1 > self.start_number:
                 self.start_number +=1
             else:
                  self.start_number= 0
             self.actor.image = self.left_list[self.start_number]
    def move(self, direction):
        if direction == "left":
            self.actor.x -= 16
            self.current_direction = "left"
        elif direction == "right":
            self.actor.x += 16
            self.current_direction = "right"
        elif direction == "up":
            self.actor.y -= 16
        elif direction == "down":
            self.actor.y += 16

            
