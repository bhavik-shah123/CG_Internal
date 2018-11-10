def setup():
    size(500,500,P3D);

def draw():
    background(255);
    translate(250,250);
    lights();
    fill(mouseX,mouseY,mouseX,200);
    rotate(120);
    sphere(150);
#for stroke manipulation use stroke(x,y,z) and strokeWeight()
