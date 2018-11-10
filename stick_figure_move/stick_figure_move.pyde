def setup():
    size(800,800);

def draw():
    background(255)
    translate(mouseX-60,mouseY-60);

    ellipse(250,50,100,100);
    rect(250,101,1,200);
    line(250,173,350,243);
    line(250,173,150,243);
    line(250,301,190,425);
    line(250,301,310,425);


    #popMatrix()
    #to fill colour dynamically we use fill(mouseX,mouseY,mouseY,100)
