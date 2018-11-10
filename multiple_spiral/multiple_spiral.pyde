x=0;
y=0;
number_of_points=1000;
circle_diameter = 5;
plot_radius = 200;
angle_incr = radians(25);
def setup():
    size(1000,1000);
    fill(random(255));
    smooth(8);
    noStroke();
def draw():
    global x;
    global y;
    global number_of_points;
    global plot_radius;
    global cirlce_diameter;
    global angle_incr;
    background(255);
    translate(width/2,height/2);
    for i in range(number_of_points):
        ratio = i/float(number_of_points);
        spiral_radius = ratio*plot_radius;
        angle = i*angle_incr;
        x = cos(angle)*spiral_radius;
        y = sin(angle)*spiral_radius;
        rotate(radians(-0.0009*frameCount));
        ellipse(x,y,circle_diameter,circle_diameter);
               
