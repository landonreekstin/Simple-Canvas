"""
ScribbleColor.py
Landon Reekstin
Program to allow user to draw with multiple colors from a toolbox

Worked with Delwys on 9/14 and 9/16
"""


import pyglet
from pyglet.gl import GL_LINES, glBegin, glEnd, glVertex3f, glColor4f
window = pyglet.window.Window(1024, 720, "Scribble", resizable=False)

# Global variable to save state of color, this is modified on mouse press
current_color = (1.0, 1.0, 16.0, 1.0) 

# Class to save line segment start, end, and color
class Vectors:
    # add init
    def __init__(self, start_x, start_y, end_x, end_y, color):
        self.vector_array = start_x, start_y, end_x, end_y
        # add color
        self.vector_color = color


# Class to create toolbox boxes in window
class ColorToolbox:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_rect(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
        ('v2f', [self.x, self.y, self.x + self.width, self.y, self.x + self.width, 
        self.y + self.height, self.x, self.y + self.height]))

#drawing vectors
drawing_vec = []
isDrawing = False
startPoint = None

@window.event
def on_mouse_press(x, y, button, modifiers):
    global isDrawing, startPoint, current_color
    isDrawing = True
    startPoint = (x, y)

     # activating color toolbox
    # check if red
    if 0 <= x <= 99 and 0 <= y <= 99:
        current_color = (1.0, 0.0, 0.0, 1)
    # check if orange
    elif 100 <= x <= 199 and 0 <= y <= 99:
        current_color = (1.0, 0.5, 0.0, 1)
    # check if yellow
    elif 200 <= x <= 299 and 0 <= y <= 99:
        current_color = (1.0, 1.0, 0.0, 1)
    # check if green
    elif 300 <= x <= 399 and 0 <= y <= 99:
        current_color = (0.0, 1.0, 0.0, 1)
    # check if blue
    elif 400 <= x <= 499 and 0 <= y <= 99:
        current_color = (0.0, 0.0, 1.0, 1)
    # check if purple
    elif 500 <= x <= 599 and 0 <= y <= 99:
        current_color = (1.0, 0.0, 1.0, 1)
    # check if white
    elif 600 <= x <= 699 and 0 <= y <= 99:
        current_color = (1.0, 1.0, 1.0, 1)
    # check if clear all and if so, remove all items from drawing_vector
    # credit to Delwys for idea to bind clear all functionality to a toolbox
    elif 700 <= x <= 750 and 0 <= y <= 50:
        drawing_vec.clear() # turns out Python has a built in function to remove all items from a list

# Handle mouse dragging
@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    global isDrawing, startPoint, drawing_vec

    # on mouse drag, give vector start, end and color
    if isDrawing == True:
        drawing_vec.append(Vectors(startPoint[0], startPoint[1], x, y, current_color))
        startPoint = (x, y)

# Handle mouse release 
@window.event
def on_mouse_release(x, y, button, modifiers):
    global isDrawing, startPoint, drawing_vec
    isDrawing = False

    drawing_vec.append(Vectors(startPoint[0], startPoint[1], x, y, current_color))


# Handle drawing
# This function refreshes the window at 60Hz, redrawing the information stored in drawing_vector
@window.event
def on_draw():
    global current_color

    window.clear()
    # Begin Drawing
    glBegin(GL_LINES)

    # set current color
    glColor4f(*current_color)

    #create a line w/ x, y, z
    global drawing_vec

    # calls Vector class function to redraw itself (with color)
    #on draw loops through object vector coordinates and draws vector with color
    if not drawing_vec == None:
        for vector in drawing_vec:
            # change color
            glColor4f(*vector.vector_color)
            glVertex3f(vector.vector_array[0], vector.vector_array[1], 0.0)
            glVertex3f(vector.vector_array[2], vector.vector_array[3], 0.0)
    glEnd()

    # Creating the 6 toolboxes
    # Red Box
    glColor4f(1.0, 0.0, 0.0, 1)
    t1 = ColorToolbox(0, 0, 99, 99)
    t1.draw_rect()

    # Orange Box
    glColor4f(1.0, 0.5, 0.0, 1)
    t1 = ColorToolbox(100, 0, 99, 99)
    t1.draw_rect()

    # Yellow Box
    glColor4f(1.0, 1.0, 0.0, 1)
    t1 = ColorToolbox(200, 0, 99, 99)
    t1.draw_rect()

    # Green Box
    glColor4f(0.0, 1.0, 0.0, 1)
    t1 = ColorToolbox(300, 0, 99, 99)
    t1.draw_rect()

    # Blue Box
    glColor4f(0.0, 0.0, 1.0, 1)
    t1 = ColorToolbox(400, 0, 99, 99)
    t1.draw_rect()

    # Purple Box
    glColor4f(1.0, 0.0, 1.0, 1)
    t1 = ColorToolbox(500, 0, 99, 99)
    t1.draw_rect()

    # White Box
    glColor4f(1.0, 1.0, 1.0, 1)
    t1 = ColorToolbox(600, 0, 99, 99)
    t1.draw_rect()

    # Clear all box
    glColor4f(0.5, 0.5, 0.5, 1)
    t1 = ColorToolbox(700, 0, 50, 50)
    t1.draw_rect()


def update(dt):
    pass


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()