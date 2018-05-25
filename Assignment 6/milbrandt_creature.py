"""
Assignment 6 - Graphics Library - Creature

By: Spencer Milbrandt

This program will display a creature that the programmer decides. 

This program can run on Python 3.X.  

Explanation for Creature:

This creature is the all popular Patrick Star from Spongebob Squarepants.
Patrick is full of wisdom (as you can tell) and has a great talent when it
comes to blowing bubbles. I chose this creature because Patrick Star was 
one of my favorite cartoon characters when growing up.

Date Created: 10/5/2013
Date Modified: 10/5/2013
"""
#Imports the common commands from graphics library.
from graphics import *

def main():
	#Import the graphics library.
	import graphics
	
	#Draws creature. Patrick Star.
	win = GraphWin('Patrick Star',500,500)
	
	head = Polygon(Point(200, 200),Point(300,200),Point(250,75))
	head.setFill('pink')
	head.setOutline('pink')
	head.draw(win)
	
	rightarm = Polygon(Point(300, 200), Point(400, 200), Point(325,250))
	rightarm.setFill('pink')
	rightarm.setOutline('pink')
	rightarm.draw(win)
	
	leftarm = Polygon(Point(200,200), Point(100,200), Point(175,250))
	leftarm.setFill('pink')
	leftarm.setOutline('pink')
	leftarm.draw(win)
	
	leftleg = Polygon(Point(175,250), Point(225,300), Point(150,400))
	leftleg.setFill('pink')
	leftleg.setOutline('pink')
	leftleg.draw(win)
	
	rightleg = Polygon(Point(325,250), Point(275,300), Point(350,400))
	rightleg.setFill('pink')
	rightleg.setOutline('pink')
	rightleg.draw(win)
	
	body = Polygon(Point(200,200), Point(300,200), Point(325,250), Point(275,300), Point(225,300), Point(175,250))
	body.setFill('pink')
	body.setOutline('pink')
	body.draw(win)
	
	pants = Polygon(Point(175,250), Point(325,250), Point(335,300), Point(165,300))
	pants.setFill("limegreen")
	pants.setOutline('limegreen')
	pants.draw(win)
	
	lefteye = Circle(Point(240,145), 10)
	lefteye.setFill('white')
	lefteye.draw(win)
	
	righteye = Circle(Point(260,145), 10)
	righteye.setFill('white')
	righteye.draw(win)
	
	leftpupil = Circle(Point(235,150), 2)
	leftpupil.setFill('black')
	leftpupil.draw(win)
	
	rightpupil = Circle(Point(265,140), 2)
	rightpupil.setFill('black')
	rightpupil.draw(win)
	
	firstflowerfirstpetal = Circle(Point(185,275), 10)
	firstflowerfirstpetal.setFill('purple')
	firstflowerfirstpetal.draw(win)
	
	firstflowersecondpetal = Circle(Point(200,265), 10)
	firstflowersecondpetal.setFill('purple')
	firstflowersecondpetal.draw(win)
	
	firstflowerthirdpetal = Circle(Point(200,283), 10)
	firstflowerthirdpetal.setFill('purple')
	firstflowerthirdpetal.draw(win)
	
	firstflowerfirstpetal = Circle(Point(185,275), 5)
	firstflowerfirstpetal.setFill('white')
	firstflowerfirstpetal.draw(win)
	
	firstflowersecondpetal = Circle(Point(200,265), 5)
	firstflowersecondpetal.setFill('white')
	firstflowersecondpetal.draw(win)
	
	firstflowerthirdpetal = Circle(Point(200,283), 5)
	firstflowerthirdpetal.setFill('white')
	firstflowerthirdpetal.draw(win)
	
	secondflowerfirstpetal = Circle(Point(235,275), 10)
	secondflowerfirstpetal.setFill('purple')
	secondflowerfirstpetal.draw(win)
	
	secondflowersecondpetal = Circle(Point(250,265), 10)
	secondflowersecondpetal.setFill('purple')
	secondflowersecondpetal.draw(win)
	
	secondflowerthirdpetal = Circle(Point(250,283), 10)
	secondflowerthirdpetal.setFill('purple')
	secondflowerthirdpetal.draw(win)
	
	secondflowerfirstpetal = Circle(Point(235,275), 5)
	secondflowerfirstpetal.setFill('white')
	secondflowerfirstpetal.draw(win)
	
	secondflowersecondpetal = Circle(Point(250,265), 5)
	secondflowersecondpetal.setFill('white')
	secondflowersecondpetal.draw(win)
	
	secondflowerthirdpetal = Circle(Point(250,283), 5)
	secondflowerthirdpetal.setFill('white')
	secondflowerthirdpetal.draw(win)
	
	thirdflowerfirstpetal = Circle(Point(295,275), 10)
	thirdflowerfirstpetal.setFill('purple')
	thirdflowerfirstpetal.draw(win)
	
	thirdflowersecondpetal = Circle(Point(310,265), 10)
	thirdflowersecondpetal.setFill('purple')
	thirdflowersecondpetal.draw(win)
	
	thirdflowerthirdpetal = Circle(Point(310,283), 10)
	thirdflowerthirdpetal.setFill('purple')
	thirdflowerthirdpetal.draw(win)
	
	thirdflowerfirstpetal = Circle(Point(295,275), 5)
	thirdflowerfirstpetal.setFill('white')
	thirdflowerfirstpetal.draw(win)
	
	thirdflowersecondpetal = Circle(Point(310,265), 5)
	thirdflowersecondpetal.setFill('white')
	thirdflowersecondpetal.draw(win)
	
	thirdflowerthirdpetal = Circle(Point(310,283), 5)
	thirdflowerthirdpetal.setFill('white')
	thirdflowerthirdpetal.draw(win)
	
	bottommouth = Oval(Point(225,175), Point(275,195))
	bottommouth.setFill('red')
	bottommouth.setOutline('red')
	bottommouth.draw(win)
	
	topmouth = Polygon(Point(225,175), Point(275,175), Point(275,183), Point(225,183))
	topmouth.setFill('pink')
	topmouth.setOutline('pink')
	topmouth.draw(win)
	
	bellybutton = Circle(Point(250,245), 1)
	bellybutton.setFill('black')
	bellybutton.draw(win)
	
	bubblewand = Line(Point(360,180), Point(375,225))
	bubblewand.setWidth(3)
	bubblewand.setFill('purple')
	bubblewand.draw(win)
	
	bubblewandend = Circle(Point(360,180), 10)
	bubblewandend.setFill('purple')
	bubblewandend.setOutline('purple')
	bubblewandend.draw(win)
	
	bubblewandendinside = Circle(Point(360,180), 7)
	bubblewandendinside.setFill('white')
	bubblewandendinside.setOutline('white')
	bubblewandendinside.draw(win)
	
	bubbleone = Circle(Point(360,140), 10)
	bubbleone.setFill('lightblue')
	bubbleone.setOutline('lightblue')
	bubbleone.draw(win)
	
	bubbletwo = Circle(Point(380,100), 10)
	bubbletwo.setFill('lightblue')
	bubbletwo.setOutline('lightblue')
	bubbletwo.draw(win)
	
	bubblethree = Circle(Point(420,60), 10)
	bubblethree.setFill('lightblue')
	bubblethree.setOutline('lightblue')
	bubblethree.draw(win)
	
	pantstwo = Polygon(Point(227,300), Point(250,280), Point(273,300))
	pantstwo.setFill('lightgrey')
	pantstwo.setOutline('lightgrey')
	pantstwo.draw(win)
	
	win.getMouse()
	win.close()
main()

