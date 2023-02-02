import turtle

# Create a new turtle
cat = turtle.Turtle()

# Set the background color
turtle.bgcolor("white")

# Draw the head
cat.color("black")
cat.begin_fill()
cat.circle(50)
cat.end_fill()
cat.setheading(90)

# Draw the ears
cat.forward(25)
cat.right(90)
cat.forward(15)
cat.left(90)
cat.forward(25)
cat.left(90)
cat.forward(15)
cat.right(180)
cat.forward(30)
cat.right(90)
cat.forward(15)
cat.left(90)
cat.forward(30)

# Draw the eyes
cat.penup()
cat.setpos(-20, 20)
cat.pendown()
cat.dot(15, "blue")
cat.penup()
cat.setpos(20, 20)
cat.pendown()
cat.dot(15, "blue")

# Draw the nose
cat.penup()
cat.setpos(0, 0)
cat.pendown()
cat.dot(5, "black")

# Draw the mouth
cat.penup()
cat.setpos(-10, -20)
cat.pendown()
cat.right(45)
cat.forward(20)
cat.left(90)
cat.forward(20)
cat.left(45)

# Draw the body
cat.penup()
cat.setpos(0, -50)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(100)
cat.right(90)
cat.forward(100)
cat.right(90)
cat.forward(100)
cat.right(90)
cat.forward(50)
cat.end_fill()

# Draw the legs
cat.right(90)
cat.forward(50)
cat.left(45)
cat.forward(35)
cat.left(90)
cat.forward(35)
cat.right(180)
cat.forward(70)
cat.right(90)
cat.forward(35)
cat.left(45)
cat.forward(50)

# Hide the turtle
cat.hideturtle()

# Keep the window open
turtle.exitonclick()