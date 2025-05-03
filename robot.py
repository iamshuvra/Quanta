class Robot:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.orientation = 0
    
    def get_state(self):
        return (self.x, self.y, self.orientation)
    
    def turn_left(self):
        self.orientation = (self.orientation+ 1) % 4

    def turn_right(self):
        self.orientation = (self.orientation - 1) % 4

    def move_forward(self):
        if self.orientation == 0:
            return self.x+1, self.y
        elif self.orientation == 1:
            return self.x, self.y+1
        elif self.orientation == 2:
            return self.x-1, self.y
        elif self.orientation == 3:
            return self.x, self.y-1
        else:
            raise ValueError("Invalid orientation")
    
    def update_position(self, x, y):
        self.x = x
        self.y = y

    def reset(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.orientation = 0
        self.update_position(start_x, start_y)