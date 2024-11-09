from cmu_graphics import *

################################################################################
# Without OOP
################################################################################

# def onAppStart(app):
#     app.colors = ['green', 'blue', 'pink', 'gray']
#     app.dogs = []

# def onMousePress(app, mouseX, mouseY):
#     color = random.choice(app.colors)
#     dx, dy = random.randint(-5, 5), random.randint(-5, 5)
#     dog = [mouseX, mouseY, color, dx, dy]
#     app.dogs.append(dog)

# def onKeyPress(app, key):
#     if key == 'p':
#         print(app.dogs)
#     if key == 'space':
#         for dog in app.dogs:
#             dog[3] = random.randint(-5, 5)
#             dog[4] = random.randint(-5, 5)

# def onStep(app):
#     for dog in app.dogs:
#         dog[0] += dog[3]
#         dog[1] += dog[4]

# def drawDog(dog):
#     x, y, color, _, _ = dog
#     earsColor = "light" + color[0].upper() + color[1:]
#     drawCircle(x + 10, y - 10, 15, fill = earsColor)
#     drawCircle(x - 10, y - 10, 15, fill = earsColor)
#     drawCircle(x, y, 15, fill = color)
#     drawCircle(x + 4, y - 3, 3, fill = 'black')
#     drawCircle(x - 4, y - 3, 3, fill = 'black')
#     drawLine(x, y + 5, x, y + 13, fill = 'hotPink', lineWidth = 5)

# def redrawAll(app):
#     for dog in app.dogs:
#         drawDog(dog)

# def main():
#     runApp()
    
# main()

################################################################################
# With OOP 
################################################################################

# class Dog:

#     def __init__(self, x, y):
#         self.x, self.y = x, y
#         self.color = random.choice(['green', 'blue', 'pink', 'gray'])
#         self.dx, self.dy = random.randint(-5, 5), random.randint(-5, 5)

#     def changeDirection(self):
#         self.dx = random.randint(-5, 5)
#         self.dy = random.randint(-5, 5)
        
#     def walk(self):
#         self.x += self.dx
#         self.y += self.dy
        
#     def drawDog(self, app):
#         earsColor = "light" + self.color[0].upper() + self.color[1:]
#         drawCircle(self.x + 10, self.y - 10, 15, fill = earsColor)
#         drawCircle(self.x - 10, self.y - 10, 15, fill = earsColor)
#         drawCircle(self.x, self.y, 15, fill = self.color)
#         drawCircle(self.x + 4, self.y - 3, 3, fill = 'black')
#         drawCircle(self.x - 4, self.y - 3, 3, fill = 'black')
#         drawLine(self.x, self.y + 5, self.x, self.y + 13, fill = 'hotPink', lineWidth = 5)
        
#     # def __repr__(self):
#     #     return f"{self.color} doggo is running in ({self.dx}, {self.dy}) direction"

from dog import Dog

def onAppStart(app):
    app.dogs = []

def onMousePress(app, mouseX, mouseY):
    app.dogs.append(Dog(mouseX, mouseY))

def onKeyPress(app, key):
    if key == 'p':
        for dog in app.dogs:
            print(dog)
        print('------------')
    if key == 'space': 
        for dog in app.dogs:
            dog.changeDirection()

def onStep(app):
    for dog in app.dogs:
        dog.walk()

def redrawAll(app):
    for dog in app.dogs:
        dog.drawDog(app)

def main():
    runApp()
    
main()
