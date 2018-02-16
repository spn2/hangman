from graphics import *
from random import randint

def makeCopy(secretWord):
	"""Returns a list of underscores with the same length 
	as the word in the input"""
	
	return ["_"]*len(secretWord)
	
def showScreen(secretList):
	"""Creates and returns a window, word written in window
	and height/width of the window"""
	
	height = 500
	width = 250
	win = GraphWin("Hangman", width, height)
	middleOfWord = Point(width/2, height/2 + 175)
	word = Text(middleOfWord, secretList)
	word.draw(win)
	
	return win, word, height, width
	
def getWord(secretWord):
	"""Show the secretList in the graphics window using the functions makeCopy and
	showScreen."""
	
	#get the secretList based on our word
	secretList = makeCopy(secretWord)
	#showScreen returns a tuple of length 3, 0th entry is the window
	win = showScreen(secretList)[0]
	
	win.getMouse()
	win.close()

def checkHit(secretWord, secretList, ltr):
	"""Return secretList and hits; the updated secretList with the guessed letters ,
	and the number of hits for the currect guessed letter (which is 0 is it
	doesn’t occur in the word or if it was guessed earlier)"""
	
	#variable to keep track of our pos in secretList
	index = 0
	#number of times ltr is in secretWord
	hits = 0
	for letter in secretWord:
		#letters match
		if letter == ltr:
			#update secretList at the correct place
			secretList[index] = ltr
			hits += 1
		#up the index
		index += 1
		
	return secretList, hits

def askLtr(secretWord, secretList):
	"""In a loop, until the word has been guessed , it asks the player to enter a
	letter , and then updates the secretList accordingly. If a correct letter
	has been guessed , a happy message will be displayed and the guessed letter
	will be shown in the word. Otherwise , a sad message is displayed. """
	
	win, word, width, height = showScreen(secretList)
	#we will increase counter by 1 for each fail
	counter = 0
	
	#starting text
	startText = Text(Point(125,125), "Guess a letter")
	startText.draw(win)
	
	#check to see if the letter given by input is in the word
	secretList, hits = checkHit(secretWord, secretList, input(""))
	#undraw the start text and the current drawn secretList
	startText.undraw()
	word.undraw()
	
	#9 "lives" + the 1 "life" above = 10 "lives"
	while counter < 9:
	
		#draw the new secretList to window
		word = Text(Point(height/2, width/2), secretList)
		word.draw(win)
		
		#if success, print msg
		if hits > 0:
		
			hitText = Text(Point(125,125), "Well done, guess again")
			hitText.draw(win)
		#if failure, increment counter, print msg
		else:
		
			hitText = Text(Point(125, 125), "Not in word, guess again.")
			hitText.draw(win)
			counter += 1
		
		#get new character, get new secretList
		secretList, hits = checkHit(secretWord, secretList, input(""))
		
		#if there are no more blanks in secretList, player won
		if "_" not in secretList:
		
			#set the stage for the victory message
			hitText.undraw()
			word.undraw()
			word = Text(Point(height/2, width/2), secretList)
			word.draw(win)
			
			#victory message
			successText = Text(Point(125,125), "You have guessed the word.")
			successText.draw(win)
			
			#get mouse and exit function 
			win.getMouse()
			return
			
		#undraw msg and secretList	
		hitText.undraw()
		word.undraw()

def task1c():

	width = 250
	height = 500
	win = GraphWin("Hangman", width, height)
	
	#loop through 1 to 10 in reverse order (10, 9, ..)
	for lives in range(10, 0, -1):
	
		input("Enter to continue")
		drawHangman(lives, win, width, height)
	
	win.getMouse()
	win.close()

def drawHangman(lives , win, width , height):

	if lives == 10:
		drawBottom(win, width , height)
	elif lives == 9:
		drawVertical(win, width , height)
	elif lives == 8:
		drawTop(win, width , height)
	elif lives == 7:
		drawNoose(win, width , height)
	elif lives == 6:
		drawHead(win, width , height)
	elif lives == 5:
		drawBody(win, width , height)
	elif lives == 4:
		drawArm(win, width , height , "left")
	elif lives == 3:
		drawArm(win, width , height , "right")
	elif lives == 2:
		drawLeg(win, width , height , "left")
	elif lives == 1:
		drawLeg(win, width , height , "right")

def drawBottom(win, width , height):

	left = width/4
	right = width - width/4
	bottom = height - height/4
	bottomLeft = Point(width/8, height*3/4)
	bottomRight = Point(width*7/8, height*3/4)
	bottomBar = Line(bottomLeft , bottomRight)
	bottomBar.draw(win)

def drawVertical(win, width , height):

	bottomLeft = Point(width/8, height*3/4)
	topLeft = Point(width/8, height/8)
	verticalBar = Line(bottomLeft , topLeft)
	verticalBar.draw(win)

def drawTop(win, width , height):

	topBar = Line(Point(width/8, height/8), Point(width/2, height/8))
	topBar.draw(win)
	
def drawNoose(win, width , height):

	nooseBar = Line(Point(width/2, height/8), Point(width/2, height/4))
	nooseBar.draw(win)
	
def drawHead(win, width , height):

	headCircle = Circle(Point(width/2, height/4 + 35), 35)
	headCircle.draw(win)
	
def drawBody(win, width , height):

	#body starts where nooseBar ends + 2 radiuses of head = 2*35 = 70
	#downwards in the height/y direction
	bodyBar = Line(Point(width/2, height/4+70), Point(width/2, height/2 + 50))
	bodyBar.draw(win)
	
def drawArm(win, width , height , side):

	if side.lower() == "left":
	
		leftArm = Line(Point(width/2, height/2-15), Point(width/2 + 20, height/2 +40))
		leftArm.draw(win)
		
	elif side.lower() == "right":
	
		rightArm = Line(Point(width/2, height/2-15), Point(width/2 - 20, height/2 +40))
		rightArm.draw(win)
		
	else:
		pass
	
def drawLeg(win, width , height , side):

	if side.lower() == "left":
		leftLeg = Line(Point(width/2, height/2 + 50), Point(width/2 + 20, height/2 +100))
		leftLeg.draw(win)
		
	elif side.lower() == "right":
	
		rightLeg = Line(Point(width/2, height/2 + 50), Point(width/2 -  20, height/2 +100))
		rightLeg.draw(win)
		
	else:
		pass

def play(secretWord):

	lives = 10
	secretList = makeCopy(secretWord)
	
	#call showScreen, create window
	win, word, height, width = showScreen(secretList)
	
	startText = Text(Point(125,25), "Guess a letter")
	startText.draw(win)
	
	#get letter input, check if it's in the secret word
	ltr = input("").lower()
	secretList, hits = checkHit(secretWord, secretList, ltr)
	#remove starttext
	startText.undraw()
	#as long as the player has lives
	while lives > 0:
	
		#draw secretList to window
		word = Text(Point(width/2, height/2 + 175), secretList)
		word.draw(win)
		
		#lose on 1 lives since lives are deducted later on
		if lives == 1:
		
			#remove excess text
			hitText.undraw()
			#draw on the last leg
			drawHangman(lives, win, width, height)
			
			#loser text
			loseText = Text(Point(125,25), "You have not guessed the word.")
			loseText.draw(win)
			win.getMouse()
			
			return
		
		#if user guessed one right letter, print msg
		if hits == 1:
		
			hitText = Text(Point(125,25), "Well done, guess again")
			hitText.draw(win)
			
		#if user guessed several right letters, print different msg
		if hits > 1:
		
			hitText = Text(Point(125,25), "Well done, you hit several letters.\nGuess again")
			hitText.draw(win)
		
		#if failure, print msg, start/continue drawing the hanging man
		elif hits == 0:
		
			hitText = Text(Point(125, 25), "Not in word, guess again.")
			hitText.draw(win)
			#draw relevant part of the hanging man
			drawHangman(lives, win, width, height)
			#lose a life
			lives += -1
			
		#update secretList
		secretList, hits = checkHit(secretWord, secretList, input(""))
		
		#win when secretList has no more "_"'s
		if "_" not in secretList:
		
			#remove excess text
			hitText.undraw()
			#remove secretList with one underscore
			word.undraw()
			#draw final iteration of secretList with all letters
			word = Text(Point(width/2, height/2 + 175), secretList)
			word.draw(win)
			
			#winner text
			winText = Text(Point(125,25), "You have guessed the word.")
			winText.draw(win)
			win.getMouse()
			
			#exit
			return
		
		#undraw secretList and success/failure text to prep for next iteration
		word.undraw()
		hitText.undraw()
	
	win.getMouse()
	win.close()
	
def random_word():
#select random word from dictionary

	infile = open(input("Enter dictionary file\n>"), 'r')
	
	
	infile.close()
	
	return word
