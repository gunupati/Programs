import turtle
t=turtle.Turtle()
ts=t.getscreen()
t.shape('turtle')
t.color('yellow')
def move():
    t.forward(2)

ts.onkey(move,'space')
ts.listen()
ts.mainloop()