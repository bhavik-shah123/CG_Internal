x=0;
y=0; 
speedX=0; 
speedY=0;
diameter = 10;
rectSize = 200;

def setup():
    fullScreen();
    fill(0, 255, 0);
    reset();
    
def reset():
    global x;
    global y;
    global speedX;
    x=width/2;
    y=height/2;
    speedX = random(7, 10);
    speedY = random(7, 10);
    
def draw():
    global x;
    global y;
    global diameter;
    global speedX;
    global speedY;
    background(0);
    ellipse(x,y,diameter,diameter);
    rect(0,0,20,height);
    rect(width-30,mouseY-rectSize/2,10,rectSize);
    
    x+=speedX;
    y+=speedY;
    
    if(x>width-30 and x<width-20 and y>mouseY-rectSize/2 and y<mouseY+rectSize/2):
        speedX = speedX*(-1);
        
    if(x<25):
        speedX*=-1.1;
        speedY*=1.1;
        x+=speedX;
        
    if(y>height or y<0):
        speedY*=-1;
        
def mousePressed():
    reset();
