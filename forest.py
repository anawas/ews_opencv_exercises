import cv2
import numpy as np
import random
from dataclasses import dataclass


class Tree:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def draw_tree(self, img):
        cv2.rectangle(img, (self.x, self.y), (self.x+10, self.y+50), (0,255,255), -1)
        cv2.ellipse(img, (self.x+5, self.y-35), (30, 50), 0, 0, 360, (0,160,0), -1)
        cv2.ellipse(img, (self.x+5, self.y-35), (30, 50), 0, 0, 360, (0,100,0), 3)

   
img = np.zeros((400,400, 3), dtype=np.uint8)
img[:200,:,:] = [255,0,0]
img[200:,:,:] = [0,255,0]

forest = []

for i in range(20):
    x = random.randint(50,350)
    y = random.randint(150,350)
    forest.append(Tree(x,y))

forest = sorted(forest, key=lambda tree: tree.y)
for tree in forest:
    print(tree.y)
    tree.draw_tree(img)


cv2.imshow("T", img)
cv2.waitKey(0)