def setup():
  size(700,500);
  background(0);
  noStroke();


def draw():
  background(0);
  fill(0, 50);
  rect(0, 0, width, height);

  fill(255);
  ellipse(random(width), random(height), 10, 10);
