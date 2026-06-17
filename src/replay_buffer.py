from collections import deque
import random
class ReplayBuffer:
    def __init__(self,cap=50000): self.buffer=deque(maxlen=cap)
    def push(self,*x): self.buffer.append(x)
    def sample(self,b): return random.sample(self.buffer,b)
    def __len__(self): return len(self.buffer)
