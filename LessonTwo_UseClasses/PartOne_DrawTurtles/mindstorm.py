import turtle


def draw_square():

    #create the turtle
    ian_the_turtle = turtle.Turtle()
    ian_the_turtle.shape("turtle")
    ian_the_turtle.color("blue")
    ian_the_turtle.speed(1)
    

    #draw a square
    for totalSquares in range(0,36):
        for count in range(0,4):
            ian_the_turtle.forward(100)
            ian_the_turtle.right(90)
        ian_the_turtle.right(10)

    

def draw_circle():
    brandon_the_turtle = turtle.Turtle()
    brandon_the_turtle.shape("turtle")
    brandon_the_turtle.color("green")
    brandon_the_turtle.circle(100)

def draw_triangle():
    ashley_the_turtle = turtle.Turtle()
    ashley_the_turtle.shape("turtle")
    ashley_the_turtle.color("red")
    
    for count in range(0,3):
        ashley_the_turtle.forward(100)
        ashley_the_turtle.right(120)
    
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("black")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()

draw_shapes()

