from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0  #window number
width,height=500,500 #window size
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  #clear the screen
    glLoadIdentity()
    glColor3f(25, 123, 180)
    glutSwapBuffers()       #important for double buffering

glutInit()                  #initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_APLPHA | GLUT_DEPTH)
glutInitWindowSize(width,height)        #set window size
glutInitWindowPosition(0,0)             #set window position
window = glutCreateWindow("VIT-AP")     #create window with title
glutDisplayFunc(draw)                   #set draw function callback
glutIdleFunc(draw)                      #draw all the time
glutMainLoop()                          #start everything
