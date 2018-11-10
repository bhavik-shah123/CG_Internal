paddleLx=20;
paddleLy=200;
paddleRx=380;
paddleRy=200;
ballX=0;
ballY=0;
ballVx=0;
ballVy=0;
ballSize = 20;
paddleWidth = 20;
paddleHeight = 60;
bigWidth = (ballSize + paddleWidth)/2;
bigHeight = (ballSize + paddleHeight)/2;
gameOn = 0;
ticker = 0;
LScore = 0;
RScore = 0;

def restart():
    paddleLx = 20;
    paddleLy = 200;
    paddleRx = 380;
    paddleRy = 200;
    ballX = paddleLx + ballSize;
    ballY = paddleRy;
    ballVx = 0;
    ballVy = 0;
    paddleLx = 20;
    paddleLy = 200;
    paddleRx = 380;
    paddleRy = 200;
    
def setup():
    size(400,400);
    background(0);
    restart();
    textSize(80);
    fill(255);
    text("PONG", 100, 160);
    text("MANIA", 120, 240);
    fill(0,0,255);
    text("PONG",100+3,160+3);
    text("MANIA",120+3,240+3);
    
def mousePressed():
    global gameOn;
    if(gameOn == 0):
        gameOn = 1;
        ballVx = 5;
    else:
        restart();
        gameOn = 0;
        
def update():
    background(0);
    fill(255,100);
    textSize(32);
    text(LScore, 10,30);
    text(RScore, 360,30);
    
    paddleLy = mouseY;
    ballX += ballVx;
    ballY += ballVy;
    
    ++ticker;
    
    paddleRy = int(ballY+50*sin(sin((ballY+ticker)/30)));
    
    if(ballY<0 or ballY>400):
        ballVy *= -1;
    elif((paddleLx-bigWidth < ballX) and (ballX < paddleLx+bigWidth) and (paddleLy-bigHeight < ballY) and (ballY < paddleLy+bigHeight)):
        ballVy = ((ballVy-paddleLy)/float(bigHeight))*4;
        ballVx *= -1;
        ballX += 1;
    elif((paddleRx-bigWidth < ballX) and (ballX < paddleRx+bigWidth) and (paddleRy-bigHeight < ballY) and (ballY < paddleRy+bigHeight)):
        ballVy = ((ballY-paddleRy)/float(bigHeight))*4;
        ballVx *= -1;
        ballX -= 1;
    elif(ballX < -2):
        ballVx = ballVy = 0;
        textSize(32);
        text("You Lose", 200,200);
        +++RScore;
        gameOn = 0;
        restart();
    elif(ballX>402):
        ballVx = ballVy = 0;
        textSize(32);
        text("You Win", 200, 200);
        ++LScore;
        gameOn = 0;
        restart();
        
def draw():
    if(gameOn == 1):
        update();
        
    fill(255);
    rect(paddleLx-(paddleWidth/2), paddleLy-(paddleHeight/2), paddleWidth, paddleHeight);
    rect(paddleRx-(paddleWidth/2), paddleRy-(paddleHeight/2), paddleWidth, paddleHeight);
    ellipse(int(ballX),int(ballY),ballSize,ballSize);
