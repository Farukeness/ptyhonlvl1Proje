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
