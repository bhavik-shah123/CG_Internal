c = color(0)
x = 0.0
y = 100.0
speed = 50.0

def setup():
    size(500,500);

def draw():
    background(255);
    move();
    display();

def move():
    global x;
    x = x+speed
    if(x>width):
        x=0

def display():
    fill(255,120,255)  #for changing color dynamically use fill(x,x/2,x/5)
    rect(x,y,50,50)
