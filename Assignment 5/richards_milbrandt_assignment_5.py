"""
Assignment Name: Assignment 5 - Foxes & Rabbits Files

Authors: John Richards and Spencer Milbrandt

Description: This program will create a predator-prey simultaion using foxes and rabbits that will print to a 
file specified by user.

Additional Notes: This program will only run in python 3.X... to run this program 
in the terminal make sure you type: python3 futval.py

Date: 9/27/13
"""

def run_simulation():	
	print()	# adds a newline for nicer output.
	
	Rabbits = eval(input("What is the initial rabbit population: "))
	Foxes = eval(input("What is the initial fox population: "))
	days = eval(input("How many days should the simulation run: "))
	frequency = eval(input("What should the frequency of displayed dates be: "))
	myFile = input("What would you like the file to be name: ")

	myFile = (myFile + ".csv")
	
	infile = open("initvals.txt", "r")
	outfile = open(myFile, "w")
	
	# rabbit birth rate without predation 
	RABBIT_BIRTH_RATE = eval(infile.readline())

	# fox birth rate 
	FOX_BIRTH_RATE = eval(infile.readline())

	# INTERACT is the likelihood that a rabbit and fox will meet
	INTERACT = eval(infile.readline())

	# SUCCESS is the likelihood that when a fox & rabbit meet that the 
	#   fox catches the rabbit
	SUCCESS = eval(infile.readline())
	
	# Starting Day
	i=0

	# Intial List Values
	RabbitsList = [Rabbits]
	FoxesList = [Foxes]
	
	RabbitsAvg=0
	FoxesAvg=0
	
	# a for-loop to compute all the values into a list
	for i in range(0, days+1):
		temp_rabbits = (RABBIT_BIRTH_RATE * RabbitsList[i-1]) - (INTERACT * FoxesList[i-1] * RabbitsList[i-1])
		temp_fox = (INTERACT * SUCCESS * RabbitsList[i-1] * FoxesList[i-1]) - (FOX_BIRTH_RATE * FoxesList[i-1])
		RabbitsList.append(temp_rabbits + RabbitsList[i-1])
		FoxesList.append(temp_fox + FoxesList[i-1])
	
	# a for-loop to compute all the averages
	for i in range(0, days+1):
		RabbitsAvg = RabbitsList[i] + RabbitsAvg
		FoxesAvg = FoxesList[i] + FoxesAvg

	RabbitsAvg = RabbitsAvg / (days+1)
	FoxesAvg = FoxesAvg / (days+1)	
	
	#print statements to file	
	print("Day, Foxes, Rabbits, ,Average Foxes, Average Rabbits", file=outfile)
		
	for j in range(0, days+1, frequency):
			print (("{},{:0.3f},{:0.3f}").format(j, RabbitsList[j],FoxesList[j]),file=outfile)
	print()	# adds a newline for nicer output. 
	print("Simulation finished - results written to file ", myFile)
	outfile.close()
	infile.close()
run_simulation()
