from cmu_graphics import *
import random

class Dog:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.color = random.choice(['green', 'blue', 'pink', 'gray'])
        self.dx, self.dy = random.randint(-5, 5), random.randint(-5, 5)

    def changeDirection(self):
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        
    def walk(self):
        self.x += self.dx
        self.y += self.dy
        
    def drawDog(self, app):
        earsColor = "light" + self.color[0].upper() + self.color[1:]
        drawCircle(self.x + 10, self.y - 10, 15, fill = earsColor)
        drawCircle(self.x - 10, self.y - 10, 15, fill = earsColor)
        drawCircle(self.x, self.y, 15, fill = self.color)
        drawCircle(self.x + 4, self.y - 3, 3, fill = 'black')
        drawCircle(self.x - 4, self.y - 3, 3, fill = 'black')
        drawLine(self.x, self.y + 5, self.x, self.y + 13, fill = 'hotPink', lineWidth = 5)
        
    # def __repr__(self):
    #     return f"{self.color} doggo is running in ({self.dx}, {self.dy}) direction"
