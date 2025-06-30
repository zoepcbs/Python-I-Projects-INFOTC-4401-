
import turtle
import math
import random
import colorsys
import time

# Screen setup
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Animated Parametric Butterfly in the Night Sky")
screen.tracer(0, 0) #un-comment for instant draw

# Colors for butterfly wings
def get_iridescent_color(t):
    # Create shifting colors based on parameter t
    r = 0.8 + 0.2 * math.sin(t/2)
    g = 0.5 + 0.5 * math.sin(t/2 + 2)
    b = 0.8 + 0.2 * math.sin(t/2 + 4)
    return (r, g, b)

# Draw moon with craters
def draw_moon(x, y, radius):
    moon = turtle.Turtle()
    moon.speed(0)
    moon.penup()
    moon.goto(x, y - radius)
    moon.color("light yellow")
    moon.begin_fill()
    moon.circle(radius)
    moon.end_fill()
    
    # Draw craters
    moon.color("khaki")
    for _ in range(5):
        crater_x = x + random.randint(-int(radius*0.7), int(radius*0.7))
        crater_y = y + random.randint(-int(radius*0.7), int(radius*0.7))
        crater_size = random.randint(int(radius*0.1), int(radius*0.25))
        moon.penup()
        moon.goto(crater_x, crater_y - crater_size)
        moon.begin_fill()
        moon.circle(crater_size)
        moon.end_fill()
    
    moon.hideturtle()

# Draw twinkling stars
def draw_stars(count, width, height):
    stars = []
    for _ in range(count):
        star = turtle.Turtle()
        star.hideturtle()
        star.speed(0)
        star.color("white")
        star.penup()
        x = random.randint(-width//2 + 50, width//2 - 50)
        y = random.randint(-height//2 + 50, height//2 - 50)
        star.goto(x, y)
        size = random.randint(1, 3)
        star.dot(size)
        
        # Add to stars list for twinkling animation
        stars.append((star, size, random.random()))
    
    return stars

# Animate twinkling stars
def twinkle_stars(stars):
    for star, original_size, phase in stars:
        # Create a twinkling effect with sine wave
        twinkle_factor = 0.5 + 0.5 * math.sin(time.time() * 2 + phase * 10)
        size = original_size * twinkle_factor
        star.clear()
        star.dot(size)

# Draw parametric butterfly curve with color gradient
def draw_parametric_butterfly(t_val=0):
    butterfly = turtle.Turtle()
    butterfly.speed(0)
    butterfly.pensize(2)
    butterfly.hideturtle()
    
    scale = 80
    t = 0.0
    
    # Calculate initial position
    x = scale * math.sin(t) * (math.exp(math.cos(t)) - 2 * math.cos(4*t) - math.pow(math.sin(t/12), 5))
    y = scale * math.cos(t) * (math.exp(math.cos(t)) - 2 * math.cos(4*t) - math.pow(math.sin(t/12), 5))
    
    butterfly.penup()
    butterfly.goto(x, y)
    butterfly.pendown()
    
    # Draw the butterfly with iridescent colors
    points = []
    
    while t < 12 * math.pi:
        x = scale * math.sin(t) * (math.exp(math.cos(t)) - 2 * math.cos(4*t) - math.pow(math.sin(t/12), 5))
        y = scale * math.cos(t) * (math.exp(math.cos(t)) - 2 * math.cos(4*t) - math.pow(math.sin(t/12), 5))
        points.append((x, y))
        t += 0.05
    
    # Draw the butterfly with colors
    for i, (x, y) in enumerate(points):
        progress = i / len(points)
        # Use iridescent colors based on progress and animation parameter
        color = get_iridescent_color(progress * 10 + t_val)
        butterfly.pencolor(color)
        butterfly.goto(x, y)
    
    return butterfly

# Butterfly body
def draw_body():
    body = turtle.Turtle()
    body.speed(0)
    body.hideturtle()
    
    # Draw body
    body.penup()
    body.goto(0, -40)
    body.pensize(8)
    body.color("black")
    body.setheading(90)
    body.pendown()
    body.forward(80)
    
    # Draw antennae
    body.penup()
    body.goto(0, 40)
    body.pensize(2)
    body.color("dark gray")
    
    # Left antenna
    body.setheading(150)
    body.pendown()
    body.forward(30)
    body.dot(3)
    
    # Right antenna
    body.penup()
    body.goto(0, 40)
    body.setheading(30)
    body.pendown()
    body.forward(30)
    body.dot(3)

# Draw spiral galaxy
def draw_spiral_galaxy(x, y, size=1.0, angle=0):
    galaxy = turtle.Turtle()
    galaxy.hideturtle()
    galaxy.speed(0)
    galaxy.penup()
    galaxy.goto(x, y)
    galaxy.setheading(angle)
    
    # Draw the core
    galaxy.dot(size * 8, "white")
    
    # Draw spiral arms
    for arm in range(2):  # Two spiral arms
        galaxy.penup()
        galaxy.goto(x, y)
        galaxy.setheading(angle + arm * 180)
        galaxy.pendown()
        
        # Draw the spiral
        for i in range(120):
            alpha = 0.15  # Tightness of spiral
            radius = size * 0.3 * math.sqrt(i)
            galaxy.pensize(3 * size * (1 - i/120))
            
            # Create color gradient from white (center) to blue
            color_ratio = i / 120
            r = 1.0 - color_ratio * 0.7
            g = 1.0 - color_ratio * 0.5
            b = 1.0
            galaxy.pencolor(r, g, b)
            
            # Calculate new position on logarithmic spiral
            theta = alpha * i
            dx = radius * math.cos(theta)
            dy = radius * math.sin(theta)
            galaxy.goto(x + dx, y + dy)

# Shooting star
def draw_shooting_star():
    shooter = turtle.Turtle()
    shooter.hideturtle()
    shooter.speed(0)
    shooter.penup()
    
    # Random position at the edge of the screen
    side = random.randint(0, 3)
    if side == 0:  # Top
        x = random.randint(-350, 350)
        y = 250
        angle = random.randint(230, 310)
    elif side == 1:  # Right
        x = 350
        y = random.randint(-250, 250)
        angle = random.randint(140, 220)
    elif side == 2:  # Bottom
        x = random.randint(-350, 350)
        y = -250
        angle = random.randint(50, 130)
    else:  # Left
        x = -350
        y = random.randint(-250, 250)
        angle = random.randint(-40, 40)
    
    shooter.goto(x, y)
    shooter.setheading(angle)
    
    # Draw the shooting star trail
    shooter.pensize(2)
    shooter.pendown()
    
    length = random.randint(50, 150)
    for i in range(length):
        # Gradually fade from white to transparent
        fade = 1 - (i / length)
        shooter.pencolor(1, 1, 1 - 0.5*fade)
        shooter.forward(1)
    
    return shooter

# Main function
def main():
    # Draw background elements
    draw_moon(300, 200, 40)
    stars = draw_stars(100, 800, 600)
    
    # Draw some spiral galaxies
    draw_spiral_galaxy(-250, 180, 0.8, 45)
    draw_spiral_galaxy(150, -150, 0.6, 120)
    draw_spiral_galaxy(-180, -220, 0.5, 70)
    
    # Animation loop variables
    animation_frame = 0
    butterfly = None
    shooting_stars = []
    last_shooting_star_time = 0
    
    # Main animation loop
    while True:
        # Update twinkling stars
        twinkle_stars(stars)
        
        # Clear old butterfly and draw new one with updated colors
        if butterfly:
            butterfly.clear()
        butterfly = draw_parametric_butterfly(animation_frame * 0.1)
        
        # Draw body on top of butterfly
        draw_body()
        
        # Occasionally add a shooting star
        current_time = time.time()
        if current_time - last_shooting_star_time > 5:  # Every 5 seconds approximately
            if random.random() < 0.3:  # 30% chance
                shooting_stars.append(draw_shooting_star())
                last_shooting_star_time = current_time
        
        # Clean up old shooting stars to avoid memory issues
        if len(shooting_stars) > 5:
            old_star = shooting_stars.pop(0)
            old_star.clear()
        
        # Update the screen
        screen.update()
        
        # Control animation speed
        time.sleep(0.05)
        animation_frame += 1

# Run the program
if __name__ == "__main__":
        main()
