"""

"""

# make sure to import things that you need...

def main():
	import math
	# rbr is the rabbit birth rate without predation 
	rBr = 0.01

	# fbr is the fox birth rate when no rabbits are available 
	fBr = 0.005

	# interaction is the likelihood that a rabbit and fox will meet
	I = 0.00001

	# hunt is the likelihood that when a fox & rabbit meet that the fox catches
	#   the rabbit
	S = 0.01
	
	# rabbits is the current rabbit population
	r = int(input("\nPlease enter the initial rabbit population: "))

	# foxes is the current fox population 
	f = int(input("Please enter the initial foxes population: "))

	# num_days is the number of days to run the simulation
	numD = int(input("Please enter the number of days to run the simulation: "))
	
	# display_freq is how often to display results in the table, does not impact calculations
	#	display always starts with initial populations
	displayFreq = int(input("Please enter the frequency of days for displaying data: "))

	# this code sets up two lists to contain the populations from the rounding calculations
	#	the first values in the list are the starting populations entered by the user 
	rR = [r]
	rF = [f]
	rRabbitsAvg = 0
	rFoxesAvg = 0
	
	fR = [r]
	fF = [f]
	fRabbitsAvg = 0
	fFoxesAvg = 0
	
	cR = [r]
	cF = [f]
	cRabbitsAvg = 0
	cFoxesAvg = 0
	
	flR = [r]
	flF = [f]
	flRabbitsAvg = 0
	flFoxesAvg = 0
	
	
	# Perform all of the population calculations in this loop
	# The new population values get appended to their corresponding lists 
	for i in range(0, numD + 1):
		# pass keeps Python from generating an error without any code in the loop
		# You can remove it or leave it
		pass
		
		# compute the new number of rabbits and foxes for the day and round the result
		changeR = round(rBr * rR[i] - I * rR[i] * rF[i])
		changeF = round(I * S * rR[i] * rF[i] - fBr * rF[i])
		
		rR.append(rR[i] + changeR)
		rF.append(rF[i] + changeF)

		# compute the new number of rabbits and foxes for the day and take the ceiling of result
		changeR = math.floor(rBr * fR[i] - I * fR[i] * fF[i])
		changeF = math.floor(I * S * fR[i] * fF[i] - fBr * fF[i])
		
		fR.append(fR[i] + changeR)
		fF.append(fF[i] + changeF)
		
		# compute the new number of rabbits and foxes for the day and take the floor of result
		changeR = math.ceil(rBr * cR[i] - I * cR[i] * cF[i])
		changeF = math.ceil(I * S * cR[i] * cF[i] - fBr * cF[i])
		
		cR.append(cR[i] + changeR)
		cF.append(cF[i] + changeF)
				
		# compute the new number of rabbits and foxes for the day and leave as a fraction
		changeR = float(rBr * flR[i] - I * flR[i] * flF[i])
		changeF = float(I * S * flR[i] * flF[i] - fBr * flF[i])
		
		flR.append(flR[i] + changeR)
		flF.append(flF[i] + changeF)
		
	
	# calculate all of the averages
	for i in range(0, numD + 1):
		rRabbitsAvg = rR[i] + rRabbitsAvg
		rFoxesAvg = rF[i] + rFoxesAvg
		
		fRabbitsAvg = fR[i] + fRabbitsAvg
		fFoxesAvg = fF[i] + fFoxesAvg
		
		cRabbitsAvg = cR[i] + cRabbitsAvg
		cFoxesAvg = cF[i] + cFoxesAvg
		
		flRabbitsAvg = flR[i] + flRabbitsAvg
		flFoxesAvg = flF[i] + flFoxesAvg
		
	rRabbitsAvg = rRabbitsAvg/(numD + 1)
	rFoxesAvg = rFoxesAvg/(numD + 1)
	
	fRabbitsAvg = fRabbitsAvg/(numD + 1)
	fFoxesAvg = fFoxesAvg/(numD + 1)
	
	cRabbitsAvg = cRabbitsAvg/(numD + 1)
	cFoxesAvg = cFoxesAvg/(numD + 1)
	
	flRabbitsAvg = flRabbitsAvg/(numD + 1)
	flFoxesAvg = flFoxesAvg/(numD + 1)
	
	
	# print out the averages
	# Here is how to do this for the rounding version
	#	will display a zero for both values until the calculations are completed
	print("\nRounded Population Averages:")
	print("{:9s}{:>10.3f}".format("Rabbits:", rRabbitsAvg))
	print("{:9s}{:>10.3f}".format("Foxes:", rFoxesAvg))
	print("\nFloor Population Averages:")
	print("{:9s}{:>10.3f}".format("Rabbits:", fRabbitsAvg))
	print("{:9s}{:>10.3f}".format("Foxes:", fFoxesAvg))
	print("\nCeiling Population Averages:")
	print("{:9s}{:>10.3f}".format("Rabbits:", cRabbitsAvg))
	print("{:9s}{:>10.3f}".format("Foxes:", cFoxesAvg))
	print("\nRaw Population Averages:")
	print("{:9s}{:>10.3f}".format("Rabbits:", flRabbitsAvg))
	print("{:9s}{:>10.3f}".format("Foxes:", flFoxesAvg))
	
	
	
	
	
	# print out Table Heading
	# Here is a version you can use as a guide. You don't have to keep it setup this way. 
	print()
	
	displayStr = "{:<10s}{:^20s}{:^19s}{:^20s}{:^29s}".format(
	"", "Rounded Values", "Floor Values", "Ceil Values", "Raw Values")
	print(displayStr)
	
	displayStr = "{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>15s}{:>15s}".format(
		"Day", "Rabbits", "Foxes", "Rabbits", "Foxes", "Rabbits", "Foxes", "Rabbits", "Foxes")
	print(displayStr)
	
	print("-" * 100)
		
	# create a for-loop to print out the values using the frequency that the user specified
	#	be sure to use string formatting to make everything line up nicely
	for j in range(0, numD + 1, displayFreq):
		displayStr = "{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>15.3f}{:>15.3f}".format(j, rR[j], rF[j], fR[j], fF[j], cR[j], cF[j], flR[j], flF[j])
		print(displayStr)
	
	
	print()
	
main()
