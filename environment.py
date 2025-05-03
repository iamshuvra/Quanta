import random

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacle = set()
        self.goal = (width-2, height-2)

    def generate_obstacles(self, num_obstacles):
        while len(self.obstacle) < num_obstacles:
            x = random.randint(1, self.width-1)
            y = random.randint(1, self.height-1)
            if (x, y) != self.goal and (x, y)!=self.goal:
                self.obstacle.add((x, y))

    def is_obstacle(self, x, y):
        return (x, y) in self.obstacle
    
    def is_goal(self, x, y):
        return (x, y) == self.goal