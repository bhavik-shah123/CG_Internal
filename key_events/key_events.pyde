def setup():
    size(500,500);
    background('#3355CC');

def draw():
    fill(40,20);
    rect(0,0,width,height);

def keyPressed():
    fill('#FFEE200');
    textSize(random(20,200));
    text(key,random(300),random(100,400));
