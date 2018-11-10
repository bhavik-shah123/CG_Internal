def setup():
    size(500,500);
    background(255);

def draw():
    fill(mouseX-50,mouseY-40,mouseY-50,250);
    lights();
    ellipse(mouseX,mouseY,50,50);
    click();

def click():
    if(keyPressed):
        background(255);
