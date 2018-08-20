import pygame,sys

FPS = 200
WINDOWHEIGHT = 480
WINDOWWIDTH = 640
POFFSET = 20
LTHICKNESS = 10
PSIZE = 40

computerScore =0 
playerScore =0 
#colores
BLACK = (0,0,0)
WHITE = (255,255,255)


def drawArena():
	DISPLAYSURF.fill((0,0,0))
	pygame.draw.rect(DISPLAYSURF,WHITE,((0,0),(WINDOWWIDTH,WINDOWHEIGHT)) , LTHICKNESS*2)
	pygame.draw.line(DISPLAYSURF, WHITE, (int((WINDOWWIDTH/2)),0),(int((WINDOWWIDTH/2)),WINDOWHEIGHT), int((LTHICKNESS/4)))


def drawPaddle(paddle):
	if(paddle.bottom > WINDOWHEIGHT-LTHICKNESS):
		paddle.bottom = WINDOWHEIGHT-LTHICKNESS
	if paddle.top < LTHICKNESS:
		paddle.top = LTHICKNESS

	pygame.draw.rect(DISPLAYSURF,WHITE,paddle)

def drawBall(ball):
	pygame.draw.rect(DISPLAYSURF,WHITE,ball)


def moveBall(ball,BDX,BDY):
	ball.x += BDX
	ball.y += BDY
	return ball 

def checkBallColl(ball,BDX,BDY):
	if ball.top == LTHICKNESS or ball.bottom == (WINDOWHEIGHT-LTHICKNESS):
		BDY = -BDY
	if ball.left == LTHICKNESS or ball.right == (WINDOWWIDTH-LTHICKNESS):
		BDX = -BDX

	return BDX,BDY

def checkPaddleColl(ball,paddle1,paddle2,BDX):
	if (ball.left == paddle1.right and BDX == -1 and paddle1.top < ball.top and paddle1.bottom > ball.bottom ):
		return -1
	if (ball.right == paddle2.left and BDX == 1 and paddle2.top < ball.top and paddle2.bottom > ball.bottom ):
		return -1
	else: return 1

def opponentAI(ball,paddle,BDX):
	if(BDX == -1):
		if(paddle.centery > (WINDOWHEIGHT-LTHICKNESS*2)/2):
			paddle.y -=1
		elif(paddle.centery < (WINDOWHEIGHT-LTHICKNESS*2)/2):
			paddle.y +=1
	elif(BDX == 1):
		if(paddle.centery < ball.centery):
			paddle.y += 1
		elif(paddle.centery > ball.centery):
			paddle.y -= 1

def calcScore(ball):
	global computerScore
	global playerScore
	if(ball.left == LTHICKNESS):
		computerScore +=1
	elif(ball.right == WINDOWWIDTH-LTHICKNESS):
		playerScore +=1



def displayCompScore():
	text = "COM = "+str(computerScore)
	resultSurf = gameFont.render(text,True ,WHITE)
	resultRect = resultSurf.get_rect()
	resultRect.topleft = (WINDOWWIDTH- 160,25)
	DISPLAYSURF.blit(resultSurf, resultRect)

def displayPlayerScore():
	resultSurf2 = gameFont.render('PLA = %s'%(playerScore),True,WHITE)
	resultRect2 = resultSurf2.get_rect()
	resultRect2.topleft = (WINDOWWIDTH - 160,55)
	DISPLAYSURF.blit(resultSurf2,resultRect2)





def main():
	pygame.init()
	global DISPLAYSURF
	global gameFont, gameFontSize
	gameFontSize = 20
	gameFont = pygame.font.Font('PressStart2P.ttf',gameFontSize)

	#playerScore = 0
	#computerScore =0



	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF= pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption('Ping hehe')

	ballX = (WINDOWWIDTH-LTHICKNESS)/2
	ballY = (WINDOWHEIGHT-LTHICKNESS)/2

	pad1 = (WINDOWHEIGHT-PSIZE)/2

	pad2 = (WINDOWHEIGHT-PSIZE)/2

	ballDirX = 1
	ballDirY = 1

	paddle1 = pygame.Rect(POFFSET,pad1,LTHICKNESS, PSIZE)
	paddle2 = pygame.Rect(WINDOWWIDTH - POFFSET - LTHICKNESS,pad2,LTHICKNESS, PSIZE)
	ball = pygame.Rect(ballX,ballY,LTHICKNESS,LTHICKNESS)
	ball = moveBall(ball,ballDirX,ballDirY)

	drawArena()
	drawPaddle(paddle1)
	drawPaddle(paddle2)
	drawBall(ball)
	ball = moveBall(ball,ballDirX,ballDirY)
	#ballDirX = checkPaddleColl(ball,paddle1,ballDirX)

	#playerScore = 0
	#computerScore = 0
	pygame.mouse.set_visible(0)




	while True:
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				sys.exit();
			elif (event.type == pygame.MOUSEMOTION):
				mousex,mousey = event.pos
				paddle1.y = mousey
		
		drawArena()
		drawPaddle(paddle1)
		drawPaddle(paddle2)
		drawBall(ball)
		ball = moveBall(ball,ballDirX,ballDirY)
		ballDirX,ballDirY = checkBallColl(ball,ballDirX,ballDirY)
		ballDirX = ballDirX* checkPaddleColl(ball,paddle1,paddle2,ballDirX)
		opponentAI(ball,paddle2,ballDirX)
		
		calcScore(ball)
		displayPlayerScore()
		displayCompScore()		
		
		


		pygame.display.update()
		FPSCLOCK.tick(FPS)


if __name__=='__main__':
	main()
