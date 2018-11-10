def thingy():
    strokeWeight(3)
    stroke(0,0,128)
    noFill()
    ellipse(325,250,50,50)
    for i in range(24):
        pushMatrix()
        translate(325,250)
        rotate(radians(15*(i+1)))
        line(0,0,0,25)
        popMatrix()
        
def setup():
    global img
    strokeWeight(3)
    background(255,0)
    size(800,600)
    fill(255,153,51)
    rect(100,100,450,100)
    fill(255)
    rect(100,200,450,100)
    fill(0,127,0)
    rect(100,300,450,100)
    thingy()
    
    img = get()
    
def draw():
    global img
    for i in range(width):
        image(img.get (i,0,1,img.height),i,25*sin(radians(i+millis())))
