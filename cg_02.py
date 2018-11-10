import OpenGL.GL import*
import OpenGL.GLUT import*
import OpenGL.GLU import*
window=0
width,height=500,500

def draw_rect(x,y,width,height):
    glBegin(GL_QUADS) #start drawing a rectangle
    glVertex2f(x,y)   #bottom left point
    glVertex2f(x+width,y) #bottom rgiht point
    glVertex2f(x+width,y+height) #top right point
    glVertex2f(x,y+height) #top left point
    glEnd()
def refresh2d(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho describes a matrix that proudces a parallel projection(left,bottom and right,top)
    #left,bottom and right,top
    glOrtho(0.0,width,0.0,height,0.0,1.0)

    glMatrixMode(GL_MODELVIEW)

    glLoadIdentity()

def draw():                                     #ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  #clear the screen
    glLoadIdentity()
    #glColor3f(2.5,0.0,1.0)
    glColor3f(25,123,180)
    refresh2d(width,height)
    draw_rect(10,10,200,100)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_APLPHA | GLUT_DEPTH)
glutInitWindowSize(width,height)
glutInitWindowPosition(0,0)
window=glutCreateWindow("VIT-AP")
glutDisplayFunc(draw)
glutIdleFunc(draw)
