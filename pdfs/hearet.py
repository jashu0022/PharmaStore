import turtle

t = turtle.Turtle()

t.speed(10)

t.color("red", "pink")

t.penup()
t.goto(0,0)
t.pendown()
t.setheading(135)
t.begin_fill()
t.forward(150)
t.circle(-75, 180)

t.penup()
t.goto(0,0)

t.pendown()
t.setheading(45)
t.forward(150)
t.circle(75, 180)
t.end_fill()

t.color("green")
t.penup()
t.goto(-100, 0)
t.pendown()
for i in range(5):
    t.forward(30)
    t.left(144)
    t.begin_fill()
    for j in range(5):
        t.forward(10)
        t.left(72)
    t.end_fill()

t.penup()
t.goto(100, 0)
t.pendown()
for i in range(5):
    t.forward(30)
    t.left(144)
    t.begin_fill()
    for j in range(5):
        t.forward(10)
        t.left(72)
    t.end_fill()

t.color("red")
t.penup()
t.goto(0, -150)

text = "\x49 \x6C\x6F\x76\x65 \x79\x6F\x75 \x62\x61\x62\x79\n\x59\x6F\x75\x27\x72\x65 \x6D\x79 \x6C\x69\x66\x65\x2C \x49\x27\x6D \x6E\x6F\x74\x68\x69\x6E\x67 \x77\x69\x74\x68\x6F\x75\x74 \x79\x6F\x75"
t.write(text, align="center", font=("Arial", 20, "bold"))

turtle.done()
