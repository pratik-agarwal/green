import turtle

def draw_square():
    window=turtle.Screen()
    window.bgcolor("green")

    cue=turtle.Turtle()
    for i in range(1,37):
        #picks the turtle
        
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
