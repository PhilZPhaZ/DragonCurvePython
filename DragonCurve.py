from importlib.resources import path
from tkinter import messagebox
import turtle
from typing import final

# set up the screen
screen = turtle.Screen()
screen.title('Dragon Curve')
screen.setup(width=1920, height=1080)

# set up the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, 0)
t.color('red')
t.hideturtle()


# create a class to find the path
class findPath:
    def __init__(self, n):
        self.l = 0
        self.r = 1
        self.list_iteration = [1]
        self.create_list(n, self.list_iteration)

    # Create a reverse function
    def reverse_list(self, l):
        return l[::-1]


    def create_list(self, n, list_iteration):
        for i in range(n):
            self.old_list = list(self.reverse_list(self.list_iteration))
            self.list_iteration.append(self.r)
            for x in range(len(self.old_list)):
                if self.old_list[x] == self.l:
                    self.old_list[x] = self.r
                else:
                    self.old_list[x] = self.l
            self.list_iteration = self.list_iteration + self.old_list

    
    def get_list(self):
        return self.list_iteration

def start():
    n = int(turtle.numinput("Dragon Curve", "Enter the number of iterations:"))
    path = findPath(n).get_list()
    t.pd()
    
    for i in range(len(path)):
        if path[i] == 1:
            t.circle(4, 90, 36)
        elif path[i] == 0:
            t.circle(-4, 90, 36)
        
start()
screen.mainloop()