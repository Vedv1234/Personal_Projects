"""
Author: Ved Vyas
Functionality of code: 
Hey! This is my cool 3D carrot program. I wanted to create something fun with OpenGL,
so I made this carrot that spins around and looks pretty realistic. I'm using simple
geometric shapes to build it up - kind of like digital sculpting! I've got a nice
orange cone for the body and some spiky green leaves on top. The whole thing rotates
smoothly and you can control it with arrow keys.
"""

# I need these libraries to make my 3D graphics work
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_carrot_body():
    """
    This is where I create the main orange part of my carrot.
    I'm using a cone shape made with triangles - it's like a 3D pizza slice!
    """
    glBegin(GL_TRIANGLE_FAN)
    # First I'll make the pointy end - every carrot needs a good point!
    glColor3f(1.0, 0.5, 0.0)  # This orange color reminds me of actual carrots
    glVertex3f(0.0, -1.5, 0.0)  # The tip goes at the bottom
    
    # Now I'll make the top circle - this is like drawing with a compass
    radius = 0.3  # Not too fat, not too skinny
    segments = 32  # More segments = smoother circle
    glColor3f(1.0, 0.6, 0.0)  # I made the top slightly lighter for some style
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, 0.5, z)
    glEnd()

    # Adding some texture lines to make it look more carrot-like
    glBegin(GL_LINES)
    glColor3f(0.9, 0.4, 0.0)  # Darker orange for the lines - looks more natural
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, 0.5, z)  # Start at the top
        glVertex3f(0.0, -1.5, 0.0)  # End at the tip
    glEnd()

def draw_leaf():
    """
    Here's my leaf-drawing function. Each leaf is just a simple triangle,
    but when you put a bunch together, they look pretty leafy!
    """
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.8, 0.0)  # Nice bright green - like fresh carrot tops
    glVertex3f(0.0, 0.5, 0.0)    # Where the leaf meets the carrot
    glVertex3f(0.0, 1.5, 0.0)    # The pointy tip
    glVertex3f(0.2, 0.8, 0.1)    # A little bend for style
    glEnd()

def draw_leaves():
    """
    This is where I arrange all my leaves in a nice circle.
    Five leaves seems to look just right!
    """
    # I'm spacing my leaves evenly around the top - like a little green crown
    angles = [0, 72, 144, 216, 288]  # 360 degrees divided into 5 parts
    for angle in angles:
        glPushMatrix()  # Save my current position
        glRotatef(angle, 0, 1, 0)  # Spin around to the next leaf spot
        glRotatef(30, 1, 0, 0)     # Tilt it outward - looks more natural
        draw_leaf()
        glPopMatrix()  # Back to my saved position

def draw_carrot():
    """
    Here's where I put everything together - like assembling a puzzle!
    """
    # First the orange part
    draw_carrot_body()
    # Then the leafy top
    draw_leaves()

def main():
    # Setting up my window and OpenGL stuff
    pygame.init()
    display = (800, 600)  # Nice size for viewing
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("My 3D Carrot")  # Look, it's got a title!

    # I need these for proper 3D viewing
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)  # Back up a bit to see the whole carrot

    # I like this gray background - makes the carrot stand out
    glClearColor(0.5, 0.5, 0.5, 1)
    
    # These help me keep track of rotation
    rot_x = 0
    rot_y = 0

    # This is my main loop where all the action happens
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # Here's my arrow key controls - pretty neat!
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rot_y -= 1
                elif event.key == pygame.K_RIGHT:
                    rot_y += 1
                elif event.key == pygame.K_UP:
                    rot_x -= 1
                elif event.key == pygame.K_DOWN:
                    rot_x += 1

        # Clear everything for the next frame
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # This is my rotation code - makes it spin nice and smooth
        glRotatef(1 + rot_x, 1, 0, 0)
        glRotatef(1 + rot_y, 0, 1, 0)
        
        # Draw my awesome carrot!
        draw_carrot()
        
        # Show it on screen
        pygame.display.flip()
        
        # Don't spin too fast - makes it easier to watch
        pygame.time.wait(10)

# Start everything running!
if __name__ == "__main__":
    main()