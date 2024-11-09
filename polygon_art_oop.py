import turtle
import random
from abc import ABC, abstractmethod

reduction_ratio = 0.618

class Shape:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        
    def get_random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def setup_screen(self):
        screen = turtle.Screen()
        screen.bgcolor('black')
        screen.colormode(255)
        turtle.tracer(0, 0)
        
    def random_position(self):
        return (random.randint(-300, 300), random.randint(-200, 200))

    def draw_polygon(self, num_sides, size, position, color, border_size=1, orientation=0):
        self.t.penup()
        self.t.goto(position)
        self.t.setheading(orientation)
        self.t.color(color)
        self.t.pensize(border_size)
        self.t.pendown()
        
        for _ in range(num_sides):
            self.t.forward(size)
            self.t.left(360/num_sides)
        self.t.penup()

class ArtGenerator(ABC):
    def __init__(self):
        self.shape = Shape()
        self.shape.setup_screen()
    
    @abstractmethod
    def generate(self):
        pass
        
    def cleanup(self):
        turtle.update()
        
class TriangleArt(ArtGenerator):
    def generate(self):
        for _ in range(30):
            pos = self.shape.random_position()
            color = self.shape.get_random_color()
            size = random.randint(30, 100)
            orientation = random.randint(0, 360)
            border_size = random.randint(1, 10)
            self.shape.draw_polygon(3, size, pos, color, border_size, orientation)

class RecursiveTriangle(ArtGenerator):
    def generate(self):
        for _ in range(30):
            pos = self.shape.random_position()
            color = self.shape.get_random_color()
            initial_size = random.randint(50, 150)
            size = initial_size
            border_size = random.randint(1, 10)

            for i in range(3):
                self.shape.draw_polygon(3, size, pos, color, border_size)
                size *= reduction_ratio

class SquareArt(ArtGenerator):
        def generate(self):
            for _ in range(30):
                pos = self.shape.random_position()
                color = self.shape.get_random_color()
                size = random.randint(30, 100)
                orientation = random.randint(0, 360)
                border_size = random.randint(1, 10)
                self.shape.draw_polygon(4, size, pos, color, border_size, orientation)

class RecursiveSquare(ArtGenerator):
    def generate(self):
        for _ in range(30):
            pos = self.shape.random_position()
            color = self.shape.get_random_color()
            initial_size = random.randint(50, 150)
            size = initial_size
            border_size = random.randint(1, 10)

            for i in range(3):
                self.shape.draw_polygon(4, size, pos, color, border_size)
                size *= reduction_ratio

class PentagonArt(ArtGenerator):
    def generate(self):
        for _ in range(30):
            pos = self.shape.random_position()
            color = self.shape.get_random_color()
            size = random.randint(30, 100)
            orientation = random.randint(0, 360)
            border_size = random.randint(1, 10)
            self.shape.draw_polygon(5, size, pos, color, border_size, orientation)

class RecursivePentagon(ArtGenerator):
    def generate(self):
        for _ in range(30):
            pos = self.shape.random_position()
            color = self.shape.get_random_color()
            initial_size = random.randint(50, 150)
            size = initial_size
            border_size = random.randint(1, 10)

            for i in range(3):
                self.shape.draw_polygon(5, size, pos, color, border_size)
                size *= reduction_ratio

class RandomArt(ArtGenerator):
    def generate(self):
        for _ in range(30):
            pos = self.shape.random_position()
            color = self.shape.get_random_color()
            size = random.randint(30, 100)
            orientation = random.randint(0, 360)
            border_size = random.randint(1, 10)
            num_sides = random.randint(3,5)
            self.shape.draw_polygon(num_sides, size, pos, color, border_size, orientation)

class RecursiveRandom(ArtGenerator):
    def generate(self):
        for _ in range(30):
            pos = self.shape.random_position()
            color = self.shape.get_random_color()
            initial_size = random.randint(50, 150)
            size = initial_size
            border_size = random.randint(1, 10)
            num_sides = random.randint(3,5)

            for i in range(3):
                self.shape.draw_polygon(num_sides, size, pos, color, border_size)
                size *= reduction_ratio

class RecursiveTrueRandom(ArtGenerator):
    def generate(self):
        for _ in range(30):
            pos = self.shape.random_position()
            color = self.shape.get_random_color()
            initial_size = random.randint(50, 150)
            size = initial_size
            border_size = random.randint(1, 10)
            num_sides = random.randint(3,5)

            for i in range(random.randint(1, 3)):
                self.shape.draw_polygon(num_sides, size, pos, color, border_size)
                size *= reduction_ratio


num = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))

pentagon = PentagonArt()
recursive_pentagon = RecursivePentagon()
triangle = TriangleArt()
recursive_triangle = RecursiveTriangle()
square = SquareArt()
recursive_square = RecursiveSquare()
random_art = RandomArt()
recursive_random = RecursiveRandom()
recursive_true_random = RecursiveTrueRandom()

if num == 1:
    triangle.generate()
    turtle.done()
elif num == 2:
    square.generate()
    turtle.done()
elif num == 3:
    pentagon.generate()
    turtle.done()
elif num == 4:
    random_art.generate()
    turtle.done()
elif num == 5:
    recursive_triangle.generate()
    turtle.done()
elif num == 6:
    recursive_square.generate()
    turtle.done()
elif num == 7:
    recursive_pentagon.generate()
    turtle.done()
elif num == 8:
    recursive_random.generate()
    turtle.done()
elif num == 9:
    recursive_true_random.generate()
    turtle.done()