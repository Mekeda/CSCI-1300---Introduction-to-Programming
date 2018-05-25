"""
# put required comments here
"""

def run_simulation():
	import math	
	print()	# adds a newline for nicer output.
	
	# rabbit birth rate without predation 
	rBr = 0.01

	# fox birth rate 
	fBr = 0.005

	# INTERACT is the likelihood that a rabbit and fox will meet
	I = 0.00001

	# SUCCESS is the likelihood that when a fox & rabbit meet that the 
	#   fox catches the rabbit
	S = 0.01

	# 1. Gather data from user, one value per input 
	R = int(input("Enter the starting rabbit population: "))
	F = int(input("Enter the starting fox population: "))
	numD = int(input("Enter the number of days this simulation will run: "))
	i=0
	
	rR = [R]
	rF = [F]
	# 2. print out some header info here with labels for days, rabbits, foxes 
	print("Days",'\t',"Rabbits",'\t',"Foxes")
	print("-----------------------------------------")
	
	# 3. print out the starting simulation values
	print(i,'\t',R,'\t','\t',F)

	# 4. write a for-loop to iterate through the simulated days
	for i in range(numD):
	
		# 5. calculate the new daily populations
		R = float(R+(rBr*R-I*R*F))
		F = float(F+(I*S*R*F-fBr*F))
	
		# 6. print out new day population information
		print("{.3f}"'\t'"{.3f}"'\t''\t'"{.3f}".format(i+1, R, F))
   

	print()	# adds a newline for nicer output. 

run_simulation()
