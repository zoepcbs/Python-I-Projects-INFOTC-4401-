import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Cherry Blossom Tree")
screen.tracer(0, 0) # un-comment for instant draw 

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.left(90)
t.up()
t.goto(0, -250)
t.down()
t.color("brown")
t.hideturtle()

def draw_branch(t, branch_length):
    if branch_length < 10:
        # Draw a pink blossom
        t.color(random.choice(["#FFC0CB", "#FFB6C1", "#FF69B4"]))
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        t.color("brown")
        return

    angle = random.randint(15, 25)
    shorten = random.uniform(0.7, 0.9)

    t.pensize(branch_length / 10)
    t.forward(branch_length)

    # Right branch
    t.right(angle)
    draw_branch(t, branch_length * shorten)

    # Left branch
    t.left(angle * 2)
    draw_branch(t, branch_length * shorten)

    # Return to original angle
    t.right(angle)
    t.backward(branch_length)

# Draw the tree
draw_branch(t, 100)

# Display the full image at once
screen.update()

turtle.done()
