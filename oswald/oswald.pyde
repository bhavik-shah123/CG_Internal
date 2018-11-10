def head():
    pushMatrix();
    noStroke();
    fill(0,0,255);
    translate(400,250,0);
    rotate(150);
    sphere(150);
    noFill();
    popMatrix();
    pushMatrix();
    fill(0);
    translate(340,270,251);
    sphere(5);
    noFill();
    popMatrix();
    pushMatrix();
    fill(0);
    translate(459,270,251);
    sphere(5);
    noFill();
    popMatrix();
    pushMatrix();
    stroke(0);
    popMatrix();

    
def setup():
    size(800,800,P3D);
    
def draw():
    head();
    print(mouseX,mouseY);
