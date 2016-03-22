import turtle


def draw_square():

    #create the turtle
    ian_the_turtle = turtle.Turtle()
    ian_the_turtle.shape("turtle")
    ian_the_turtle.color("blue")
    

    #draw a square
    for totalSquares in range(0,36):
        for count in range(0,4):
            ian_the_turtle.forward(100)
            ian_the_turtle.right(90)
        ian_the_turtle.right(10)

def draw_stem():
    bob_the_turtle = turtle.Turtle()
    bob_the_turtle.shape("turtle")
    bob_the_turtle.color("green")
    bob_the_turtle.speed(1)
    bob_the_turtle.right(90)
    bob_the_turtle.forward(250)


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("black")
    draw_square()
    draw_stem()
    window.exitonclick()

draw_flower()

