import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("green")

    #picks the turtle/initialize the turtle object
    cue=turtle.Turtle()
    for i in range(1,37):
        #use the object 'cue' to create a square and turn the turtle 10 degrees to create a new
        #square, thus creating a circle (36 times)
        cue.forward(100)
        cue.right(90)
        cue.forward(100)
        cue.right(90)
        cue.forward(100)
        cue.right(90)
        cue.forward(100)
        cue.right(90)
        cue.right(10)
    window.exitonclick()
draw_square()
