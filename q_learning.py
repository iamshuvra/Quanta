import numpy as np
import random

class QLearning:
    def __init__(self, width, height, num_orientations, num_actions, lr=0.1, gamma=0.9, epsilon=0.2):
        self.qTable = np.zeros((width, height, num_orientations, num_actions))
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.num_actions = num_actions

    def choose_action(self, state):
        if random.random()<self.epsilon:
            return random.randint(0, self.num_actions-1)
        else:
            return np.argmax(self.qTable[state])
        
    def update(self,state, action, reward, next_state):
        max_future_q = np.max(self.qTable[next_state])
        current_q = self.qTable[state + (action,)]
        new_q = current_q + self.lr * (reward + self.gamma * max_future_q - current_q)
        self.qTable[state][action] = new_q
        return new_q
    
    