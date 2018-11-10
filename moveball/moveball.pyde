x=40
y=375
move_x = 5;

def setup():
    size(500,600);

def draw():
    background(0);
    fill(255,0,0);
    rect(0,400,500,600);
    noFill();
    move();


def move():
    global x;
    global move_x;
    fill(255);
    ellipse(x,y,50,50);
    noFill();
    if(keyPressed):
        fill(255);
        ellipse(x,y,50,50);
        noFill();
        x = x+move_x;
        if(x>width):
            x = width;
            move_x = -move_x;
        if(x<0):
            x=0;
            move_x = -move_x;
