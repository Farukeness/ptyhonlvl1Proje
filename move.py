class Enemy:
    def __init__(self, target_list, speed, sprite, animation_frames,cell_width,cell_height,enemy_width,enemy_height):
        self.target_list = target_list 
        self.speed = speed
        self.sprite = sprite
        self.animation_frames = animation_frames
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.enemy_width = enemy_width
        self.enemy_height = enemy_height
        self.current_frame = 0
        self.current_target = 0
        self.position = [x_y * 16 for x_y in target_list[0]]
        self.animation_timer = 0

    def update(self, dt):
        target_x, target_y = self.target_list[self.current_target]

        
        target_pos_x = target_x * self.cell_width + self.enemy_width / 2
        target_pos_y = target_y * self.cell_height + self.enemy_height / 2

        if self.position[0] < target_pos_x:
            self.position[0] += self.speed * dt
            if self.position[0] > target_pos_x:  
                self.position[0] = target_pos_x
        elif self.position[0] > target_pos_x:
            self.position[0] -= self.speed * dt
            if self.position[0] < target_pos_x:  
                self.position[0] = target_pos_x

        if self.position[1] < target_pos_y:
            self.position[1] += self.speed * dt
            if self.position[1] > target_pos_y: 
                self.position[1] = target_pos_y
        elif self.position[1] > target_pos_y:
            self.position[1] -= self.speed * dt
            if self.position[1] < target_pos_y: 
                self.position[1] = target_pos_y

        
        if self.position[0] == target_pos_x and self.position[1] == target_pos_y:
            self.current_target = (self.current_target + 1) % len(self.target_list)
            

        
        self.animation_timer += dt
        if self.animation_timer >= 0.1:  
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.animation_timer = 0

        self.sprite.pos = self.position

    def draw(self):
        self.sprite.image = self.animation_frames[self.current_frame]
        self.sprite.draw()



class character_move:
    def __init__(self, actor,left_list,right_list,cell_width,cell_height):
        self.actor = actor  
        self.animations = {  
            "left": left_list,
            "right": right_list
        }
        self.left_list = left_list
        self.right_list = right_list
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.default_img = right_list[0]  
        self.c_direction = "right"  
        self.c_frame = 0  
        self.animation_time = 0.1  
        self.time = 0  

    def update_animation(self, dt):
        frames = self.animations.get(self.c_direction, [self.default_img])
        if len(frames) > 1:
            self.time += dt
            if self.time >= self.animation_time:
                self.c_frame = (self.c_frame + 1) % len(frames)
                self.actor.image = frames[self.c_frame]
                self.time = 0

    def move(self, direction):
        
        if direction in ["left", "right"]:
            self.c_direction = direction
            if direction == "left":
                self.actor.x -= self.cell_width  
            elif direction == "right":
                self.actor.x += self.cell_height 

            
            self.c_frame = 0
            self.actor.image = self.animations[direction][self.c_frame]
        elif direction in ["up", "down"]:
            if direction == "up":
                self.actor.y -= 16
            elif direction == "down":
                self.actor.y += 16

            
            self.actor.image = self.default_img
